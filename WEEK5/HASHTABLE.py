class HashTable:
    def __init__(self):
        self.max=10
        self.arr=[[] for i in range(self.max)]

    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.max

    def __setitem__(self, key, value):
        h=self.get_hash(key)
        found=False
        for index,element  in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][index]=(key,value)
                found=True
                break
        if not found:
            self.arr[h].append((key,value))





    def __getitem__(self, item):
        h=self.get_hash(item)
        return self.arr[h]

    def __delitem__(self, key):
        h=self.get_hash(key)
        self.arr[h]=None

h1=HashTable()
h1['march 6']=130
h1['march 1']=20
h1["march 8"]=111
h1["march 17"]=459
print(h1["march 6"])
print(h1.arr)
print(h1['march 8'])
