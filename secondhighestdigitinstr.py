def secondHighest(s):
    no_set=set()
    for char in s:
        if char.isdigit():
            no_set.add(int(char))
    no_set=sorted(no_set,reverse=True)
    if len(no_set)>=2:
        print(no_set[1])
    else:
        print('not enough')
    print(no_set)

s="ah3295jha731"
secondHighest(s)
