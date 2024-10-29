
s='hello'
substrings = []
n=len(s)
for start in range(n):
    for end in range(start + 1, n + 1):
        print(s[start:end])
        print(s[end:start])
        substring = s[start:end]
        if substring == substring[::-1]:
            substrings.append(s[start:end])
print(substrings)
