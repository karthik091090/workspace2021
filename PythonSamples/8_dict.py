# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)


#####################  Duplicate values will overwrite existing values:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)
# print(len(thisdict))

################################
# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }
# print(type(thisdict))

# print(thisdict.keys())
# print(thisdict.values())

# x=thisdict.keys()
# print(x)

# x=thisdict.items()
# print(x)

######################################

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#     print("Yes, 'model' is one of the keys in the thisdict dictionary")

#####################################

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
###################    Print all key names in the dictionary, one by one:
# for x in thisdict:
#     print(x)
######
# for x in thisdict.keys():
#   print(x)

#########################   Print all values in the dictionary, one by one:
# for x in thisdict:
#     print(thisdict[x])
######
# for x in thisdict.values():
#   print(x)

######################
# for x, y in thisdict.items():
#     print(x, y)

########################  copy dict

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = dict(thisdict)
# print(mydict)

# mydict = thisdict.copy()
# print(mydict)


#####################
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004,
    "hobbies": ['cricket', 'football']
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)
myfamily['child1']['year']=2000
myfamily['child1']['hobbies'].append('hockey')
print(myfamily)