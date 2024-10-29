def most_used_character(string):
    char_counts = {}
    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    most_used_char = None
    max_count = 0
    for char, count in char_counts.items():
        if count > max_count:
            most_used_char = char
            max_count = count

    return most_used_char


string1 = "hello"
print(most_used_character(string1))

string2 = "abracadabra"
print(most_used_character(string2))
