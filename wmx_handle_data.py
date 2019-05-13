#INPUT THE FILE NAME AND READ IT
#RETURN DICT WITH ROW KEY AND LINE VALUE 
def txt_records(fileName):
   fin=open(fileName)
   temList=[]
   for line in fin:
      lineList=line.split()
      temList.append(lineList)
   dataDict=records_fields(temList)
   fin.close()
   return dataDict
#INPUT TO LIST
#RETURN DICT WITH ROW KEY AND LINE VALUE 
def records_fields(aList):
   dataDict={}
   fieldsNum=len(aList[0])
   for i in range(fieldsNum):
      dataDict[aList[0][i]]=[float(record[i]) for record in aList[1:]]
   return dataDict 
if __name__=='__main__':
   resData=records_fields('test.txt')



