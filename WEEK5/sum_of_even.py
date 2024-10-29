# # # # def isEven(n):
# # # #     if n%2==0:
# # # #         return True
# # # #     else:
# # # #         return True
# # # #
# # # # size=int(input("Enter size of the array"))
# # # # list1=[int(input("Enter the numbers")) for i in range(size)]
# # # # s=0
# # # # for i in list1:
# # # #     if(isEven(i)):
# # # #         s+=i
# # # # print(f"Sum of even numbers in the array is {s}")
# # #
# # # def my_function(*kids):
# # #     print(kids[1])
# # # my_function("reyha",'arwa')
# # # fruit_list=['apple','orange','banana']
# # # for i in range(len(fruit_list)):
# # #     print(i,fruit_list[i])
# # #
# # # for pos,fruit in enumerate(fruit_list,1):
# # #     print(pos,fruit)
# # # list1=[1,2,3,4,5]
# # # square_list=[i**2 for i in list1]
# # # print(square_list)
# # # even_list=[i for i in list1 if i%2==0]
# # # print(even_list)
# # # x=lambda a,b:a*b
# # # print(x(6,5))
# # #
# # # x=lambda a,b,c:a+b+c
# # # print(x(1,2,3))
# # #
# # # def upper_decor(fun):
# # #     def wrapper(name):
# # #         r=fun(name)
# # #         return r.upper()
# # #     return wrapper
# # # @upper_decor
# # # def hello(name):
# # #     return "hello"+name
# # # print(hello('asha'))
# # str1="hepqr"
# # dict1={}
# # for char in str1:
# #     keys=dict1.keys()
# #     if char in keys:
# #         dict1[char]+=1
# #     else:
# #         dict1[char]=1
# #
# # print(dict1)
# # print(str1[:2]+str1[-2:])
# # def rev(str1):
# #     if len(str1)==1:
# #         return str1
# #     else:
# #         return rev(str1[1:])+str1[0]
# # print(rev("hello"))
# mark=float(input("Enter ur mark"))
# status=lambda mark:"passed" if mark>50 else "failed"
# print(status(mark))
def sqr(n):
    for i in range(1,n):
        yield i*i

a=sqr(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
