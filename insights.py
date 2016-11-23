import pagode as pd

import datetime
import numpy as np
import matplotlib.pyplot as plt

cols =['weekday','day','time','sender','msg']
df = pd.read_csv('data/messages.txt', 
              columns=cols, sep='|')
print("Data Loaded.")              
#print("columns:")
#print(df.columns)
print("----")
print("Total Number of messages:", len(df))

print("Analysis period:", str(df.day[0]) +" ~ "+ str(df.day[-1]) )

print("Participants: ")
friends = df.sender.unique()
print(str(friends)[1:-1])

msgN = []
for f in friends:
    msgN.append([f,len(df[df.sender == f])])

msgN.sort(key=lambda x:x[1], reverse=True)

#### Message Percentage Plot
# Data to plot
labels = [m[0] for m in msgN]
sizes = [m[1] for m in msgN]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice
 
# Plot
print("Porcentagem de Mensagens")
plt.pie(sizes, explode=explode, 
        labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True,
        startangle=140)
 
plt.axis('equal')
plt.show()
plt.clf()

def plotMsgPerHour(df, title="Number of Messages per Hour of the day."):
    hours = np.array([int(x.split(':')[0]) for x in df.time.values])
    
    unique, counts = np.unique(hours, True)
    
    plt.plot(unique,counts, 'ko')
    plt.xlim([0,23])
    plt.ylim([1,1200])
    #plt.yscale("log")
    plt.title(title)
    plt.xlabel("Time of the day (JST UTC+9)")
    plt.ylabel("Number of Messages")
    plt.show()
    plt.clf()
    
plotMsgPerHour(df)


for day in df.sender.unique():
    plotMsgPerHour(df[df.sender == day], day)


def getMsgPerMonth(df,month='01'):
    
    temp = [z for z in map(lambda x: x.split('/')[0] == month, df.day.values)]
    
    return df[temp]

Ms = ['12','01','02','03','04','05',
      '06','07','08','09','10','11']
months = [len(getMsgPerMonth(df, m)) 
          for m in Ms ]
          
plt.plot(Ms, months, 'o')
plt.xlim(xmin=0,xmax=12)
plt.title('Number of Messages per Month')
plt.show()
plt.clf()

#Word Processing:
    
print(df.msg.mostCommon(10))
print('___')

print(df.msg.howMany('Rita',False,False))
print("-")
print(df.msg.howMany('Rita'))

"""
#The text should be obly between 0 and 1.
plt.text(0.5,0.5,"Rita \nKaori")
plt.axis('off')
plt.show()
plt.clf()
"""
