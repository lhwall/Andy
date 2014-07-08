'''
Created on Jun 27, 2014

@author: Andy
'''

import psycopg2
import psycopg2 as dbapi2
import psycopg2.extensions as e
import sys

from org.classProj.recycler.ReadInputFile import readFile 

class InsertGarbageRpt(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        
    def insertData(self, inputDict):
        '''
        Inserts data into two tables
        after connecting to the database
        '''
        connectDb = dbapi2.connect(database = 'garbagerecyler', user = 'postgres', password = 'admin')
            # connectDb.connection.connection.set_isolation_level( e.ISOLATION_LEVEL_AUTOCOMMIT)
        cur = connectDb.cursor()
        id = 0
        self.inputDict =  inputDict
        dailyRptLst = inputDict['DailyRptCollection']
        garbageTruckLst = inputDict['GarbageTruckCollection']
        rowCount = 0
        for dailyRpt in dailyRptLst:
            print('now at row %d ' % id)
            idStr = str(id)
            insertDailyRptStr = 'Insert into dailyReport (reportid, title, dailyweight, rptdte, dailymiles, supervisor) VALUES (%s, %s, %s, %s, %s, %s)'
            print ('%s' % insertDailyRptStr)
            cur.execute(insertDailyRptStr, (idStr, 'titles', dailyRpt.totalCollect, dailyRpt.dateCollected.strip(), dailyRpt.totalMiles, dailyRpt.supervisor))
           
            #  if id == 3:
            #     break
            garbageTruckLsts = dailyRpt.garbageTruckLst
            for truck in garbageTruckLsts:
                insertGarbageTruckStr = "Insert into garbagetruck (vehicleNum, reportid, routenum, vehicleweight, milesdriven) \
                                    VALUES ('%s', '%s', '%s', '%f', '%f')" % (truck.vehicleNum.strip(), idStr, truck.rtNum, truck.garbageWt, truck.miles)
                                   
                cur.execute(insertGarbageTruckStr)
                # if rowCount == 15:
                #   break
            id += 1                               
                                            
                                            
        cur.close()
        connectDb.commit()
        connectDb.close()  
       

if __name__ == '__main__':
    fileDict  = readFile('C:\\Users\\andy\\Downloads\\CityofAustin-AustinResourceRecovery_GarbageDailyReport_March2014.xls')
    garbageRpt = InsertGarbageRpt()
    garbageRpt.insertData(fileDict)
    print('alll done')
    
    