from pathlib import Path
import pandas as pd

datapath= Path(r'C:\Users\Sahar\Desktop\Git\Read_text_into_lists')
df = open(datapath / "Cancer_Dataset.txt","r")
#Read text file
l = df.readlines()
Rows_number = len(l)

list = []
for i in range (1, Rows_number):
    line = []
    line.append(l[i][0:8])
    line.append(l[i][8:12])
    line.append(l[i][12])
    line.append(l[i][13:15])
    line.append(l[i][15:20])
    line.append(l[i][20])

    list.append(line)

#Convert list to dataframe
columns = ['Date','Patient_ID', 'Sex', 'Age', 'Tumor_size', 'Benign_Cancer']
res = pd.DataFrame(list, columns=columns)

#Export dataframe as csv file
res.to_csv("Output_Cancer_Dataset.csv")
