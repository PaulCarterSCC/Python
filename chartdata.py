
import csv

def ReadInData(Datafile):
    ServerName =[]
    StartDate =[]
    EndDate =[]
    with open(Datafile) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            ServerName.append(row[0])
            StartDate.append(row[2])                
            EndDate.append(row[3])
 
    return ServerName, StartDate, EndDate

def DayAndTime(TimeStamp):
    DayValue =[]
    TimeValue =[]
    for i,line in enumerate(TimeStamp):
        DayValue.append(line[0:2])
        TimeValue.append(line[11:16])
        
    return DayValue,TimeValue

def TimeInfiveMintues(HoursMinutes):
    FiveMinutesHours = 0
    FiveMinutes = 0
    FiveMinutesInDay =[]
    for i, RowValue in enumerate(HoursMinutes):
        FiveMinutesHours = int(RowValue[0:2])*12 # there are 12 five minutes in an hours
        FiveMinutes = int(RowValue[3:5])//5 # how many whole 5 minutes in number
        FiveMinutesInDay.append(FiveMinutesHours+FiveMinutes)  # Add both numbers together to get the total number of 5 minutes
       # print(FiveMinutes,RowValue[3:5],FiveMinutesHours,FiveMinutesInDay)
    return FiveMinutesInDay

def PopulateDay(StartPeriod,EndPeriod,TimeArray):
    NextDayTime =0
    if EndPeriod>288:  
        NextDayTime = EndPeriod -288
        EndPeriod = 288
    while StartPeriod <= EndPeriod:
        TimeArray[StartPeriod] =1
        StartPeriod +1
    return TimeArray
    

RawDataFile = '/Users/paulcarter/Documents/python/ExcelChart/DataFiles/2HighWaits.csv'

ServerName,StartDate,EndDate = ReadInData(RawDataFile)
# delete the header row from the import file.
ServerName.pop(0)
StartDate.pop(0)
EndDate.pop(0)

ListOfServer = set(ServerName)
#print(ListOfServer)
#print(ServerName)

#print(ServerName)
#print(StartDate)
#print(EndDate)
#Create list values for Start
StartDay=[]
EndDay=[]
StartTime=[]
EndTime=[]
FiveMinutePeriodsForday =[0]*288 # Creates an array of 289, 288 represents a 5 minutes in a day.
DayOfMonth=[FiveMinutePeriodsForday] *31
ListOfServers = set(ServerName)
AlertData =['ServerName',DayOfMonth] * len(ListOfServers)

StartDay,StartTime = DayAndTime(StartDate)
EndDay,EndTime = DayAndTime(EndDate)

#print(StartDay,StartTime,EndDay,EndTime)

StartTimeOfDay = TimeInfiveMintues(StartTime)
EndTimeOfDay = TimeInfiveMintues(EndTime)

#print(AlertData)


for i,Server in enumerate(ListOfServers):
    print(i,Server)
    AlertData[i,i,i] = Server  

print(AlertData)