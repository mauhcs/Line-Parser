import codecs

class Series(object):
    
    def __init__(self, values=[], name=None):
        self.name = name
        self.values = values

    def append(self,value):
        self.values.append(value)
        
    def unique(self):
        return set(self.list)
    
    def __len__(self):
        return len(self.values)
         
class DataFrame(object):
    
    def __init__(self):
        self.columns = []
        self.data = {}
        
    def __getitem__(self, name):
        """Get items with [ and ]
        """
        return self.data[name]
        
    def __getattr__( self, name):
        """Get Atributes with . 
        example df.column1
        """
        for col in self.columns:
            if col == name:
                return self.data[col]
        print('No column',name)
        return []

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
    




