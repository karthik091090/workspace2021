#################################################  multi line strings
# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)

#################################################  slicing
# b = "abcdefghijklm"
# print(b[2:5])
# print(b[:5])  ##### slice from the start
# print(b[2:])  ##### slice to the end
# print(b[5:-2])  ##### Negative Indexing
# print(b[-5:-2])  ##### Negative Indexing
# print(b[-1])  ##### Negative Indexing

#################################################  Modify

# a = "ABCdefghijkl"
# b = " WXYZ "
# c= "Hello, world, I, am"
# print(a.upper())
# print(a.lower())

# print(b.strip())
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

# print(b.replace('W','1'))
# print(b.replace(' ','2'))   ###replace space with a value

# print(a.split(','))
# print(c.split(','))
# print(c.split('o'))


txt = "I love apples, apple are my favorite fruit"
# x = txt.count("apple")
# print(x)

# y = txt.count("p")
# print(y)
# y = txt.count(" ")
# print(y)

# x = txt.find("love")
# print(x)

# myTuple = ("John", "Peter", "Vicky")
# x = "".join(myTuple)
# print(x)
# x = "-".join(myTuple)
# print(x)
# x = "\"".join(myTuple)
# print(x)