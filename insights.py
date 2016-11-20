import pagode as pd

cols =['weekday','day','time','sender','msg']
df = pd.read_csv('data/messages.txt', 
              columns=cols, sep='|')
print("Data Loaded.")              
print("columns:")
print(df.columns)
print("----")
print("Number of messages:", len(df))

print("Analysis period:", str(df.day[0]) +" ~ "+ str(df.day[-1]) )
