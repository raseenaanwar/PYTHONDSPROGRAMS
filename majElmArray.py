def maj(list1):
    count={}
    for number in list1:
        if number in count:
            count[number]+=1
        else:
            count[number]=1
    print(count)
    size=len(list1)
    for number,freq in count.items():
        if freq>size/2:
            print(f"{number} occurs at {freq}")

size=int(input("Enter the size"))
list1=[int(input()) for i in range(size)]
maj(list1)

