'''
Created on Jun 25, 2014

@author: Andy
'''



class GarbageTruck(object):
    '''
    classdocs
    '''


    def __init__(self, rtNum, vehicleNum, miles, garbageWt):
        '''
        Garbage Truck Constructor
        '''
        
        self.rtNum = rtNum
        self.vehicleNum = vehicleNum
        self.miles = miles
        self.garbageWt = garbageWt
        
        # print('leaving Garbage truck consturctor')
        
if __name__ == '__main__':
    GarbageTruck('2', '33', 44.4, 444.55)
     
    def __str__(self):
        '''
         The stringified version of Garbage truck
        '''
        return 'GarbageTruck routeNum, vehicleNumb, milesDrive and garbageWeight are respectively(%s %s %f, %f)' % \
                    (self.routeNumb, self.vehicleNumb, self.milesDriven, self.garbageWeight) 
     
        