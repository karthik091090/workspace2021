## 3. Write a Python program to count the occurrences of each character in a given string. 

# Input string
input_string = input("Enter a string: ")
input_string = input_string.replace(" ", "")  # Remove spaces for counting
input_string = input_string.lower()  # Convert to lowercase


# Dictionary to store character counts
char_count_dict = {}
print(f"'char_count_dict':{char_count_dict}")

# Loop through each character in the string
for char in input_string:
    print(char)
    if char in char_count_dict:
        # char_count[char] += 1
        char_count_dict[char] = char_count_dict[char]+ 1
    else:
        char_count_dict[char] = 1


print(char_count_dict)
# Display the results
print("Character frequencies:")
for char in char_count_dict:
    print(f"'{char}': {char_count_dict[char]}")
