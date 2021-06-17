import pandas as pd

def csv_generator(df):
    df.to_csv('database.csv')

def csv_creator():
    try:
        while True:
            for i in range(len(features)):
                details[features[i]].append(input())
    except KeyboardInterrupt:
        pass
    df=pd.DataFrame(details,columns=['Name','email_id','dob'])
    csv_generator(df)

def csv_editor():
    row_no=int(input("enter row: "))
    for i in range(len(features)):
        details[features[i]][row_no] = input()
    df=pd.DataFrame(details,columns=['Name','email_id','dob'])
    csv_generator(df)

def csv_row_deleter():
    df=pd.read_csv("database.csv")
    row_to_del=int(input("delete row: "))
    df.drop([row_to_del],axis=0,inplace=True)
    df=df.reset_index(drop=True)
    df=df.drop(["Unnamed: 0"],axis=1)
    csv_generator(df)

details={}
features=["Name","email_id","dob"]
for i in range(3):
    details[features[i]]=[]

#csv creator
df=csv_creator()
print("CSV created")

#csv editor
df=csv_editor()
print("File Edited")

#row deletion
csv_row_deleter()
print("Row Deleted")