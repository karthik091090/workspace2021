# thislist = ["apple", "banana", "cherry"]
# print(thislist)

# print(thislist[-1])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])


# ######################################################## Change value
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# if "apple" in thislist:
#     print("Yes, 'apple' is in the fruits list")

# thislist[1] = "blackcurrant"
# print(thislist)

# ############################################################ insert
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# ####################################################### append
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

############################################### Extend
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

################################################## Remove
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop()   ###### remove last item
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(0)  ###### remove item based on index
# print(thislist)


################################################## delete
# thislist = ["apple", "banana", "cherry"]
# del thislist
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

################################################## loop through list
# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#     print(x)

################################################## Loop Through the Index Numbers
# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#     print(i)
#     print(thislist[i])

################################################  List Comprehension
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)

# zlist=[a for a in range(10)]
# print(zlist)

################################################  SOrt
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist2 = [10, 2, 5]
# thislist.sort()
# print(thislist)

# thislist2.sort()
# print(thislist2)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)