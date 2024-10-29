
class Trie(object):
    def __init__(self):
        self.child={}
    def insert(self,word):
        current=self.child
        for l in word:
            if not l in current:
                current[l]={}
                current=current[l]
            current['*']=1
    def search(self,word):
        current=self.child
        for l in word:
            if l not in current:
                return False
            current=current[l]
        return '* ' in current
    def startswith(self,prefix):
        current=self.child
        for l in prefix:
            if l not in current:
                return False
            current=current[l]
        return True

    def print(self):
        print(self.child)
ob1=Trie()
ob1.insert("app")
ob1.insert("append")
print(ob1.search('app'))
print(ob1.startswith('app'))
ob1.print()
