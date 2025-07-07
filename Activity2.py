import random
import time
def getRandomDate(startDate, endDate ) :
    print ("Printing Random Date Between ",startDate," And ",endDate )
    randomGenerator= random.random()
    dateFormat="%m/%d/%Y"
    startTime=time.mktime(time.strptime(startDate,dateFormat))
    endTime=time.mktime(time.strptime(endDate,dateFormat))
    randomTime=startTime+randomGenerator*(endTime-startTime)
    randomDate=time.strftime(dateFormat,time.localtime(randomTime))
    return randomDate
print("randomDate= ",getRandomDate("1/1/2024","7/7/2025"))

   
