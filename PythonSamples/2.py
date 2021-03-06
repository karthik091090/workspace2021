# a=b=c=1
# print(a,b,c)

# a,b,c=1,10.5,'sdsad'
# print(a,b,c)
# print(type(a))
# print(type(b))
# print(type(c))

# ###############################################  String
# str = 'Hello World!'
# print(str)          # Prints complete string
# print(str[0])       # Prints first character of the string
# print(str[2:5])     # Prints characters starting from 3rd to 5th
# print(str[2:])      # Prints string starting from 3rd character
# print(str * 2)      # Prints string two times
# print(str + "TEST") # Prints concatenated string
# print(str[::3]) 

###############################################  List
# list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
# tinylist = [123, 'john']
# print(list)          # Prints complete list
# print(list[0])       # Prints first element of the list
# print(list[1:3])     # Prints elements starting from 2nd till 3rd 
# print(list[2:])      # Prints elements starting from 3rd element
# print(tinylist * 2)  # Prints list two times
# print(list + tinylist) # Prints concatenated lists

# ###############################################  tuple
# tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
# tinytuple = (123, 'john')
# print(tuple)               # Prints the complete tuple
# print(tuple[0])            # Prints first element of the tuple
# print(tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
# print(tuple[2:])           # Prints elements of the tuple starting from 3rd element
# print(tinytuple * 2)       # Prints the contents of the tuple twice
# print(tuple + tinytuple)   # Prints concatenated tupless

# ###############################################  dict
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print(dict)
print(dict['one'])       # Prints value for 'one' key
print(dict[2])           # Prints value for 2 key
print(dict.keys())   # Prints all the keys
print(dict.values()) # Prints all the values

print(tinydict)          # Prints complete dictionary
print(tinydict.keys())   # Prints all the keys
print(tinydict.values()) # Prints all the values