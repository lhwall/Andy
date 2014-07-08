''' 
jhjk
'''
import psycopg2
import psycopg2 as dbapi2
import psycopg2.extensions as e
import sys


class CreateDB:
    
    ISOLATION_LEVEL_AUTOCOMMIT = e.ISOLATION_LEVEL_AUTOCOMMIT
    ISOLATION_LEVEL_READ_COMMITTED = e.ISOLATION_LEVEL_READ_COMMITTED
    ISOLATION_LEVEL_SERIALIZABLE = e.ISOLATION_LEVEL_SERIALIZABLE 
    def __init__(self, name):
        '''
        Constructor
        
        self._admin_engine = create_engine(
                '%s+%s://%s:%s@%s/postgres'%(self.vendor, self.driver, self.user,
                                             self.password, self.host))
        self._AdminSession = sessionmaker(bind=self._admin_engine)
         '''
        self.name = " Create database GarbageRecyler  OWNER postgres TABLESPACE salesspace;"



    def create(self):
        """Create this database"""
        # set isolation level to AUTOCOMMIT
        # postgres can't CREATE databases within a transaction
        ISOLATION_LEVEL_AUTOCOMMIT = e.ISOLATION_LEVEL_AUTOCOMMIT
        ISOLATION_LEVEL_READ_COMMITTED = e.ISOLATION_LEVEL_READ_COMMITTED
        ISOLATION_LEVEL_SERIALIZABLE = e.ISOLATION_LEVEL_SERIALIZABLE
        # conn = self._admin_engine.connect()
        conn = dbapi2.connect(database = 'postgres', user = 'postgres', password = 'admin')
        
        conn.connection.connection.set_isolation_level(
            ISOLATION_LEVEL_AUTOCOMMIT)
        # Create database GarbageRecyler  OWNER postgres TABLESPACE salesspace
        createDBStr0 = " Create database GarbageRecyler"

        # conn.execute('CREATE DATABASE %s'%(self.name))
        conn.execute('%s'%(createDBStr0))
        # conn.connection.connection.set_isolation_level(
         #S   ISOLATION_LEVEL_READ_COMMITTED) 
        # conn.commit()   
        conn.close()
    
    def connectDB(self, host ='localhost', port = '5432'):
        con = None
        
        try:
            
            #con = psycopg2.connect(user = 'postgres', password = 'admin') 
            connectDb = dbapi2.connect(database = 'garbagerecyler', user = 'postgres', password = 'admin')
            # connectDb.connection.connection.set_isolation_level( e.ISOLATION_LEVEL_AUTOCOMMIT)
            cur = connectDb.cursor()
            # cursor = connectDb.cursor()
            print ("Opened database successfully")
            createTblStr1 = ''' CREATE TABLE dailyReport ( 
                            reportID    char(10) CONSTRAINT reportKey PRIMARY KEY, 
                            title       varchar(40) NOT NULL, 
                            dailyWeight float NOT NULL,
                            rptDte      date,
                            dailymiles  float NOT NULL,
                            supervisor  varchar(50)
                        ); '''
            createTblStr2 = ''' CREATE TABLE garbageTruck ( 
                            vehicleNum    char(6)  CONSTRAINT vehiclekey PRIMARY KEY (vehiclenum, reportid, routenum), 
                            reportID   char(10) references dailyReport(reportID),
                            vehicleWeight float  NOT NULL,
                            routeNum       varchar(10),
                            milesDriven    float  NOT NULL
                            
                            
                            
                           
CREATE TABLE garbagetruck
(
  vehiclenum character(6) NOT NULL,
  reportid character(10),
  vehicleweight double precision NOT NULL,
  routenum character varying(10),
  milesdriven double precision NOT NULL,
  CONSTRAINT vehiclekey PRIMARY KEY (vehiclenum, reportid),
  CONSTRAINT garbagetruck_reportid_fkey FOREIGN KEY (reportid)
      REFERENCES dailyreport (reportid) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE garbagetruck
  OWNER TO postgres;
                        ); '''
            # cursor.execute(createDBStr0) 
            # cursor.close()
            #connectDb.commit()
            #connectDb.close()
            #             cur.execute('show databases')
            #prettyPrint(cursor.fetchall())
   
            ## switch to using the newly-created database
            #cur.execute('use GarbageRecyler')
            cur.execute(createTblStr1)
            cur.execute(createTblStr2)         
            cur.close()
            connectDb.commit()
            print (' hhhhh' )   
            
            # cur.execute('Select pg_reload_conf()')  #this reloads the database with the new config to allow remote users set on June 7th, 2014
            # cur.execute('SELECT * from actor where actor_id = 1') 
           
        except psycopg2.DatabaseError as e:
            print ('Error %s' % e )   
            sys.exit(1)
            
            
        finally:
            
            if con:
                con.close()
                
        
    
if __name__ == '__main__':
    createdb = CreateDB('GarbageRecyler')  # creates the database
    createdb.connectDB()   # creates two table; garbagetruck and dailyreport
