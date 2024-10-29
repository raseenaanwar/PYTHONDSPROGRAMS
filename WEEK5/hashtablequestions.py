def has_repeated_characters(string):
    char_counts = {}
    for char in string:
        if char in char_counts:
            return True
        char_counts[char] = 1
    return False
string1 = "hello"
if(has_repeated_characters(string1)):
    print('HAS REPEATED CHARACATERS')
else:
    ("None")



