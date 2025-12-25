# Find the most frequent character in a string.
input_string = input("Enter a string: ")
char_count = {} 
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1    

frequent_char = 0
print(char_count)

for item in char_count.keys():
    print(item)
    if char_count[item] > frequent_char:
        frequent_char = char_count[item]
        frequent_char_key = item

print(f"Most frequent character: '{frequent_char_key}' with count {frequent_char}")