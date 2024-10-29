class HashTable:
    def __init__(self):
        self.MAX=10
        self.arr=[None for i in range(self.MAX)]
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
            return h % self.MAX

    def __setitem__(self, key, value):
        h=self.get_hash(key)
        self.arr[h]=value
        print(h)
        print(self.arr[h])

    def __getitem__(self, key):
        h=self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h=self.get_hash(key)
        self.arr[h]=None

h1=HashTable()
h1['march 6']=130
h1['june 31']=20
h1['march 8']=100
h1['march 17']=120

print(h1.arr)
