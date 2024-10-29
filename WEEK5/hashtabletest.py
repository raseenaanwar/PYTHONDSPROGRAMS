# class HashClass:
#     def __init__(self):
#         self.max=100
#         self.arr=[None for i in range(self.max)]
#     def get_hash(self,key):
#         h=0
#         for char in key:
#             h+=ord(char)
#
#         return h%self.max
#     # def add_val(self,key,val):
#     def __setitem__(self, key, val):
#         h=self.get_hash(key)
#         self.arr[h]=val
#     # def get_val(self,key):
#     def __getitem__(self, key):
#         h=self.get_hash(key)
#         return self.arr[h]
#     def __delitem__(self, key):
#         h=self.get_hash(key)
#         self.arr[h]=None
# t=HashClass()
# # print(t.get_hash('march'))
# t['march 6']=110
# t['march 10']=200
# t['may 16']=10
# t['dec 9']=190
#
# print(t.arr)
# del t['march 6']
# print(t.arr)
# collision handling
# seperate chaning
class HashTable:
    def __init__(self):
        self.max=10
        self.arr=[[] for i in range(self.max)]
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h
    def __setitem__(self, key, value):
        h=self.get_hash(key)
        found=False
        for index,elmnt in enumerate(self.arr[h]):
            if len(elmnt)==2 and elmnt[0]==key:
                self.arr[h][index]=(key,value)
                found=True
                break
            if not found:
                self.arr[h].append((key,value))
    def __getitem__(self, key):
        h=self.get_hash(key)
        for elmnt in self.arr[h]:
            if elmnt[0]==key:
                return elmnt[1]

t=HashTable()
t['march 6']=120
t['may 6']=100
t['march 6']=190
t['jun 8']=1
t['aug 9']=1000
print(t['may 6'])
