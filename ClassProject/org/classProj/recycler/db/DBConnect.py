'''
Created on Jun 27, 2014

@author: Andy
'''

import psycopg2
import sys


class DBConnect:
    '''
    classdocs dd
    '''


    def __init__(self, params):
        '''
        Constructor
        '''



    def connectDB(self):
        con = None
        
        try:
             
            con = psycopg2.connect(database='dvdrental', user='postgres', password='admin') 
            cur = con.cursor()
            cur.execute('SELECT version()')          
            ver = cur.fetchone()
            print (ver )   
            
            cur.execute('Select pg_reload_conf()')  #this reloads the database with the new config to allow remote users set on June 7th, 2014
            # cur.execute('SELECT * from actor where actor_id = 1') 
            rowstr = cur.fetchone()
            print (rowstr)
        except psycopg2.DatabaseError as e:
            print ('Error %s' % e )   
            sys.exit(1)
            
            
        finally:
            
            if con:
                con.close()
    
    
if __name__ == '__main__':
    pass