#Count the number of vowels in a string.
input_string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in input_string:
    if char in vowels:
        count += 1
print("Number of vowels:", count)   

