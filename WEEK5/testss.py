# # x=[i for i in range(5)]
# # print(x)
# #
# # x={i : i+2 for i in range(5)}
# # print(x)
# # a=lambda x,y:x+y
# # print(a(4,3))
# # nums=[2,1,4,2,5,3,2,4]
# # dict1=dict()
# # for i in range(len(nums)):
# #     if nums[i]%2==0 and nums[i] not in dict1:
# #         dict1[nums[i]]=1
# #     elif nums[i]%2==0 and nums[i] in dict1:
# #         dict1[nums[i]]+=1
# # if not dict1:
# #     print(-1)
# # print(nums)
# # print(dict1)
# # max_value = max(dict1.values())
# # count_max_value = sum(1 for value in dict1.values() if value == max_value)
# # # print(count_max_value)
# # if count_max_value > 1:
# #     print (min(dict1.keys()))
# # else:
# #     print (max(dict1, key=dict1.get))
#
# # SECOND LARGETS
# # nums=[1,2,5,0,8,6,5]
# # largest=max(nums)
# # sec_largest=nums[0]
# # for i in range(len(nums)):
# #     if nums[i]>sec_largest and nums[i]<largest:
# #         sec_largest=nums[i]
# # print(sec_largest)
# # n=7
# # f=0
# # for i in range(2,n):
# #     if n%i==0:
# #         f=1
# # if f==0:
# #     print("Prime")
# # else:
# #     print("Not")
# #
# # def is_prime(n):
# #
# #     if n<=1:
# #         return False
# #     for i in range(2,(n//2)+1):
# #         if n%i==0:
# #             return False
# #
# #     return True
# #
# # nums=[1,2,3,4,5,6,7,78]
# # i=0
# # while i<len(nums):
# #     if is_prime(nums[i]):
# #         nums.pop(i)
# #     else:
# #         i+=1
# # print(nums)
# # 1
# # 1 2
# # 1 2 3
# # 1 2 3 4
# # for i in range(1,5):
# #     for j in range(1,i):
# #         print(j,end=" ")
# #     print(end='\n')
# # for i in range(5,1,-1):
# #     for j in range(1,i):
# #         print(j,end=" ")
# #     print(end="\n")
# # for i in range(5):
# #     print(" ")
# # def reversestr(text,result=""):
# #     if text=="":
# #         return result
# #     result+=text[-1]
# #     print(text[:-1])
# #     return reversestr(text[:-1],result)
# # print(reversestr("hello"))
# def flatten(arr):
#     result = []
#     while arr:
#         sub_list = arr.pop(0)
#         print("sublist",sub_list)
#         if isinstance(sub_list, list):
#             print("inside insatnce")
#             arr = sub_list + arr
#             print("arr:",arr)
#         else:
#             result.append(sub_list)
#     return result
#
# # Test the function
# nested_array = [[1, 23, [1, 2], [1]], [2, 3, 1], [1, 2]]
# flattened_array = flatten(nested_array)
# print(flattened_array)
# import copy
# list1=[1,2,3,[4,5]]
# list2=copy.copy(list1)
# print("lsit2 id",id(list2))
# print("lsit2 id",id(list1))
# list2[0]=99
# print(list2)
# print(list1)
# old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
# new_list = old_list
#
# new_list[2][2] = 9
#
# print('Old List:', old_list)
# print('ID of Old List:', id(old_list))
#
# print('New List:', new_list)
# print('ID of New List:', id(new_list))
# old_list[0][0]=100
# print('Old List:', old_list)
# print('ID of Old List:', id(old_list))
#
# print('New List:', new_list)
# print('ID of New List:', id(new_list))
# import os
# print(os.environ)
# import  random
# def gen_otp():
#     otp=random.randint(100000,999999)
#     return otp
# print(gen_otp())
# print(gen_otp())
# from datetime import datetime
# t=datetime.now().time()
# print(t)
# n=6
# for i in range(2,int(n**.5)+1):
#     if n%i==0:
#         print("not")
#         break
# else:
#     print("prime")
# n = 7
# for i in range(2, int(n**0.5) + 1):
#     if n % i == 0:
#         print("not")
#         break
# else:
#     print("prime")
# k=2
# a=[2,1,3,6,0,9]
# a.sort(reverse=True)
# for i in range(k):
#     print(a[i])

# from collections import Counter
# nums =[3,0,1,0]
# k=1
# dict1 = {}
# for num in nums:
#     if num in dict1:
#         dict1[num] += 1
#     else:
#         dict1[num] = 1
#
# print(dict1)
# sorted_d = dict(sorted(dict1.items()))
# print(sorted_d)
# sorted_d1 = dict(sorted(dict1.items(),key=lambda  item:item[1]))
# print(sorted_d1)
# ans = []
# for key, value in dict1.items():
#     if value >= k:
#         ans.append(key)
#
#         # If k is greater than or equal to the number of unique elements, return all unique elements
# if k >= len(set(nums)):
#     print(list(set(nums)))
#
# print(ans)
# dic3={}
# dic1={1:1,2:2}
# dic2={3:1,1:4,8:7}
# nums=[1,1,1,2,2,3]
# count=Counter(nums)
# k=2
# print(count)
# # Step 2: Sort the elements by frequency
# sorted_elements = sorted(count, key=count.get, reverse=True)
#
#     # Step 3: Return the top K elements
# print(sorted_elements[:k])
# for d in (dic1,dic2):
#     dic3.update(d)
# print(dic3)
# dict1={x:x*x for x in range(5)}
# print(dict1)
# from collections import Counter
# dict1={x:x**2 for x in range(1,16)}
# print(dict1)
# if 1 in dict1:
#     del dict1[1]
# print(dict1)
# keymax=min(dict1.values() )
# print(keymax)
# print(Counter(dict1))
# highest_three = sorted(dict1.items(), key=lambda item: item[1], reverse=True)[:3]
#
# # highest_three = sorted(dict1.items(),reverse=True)[:3]
# print(highest_three)
list1=[1,2,34,4,3]
sum1=5
# low=0
# flag=False
# high=len(list1)-1
# while low<high:
#     s=list1[low]+list1[high]
#     print(s)
#     if s==sum1:
#         print("found",list1[low],list1[high])
#         break
#     elif s>sum1:
#         low+=1
#     else:
# #         high-=1
# nums=[1,8,2,7,4,6]
# sum1=10
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]+nums[j]==sum1:
#             print(i,j)
#             break
# print("not")
# nums=[[1,2,3],[4,5,6],[5,62,1]]
# outerlist=[]
# innerlist=[]
# for i in range(len(nums)-1,-1,-1):
#     outerlist.append(nums[i])
#     innerlist.append(nums[i][::-1])
# print(outerlist)
# print(innerlist)
# strs = ["eat","tea","tan","ate","nat","bat"]
# anagram_map={}
# r=[]
# for s in strs:
#     s1=tuple(sorted(s))
#     print(s,":",s1)
#     if s1 not in anagram_map:
#         anagram_map[s1]=[]
#     anagram_map[s1].append(s)
# print(anagram_map)
# for value in anagram_map.values():
#     r.append(value)
# print(r)
class HashClass:
    def __init__(self):
        self.max=100
        self.arr=[None for i in range(self.max)]
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)

        return h%self.max
    # def add_val(self,key,val):
    def __setitem__(self, key, val):
        h=self.get_hash(key)
        self.arr[h]=val
    # def get_val(self,key):
    def __getitem__(self, key):
        h=self.get_hash(key)
        return self.arr[h]
    def __delitem__(self, key):
        h=self.get_hash(key)
        self.arr[h]=None
t=HashClass()
# print(t.get_hash('march'))
t['march 6']=110
t['march 10']=200
t['may 16']=10
t['dec 9']=190

print(t.arr)
del t['march 6']
print(t.arr)
