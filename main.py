import pandas as pd
import numpy as np
import re

data = pd.read_csv('Input_1.csv')         #importing the input file
dataHeaders = data.columns                #all headers of input data

headers = ["Name","Username","Chapter Tag","Test_Name","score","time-taken (seconds)","answered","correct","wrong","skipped"]


newDataHeaders = []                                #these lines will spilt the test_name and their parameters
for i in dataHeaders:
    temp = i.split("-",1)
    temp[0]=temp[0].strip()
    temp[-1]=temp[-1].strip()
    newDataHeaders.append(temp)


oData = pd.DataFrame([],columns=headers)        #creating an empty data frame for storing of output data


for i in data.index:
    tempData= {}                                 #dict for new row which will be added in the output after doing some operations
    for r in range(len(newDataHeaders)):         #for travering everyrow of the input data
        if headers[3] not in tempData:
                tempData[headers[3]]=[]          #if key is not presnt in the tempdata then add it
        if r<3:
            if headers[r] not in tempData:
                tempData[headers[r]]=[]
        else:
            if newDataHeaders[r][-1] not in tempData:
                tempData[newDataHeaders[r][-1]]=[]                                    
            
            if newDataHeaders[r][0] not in tempData[headers[3]]:
                tempData[headers[0]].append(data.iloc[i][0])
                tempData[headers[1]].append(data.iloc[i][1])
                tempData[headers[2]].append(data.iloc[i][2])
                tempData[headers[3]].append(newDataHeaders[r][0])
            tempData[newDataHeaders[r][-1]].append(data.iloc[i][r])

    tempData = pd.DataFrame(tempData)                                       #making dataframe of new data
    oData = pd.concat([oData, tempData], ignore_index = True)               #merging both oData and new data
    # oData.reset_index()

oData = oData[oData.score !="-"]                                    #removing unnecessary data

headers = ["Name","Username","Chapter Tag","Test_Name","answered","correct","score","skipped","time-taken (seconds)","wrong"]
oData = oData[headers]                                              #rearranging the columns

oData = oData.sort_values(by=['Name','Test_Name'], ascending=True)  #sorting the dataframe according to the name and test_name

# oData.reset_index(drop=True,inplace=True)                         #if you want indexing
# oData= oData.sort_values()

oData.to_csv('output.csv', index=False)                             #exporting into the csvfile