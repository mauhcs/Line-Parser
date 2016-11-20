import pagode as pd

cols =['weekday','day','time','sender','msg']
df = pd.read_csv('messages.txt', 
              columns=cols, sep='|')
                
#print(df)

#print('DATA')
#print(df.data)

print('COLUMNS')
print(df.columns)
print('getitem')
print(len(df['weekday']))
