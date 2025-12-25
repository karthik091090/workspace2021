input_string = input("Enter a string: ")

len=len(input_string)
reversed_string=""

while len>0:
    reversed_string=reversed_string + input_string[len-1]
    len=len-1
print("Reversed string:",reversed_string)


# Another method to reverse a string using slicing
test_string = "Hello, World!"
print("reversed string:", test_string[::-1])


input_number = 345
reversed_number = 0
while input_number > 0:
    digit = input_number % 10
    print("digit:", digit)
    reversed_number = reversed_number * 10 + digit
    input_number //= 10
print("Reversed number:", reversed_number)

#reverse number using string slicing
input_number = 12345
reversed_number = str(input_number)[::-1]
print("Reversed number using string slicing:", reversed_number)