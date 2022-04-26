names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
names2 = names1
names3 = names1[:]

# print(names1)
# print(names2)
# print(names3)

names2[0] = 'Alice'
names3[1] = 'Bob'

for ls in (names1, names2, names3):
    print(ls)