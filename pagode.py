import codecs
from itertools import compress

class Series(object):
    
    def __init__(self, values=None, name=None):
        self.name = name
        if values is None:
          self.values = []
        else:
          self.values = values

    def append(self,value):
        self.values.append(value)
        
    def unique(self):
        return set(self.list)
    
    def __len__(self):
        return len(self.values)
        
    def __eq__(self, value):
      return [v == value for v in self.values]
         
class DataFrame(object):
    
    def __init__(self, data=None, columns=None):
        #Define the colmns
        if columns is None:
          self.columns = []
        else:
          if isinstance(columns,list):
            self.columns = columns
          else:
            print("Columns type "+ type(columns)+" not recognized. Type must be list.")
        
        #Define the data
        self.data = {}
        if isinstance(data,list):
          
          #if columns were given
          if self.columns:
            i = 0
            for d in data:
              if not isinstance(d,list):
                print("error. Data must be a list of lists")
                return
                
              name = self.columns[i]
              self.data[name] = Series(d,name)
              i += 1
          
          #if no columns were given
          else:
            i = 0
            for d in data:
              if not isinstance(d,list):
                print("error. Data must be a list of lists")
                return
                
              self.columns.append(i)
              self.data[i] = Series(d,i)
              i += 1
        
    def __getitem__(self, name):
        """Get items with [ and ]
        """
        if isinstance(name, str):
          return self.data[name]
        elif isinstance(name, list):
          ind = list(compress(range(len(name)), name))
          temp = DataFrame([[self.data[c].values[i] 
                                for i in ind] 
                               for c in self.columns],
                               columns=self.columns)
          return temp
          
    def __getattr__( self, name):
        """Get Atributes with . 
        example df.column1
        """
        for col in self.columns:
            if col == name:
                return self.data[col]
        print('No column',name)
        return []
        
    def __len__(self):
      return len(self.data[self.columns[0]])

def read_csv(filePath, sep=',', header=None,
             encode='utf-8', columns=None):
    
    df = DataFrame()
    with codecs.open(filePath, 'r', encoding=encode) as f:
       
        def next():
            return f.readline().split(sep)
        
        if header:
            head = next()
            for h in head:
                df.columns.append(h)
                df.data[h] = Series(name=h)
        
        elif columns:
            for c in columns:    
                df.columns.append(c)
                df.data[c] = Series(name=c)
            
        else:
            first = next()
            c = 0
            for f in first:
                df.columns.append(str(c))
                df.data[str(c)] = f
                c+=1 

        for line in f:
            i=0
            for L in line.split(sep):
                name = df.columns[i]
                df.data[name].append(L)
                i+=1
    return df
    




