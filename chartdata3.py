
import csv


def ReadInData(Datafile):
    ServerName =[]
    StartDate =[]
    EndDate =[]
    NewLine =[]
    with open(Datafile) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            ServerName.append(row[0])
            StartDate.append(row[2])                
            EndDate.append(row[3])
            NewLine.append(row[0],row[2],row[3])
    return ServerName, StartDate, EndDate,NewLine

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
    
def CreateList(ListOfServers):
    DataList =[]
    RowElement = [0]*291    # 288 five minutes with 290 the servername and 289 being the day of the month
    for i, ServerNam in enumerate(ListOfServers):
        for d in range(1,32):
            RowElement[289] = d
            RowElement[290] = ServerNam
            DataList.append(RowElement[:])
    return DataList


RawDataFile= 'C:/Users/a-paul.carter/OneDrive - Surrey County Council/Python/2HighWaits.csv'

ServerName,StartDate,EndDate,RowData = ReadInData(RawDataFile)
# delete the header row from the import file.
ServerName.pop(0)
StartDate.pop(0)
EndDate.pop(0)

ListOfServers = set(ServerName)
CountOfServers =len(ListOfServers)


StartDay=[]
EndDay=[]
StartTime=[]
EndTime=[]



StartDay,StartTime = DayAndTime(StartDate)
EndDay,EndTime = DayAndTime(EndDate)

print(StartDay,StartTime,EndDay,EndTime)

StartTimeOfDay = TimeInfiveMintues(StartTime)
EndTimeOfDay = TimeInfiveMintues(EndTime)

#print(AlertData)


DataMatrix = CreateList(ListOfServers)

for row in DataMatrix:
    if row[-1] == 'SEC-SQL-20.SurreyCC.local':
        if row[-2] == 31:
            print(row)
