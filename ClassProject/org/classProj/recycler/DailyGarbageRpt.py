'''
Created on Jun 25, 2014

@author: Andy
'''

class DailyGarbageRpt(object):
    '''
    classdocs
    '''


    def __init__(self, supervisor, dateCollected,  totalMiles, totalCollect, garbageTruckLst):
        '''
        Constructor
        '''
        self.supervisor = supervisor
        self.dateCollected = dateCollected
        self.totalCollect = totalCollect
        self.totalMiles = totalMiles
        self.garbageTruckLst = garbageTruckLst
        
        

    def __str__(self):
        '''
         The stringified version of Garbage truck
        '''
        return 'DailyGarbageRpt supervisorName, dateGrbgeCollected, totGrbgeCollected and garbageTruckLst are respectively(%s %s %f, %s)' % \
                   (self.supervisorName, self.dateCollected, self.totalCollect,
                        self.garbageTruckLst)