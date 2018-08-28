
ListOfServers =['PRI-SQL-21.SurreyCC.local'
                ,'SEC-SQL-20.SurreyCC.local'
                ,'PRI-SQL-01.SurreyCC.local']
             #   ,'PRI-SQL-09.SurreyCC.local'
              #  ,'PRI-SQL-24.SurreyCC.local'
               # ,'SEC-SQL-T-02.SurreyCC.local'
                #,'PRI-SQL-20.SurreyCC.local']
DataList =[]
RowElement = [0]*10    # 288 five minutes with 290 the servername and 289 being the day of the month

for i, ServerNam in enumerate(ListOfServers):
    for d in range(1,32):
        RowElement[9] = d
        RowElement[8] = ServerNam
        print(d,RowElement)
        DataList.append(RowElement[:])


for row in DataList:
    print(row)
#print(DataList)