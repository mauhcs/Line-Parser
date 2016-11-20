from chatparser import Printo

sep = '|'
P = Printo()
with open("data/messages.txt", 'a', encoding='utf-8') as f:
    
    today = None
    for line in P.f:
       #print(line.split('\t'))
       
       if P.newDay(line):
           today = (P.newDay(line))
           isMsg = False
           #print(today)
           
       
       if P.time(line):
           time = (P.time(line))
           
       if (P.author(line)):
           isMsg= True
           author = (P.author(line))
           
       if P.msg(line):
           msg = (P.msg(line))
           #print('here')
           
       #print(isMsg)
       if isMsg:
           m = (str(today[0])+sep+str(today[1])+sep+time+sep+author+sep+msg+'\n')
           try:
               f.write(m)
           except Exception as e:
               print('---')
               print(e)
               print(line)
           isMsg = False
       
 
        
    
#print(P.mostCommon(1000))
P = 0 # closes file due to __del__ method
