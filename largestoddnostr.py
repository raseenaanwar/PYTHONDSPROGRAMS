def odd(i):
    if i%2==1:
        return True
    else:
        return False
def largeOddStr(s):
    no_set=set()
    for char in s:
        if char.isdigit():
            no_set.add(int(char))
    largest_odd=0
    for i in no_set:
        if(odd(i)):
            if i>largest_odd:
                largest_odd=i
    if largest_odd!=0:
        print("largets Odd",largest_odd)
str="gfgdfy7674654829"
largeOddStr(str)
