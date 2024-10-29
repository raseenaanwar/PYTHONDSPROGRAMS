# chaining
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
        # self.arr[h]=value
        for index ,elment in enumerate(self.arr[h]):
            self.arr[h].append(key,value)

    def __getitem__(self, item):
        h=self.get_hash(item)
        return self.arr[h]
    def __delitem__(self, key):
        h=self.get_hash(key)
        self.arr[h]=None

h1=HashTable()
h1['march 6']=130
h1['march 17']=459
print(h1.arr)
print(h1['march 6'])
print(h1['hhhhh'])
# del h1['march 6']
print(h1.arr)
print(h1.get_hash('march 6'))
print(h1.get_hash('march 17'))
print(h1['march 6'])
