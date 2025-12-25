# Input string
input_string = input("Enter a string: ")

# Initialize an empty string to store result
result = ""

# Loop through each character in the input string
for char in input_string:
    if char not in result:
        result += char
        
# Display the result
print("String after removing duplicates:")
print(result)