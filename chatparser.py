import codecs
import re
import collections

from ignore import ignoredCharacters
# Tally occurrences of words in a list



class Printo(object):
    
    def __init__(self, F = 'raw_text.txt'):
        self.f = codecs.open('raw_text.txt',
                           encoding='utf-8')
        self.cnt = collections.Counter()
        self.ignored = ignoredCharacters()
   
    def hasTime(self, line):
        return re.match('^[0-9][0-9]:[0-9][0-9]',line)
        
    def __del__(self):
        self.f.close()
        print('endof object')

    def lineN(self, lineNumber=1):
        i = 1
        for line in self.f:
            if i == lineNumber:
                return line
            i += 1
        print()
        return ''
        
    def countWords(self):
        for line in self.f:
            for word in line.split('\t'):
                for w in word.split(' '):
                    if w not in self.ignored:
                        self.cnt[w] += 1
    
    def mostCommon(self,N=5):
        self.countWords()
        most = []
        for x in self.cnt.most_common(N):
            most.append(x)
        return most
    
    def newDay(self, line):
        day = "(Mon,|Tue,|Wed,|Thu,|Fri,|Sat,|Sun,)"
        words = line.split(' ')
        if re.match(day,words[0]):
             #print(line[:-1])
             week = (words[0][:-1])
             numberDay = words[1][:-1]
             return week,numberDay
        else: 
            return False
    
    def time(self, line):
        t = '^[0-9][0-9]:[0-9][0-9]'
        if re.match(t,line[:5]):
            return(line[:5])
        else:
            return False

    def author(self, line):
        try:
            Ts = line.split('\t')
            A = (Ts[1].split(' ')[0])
            return A
        except  IndexError:
            return False
    
    def msg(self, line):
        try:
            Ts = line.split('\t')
            M = Ts[2]
            return M.replace('\n','')
        except:
            M = Ts[0]
            if M == '\n':
                return False #print(M)
            else:
                return False
                #print('here')
                #return M
