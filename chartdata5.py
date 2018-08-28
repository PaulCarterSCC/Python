
import csv


def ReadInData(Datafile):
    ServerNameList =[]
    #StartDate =[]
    #EndDate =[]
    NewLine =[]
    with open(Datafile) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            ServerName = row[0]
            ServerNameList.append(ServerName)
            StartDate = (row[2])                           # take the start date and time values
            EndDate=(row[3])                             #Take the End date and time values 
            NewLine.append(ServerName+' '+StartDate+' '+EndDate)   #Make one row to return
            #print(ServerName,StartDate,EndDate)

    return ServerNameList,NewLine

def ConvertData(RawData):
    StartDay = ''
    NewLine =[]
    for row in RowData:
            Line =row.split()
            ServerName  = Line[0]
            StartDate   = Line[1]                            # take the start date and time values
            StartTime   = TimeInfiveMintues(Line[2])
            EndDate     = Line[3]                              #Take the End date and time values 
            EndTime     = TimeInfiveMintues(Line[4])
            #print(Line[1],Line[2],Line[0])
            StartDay    = StartDate[0:2]
            EndDay     = EndDate[0:2]          #Split the date and time into Day of month and Time of Day
            NewLine.append(StartDay +' '+ StartTime +' '+ EndTime +' '+ EndDay +' '+ServerName )
    return NewLine





def DayAndTime(TimeStamp):
    #DayValue =[]
    #TimeValue =[]
    DayValue  = TimeStamp[0:2]  #First vales of the string are the day of the month
    TimeValue = TimeStamp[11:16]    #This is the Time String of the TimeStamp
    #TimeValue = TimeInfiveMintues(TimeValue) #Convert to a number between 0-288    
    return DayValue,TimeValue

def TimeInfiveMintues(HoursMinutes):
    FiveMinutesHours = 0
    FiveMinutes = 0
    Total = ''
    #for i, RowValue in enumerate(HoursMinutes):
    FiveMinutesHours = int(HoursMinutes[0:2])*12 # there are 12 five minutes in an hours
    FiveMinutes = int(HoursMinutes[3:5])//5 # how many whole 5 minutes in number
       # FiveMinutesInDay.append(FiveMinutesHours+FiveMinutes)  # Add both numbers together to get the total number of 5 minutes
       # print(FiveMinutes,RowValue[3:5],FiveMinutesHours,FiveMinutesInDay)
    Total  = str(FiveMinutesHours+FiveMinutes)# Add both numbers together to get the total number of 5 minutes
    return  Total

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

def DataDump(Data,TheFile): 
    Process = open(TheFile, 'w')
    for item in Data:
      Process.write("%s\n" % item)
    Process.close()


RawDataFile= 'C:/Users/a-paul.carter/OneDrive - Surrey County Council/Python/2HighWaitsSept.csv'# when coding at work
TheOutPutFile ='C:/Users/a-paul.carter/OneDrive - Surrey County Council/Python/2HighWaitsSept.txt'
#RawDataFile= '/Users/pcarter/Documents/python/2HighWaits.csv' # when coding at home
#TheOutPutFile ='/Users/pcarter/Documents/python/2HighWaitsSept.txt'

ServerName,RowData = ReadInData(RawDataFile)

# delete the header row from the import file. This is to insure that some of the row items can integrars
ServerName.pop(0)
RowData.pop(0)
#print(RowData)
RawData = ConvertData(RowData)

sorted(RawData, key=lambda x: (x[4], x[0]))
 
for row in RawData:
    print(row)


ListOfServers = set(ServerName)
CountOfServers =len(ListOfServers)



DataMatrix = CreateList(ListOfServers)

print(DataMatrix)

for InRow in RawData:
    Line =InRow.split()
    for Mrow in DataMatrix:
        #print(int(Line[0]),'--',Mrow[-2],'--',type(Line[0]),type(Mrow[-2]))
        if Mrow[-1] == Line[-1] and Mrow[-2] == int(Line[0]):
            FromNum = int(Line[1])
            ToNum   = int(Line[2])
            for i in range(FromNum,ToNum):
                Mrow[i] = 1
                

DataDump(DataMatrix,TheOutPutFile)
print('Job Done')