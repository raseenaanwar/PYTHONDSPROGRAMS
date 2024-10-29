

class Trie:
   def __init__(self):
      self.child = {}
   def insert(self, word):
      current = self.child
      for l in word:
         if l not in current:
            current[l] = {}
         current = current[l]
      current['*']=1
   def search(self, word):
      current = self.child
      for l in word:
         if l not in current:
            return False
         current = current[l]
      return '*' in current
   def startsWith(self, prefix):
      current = self.child
      for l in prefix:
         if l not in current:
            return False
         current = current[l]
      return True
ob1 = Trie()
ob1.insert("apple")
ob1.insert('apply')
ob1.insert('show')

ob1.insert('shower')
print(ob1.search("apple"))
print(ob1.search("app"))
print()
print('words starts with app',ob1.startsWith("app"))
print()
ob1.insert("app")
print(ob1.search("appbnnn"))
print(ob1.child)
