# Check if a string is a palindrome.

input_string = input("Enter a string: ")
reversed_string = input_string[::-1]
if input_string == reversed_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")   
    