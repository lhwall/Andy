'''
Created on Jun 24, 2014

@author: andwalke
'''
import org.classProj.recycler.DailyGarbageRpt
from org.classProj.recycler.GarbageTruck import  GarbageTruck



from mmap import mmap,ACCESS_READ
from xlrd import open_workbook
# from xlrd import close_workbook

import datetime


def readFile(fileName):
    '''
    reads the input Excel file
    '''
    try:
        garbageTruckLst = []
        dailyRptLst = []
        currRow = 1
        row = 0
        wb = open_workbook(fileName)
        
        for s in wb.sheets():
            print ('Sheet:', s.name)
            while row < s.nrows:
                currRow = 2  # reset currRow
                colCount = 0
                col = 0   
                if ((s.cell(row, 0).value).strip()) == "Supervisor:":
                    supervisor = s.cell(row, 1).value
                    garbageTruckLst = []  # reset the garbage truck list for each new supervisor
                    while  row < (s.nrows - 1) and ((s.cell(row + 1, 0).value).strip()) == "Daily Date:" and validDateStr(s.cell(row + 1, 1).value):
                      
                        # go to the line below and get data from the next four columns
                        dateCollected = s.cell(row + 1, 1).value
                        colCount += 1
                        rtNum = s.cell(row + currRow, col +  colCount  ).value
                        colCount += 1
                        vehicleNum = s.cell(row + currRow, col + colCount  ).value
                        colCount += 1
                        milez = (s.cell(row + currRow, col + colCount  ).value)
                        if milez:
                            miles = float(milez)
                        else:
                            miles = float("nan")
                        colCount += 1
                       
                        totalGarbage = s.cell(row + currRow, col + colCount ).value
                        if totalGarbage:
                            totalGarbageWt = float(totalGarbage)
                        else:
                            totalGarbageWt = float('nan')
                        currRow += 1
                        # col = 0
                        if rtNum == "" and vehicleNum == "" :
                            
                            print ('for supervisor %s the total miles is %f and total garbage weight is %f ' % (supervisor, miles, totalGarbageWt))
                            # subtotals for the whole week
                            dailyRpt = org.classProj.recycler.DailyGarbageRpt.DailyGarbageRpt(supervisor, dateCollected, miles, totalGarbageWt, garbageTruckLst)
                            dailyRptLst.append(dailyRpt)
                            col = 0
                            colCount = 0
                            row += currRow  # skip a row then we need to look for another daily date
                            currRow = 2 # set currRow to one as it is immediately under the Daily date 
                            print('the size of the dailyslist is %d' % len(garbageTruckLst))
                            garbageTruckLst = []  # reset the garbage truck list at the end of each daily list
                            continue
                        else:
                            # populate the Garbage truck object
                            garbageTruck = GarbageTruck(rtNum, vehicleNum, miles, totalGarbageWt)
                            garbageTruckLst.append(garbageTruck)
                            col = 0
                            colCount = 0
                       
                    print ('the last row to print is %d ' % row)    
                    row += currRow 
                else:
                    row += 1
                    continue     
                    
               
                print ('the size of the dailyRpt list is %d' % len(dailyRptLst)) 
        inputFileDict = {"GarbageTruckCollection": garbageTruckLst, "DailyRptCollection" : dailyRptLst}     
        return inputFileDict 
    except(FileNotFoundError,  Exception) as ex:
        print("there is a problem here %s " % ex)
        
    finally:
        print('we should close resources including the workbook')
        




# should log and keep track of missed records or bad records
def validDate(y, m, d):
    Result = True
    try:
        d = datetime.date(int(y), int(m), int(d))
    except ValueError as e:
        Result = False
        print("there has been an exception in validDate %s " % e)
    return Result
       
        
def validDateStr(str):
    Result = True
    # first trim all whitespace at the ends of the string
    # "03/03/2003"
    try:
        trimStr = str.strip()
        m = trimStr[0:2]  
        d = trimStr[3:5]
        y = trimStr[6:10]
        validDate = datetime.date(int(y), int(m), int(d))
    except (ValueError, Exception) as e:
        Result = False
        print("there has been an exception in validDateStr %s" % e)
    return Result    
        
        
if __name__ == '__main__':
    fileDict  = readFile('C:\\Users\\andy\\Downloads\\CityofAustin-AustinResourceRecovery_GarbageDailyReport_March2014.xls')