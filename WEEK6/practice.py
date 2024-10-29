# firstcharcap
str='heloo'
firstchar=str[0].upper()
print(firstchar)
print(firstchar+str[1:])
#longest valued key
dict1={'name':'asha','place':'nedumangad'}
longest_value=None
longest_value_length=0
for key,value in dict1.items():
    if(len(value))>longest_value_length:
        longest_value=value

print(longest_value)
class Parent:
    def __init__(self,name):
        self.name=name
    def say_hello(self):
        print(f"I am {self.name}")
class Child(Parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    def say_hello(self):
        super().say_hello()
        print(f"I am {self.age} years old")

c1=Child('Alice',22)
c1.say_hello()



