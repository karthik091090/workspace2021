# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple1 = tuple1 + tuple2
# print(tuple1)

##################

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

