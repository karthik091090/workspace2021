# num=int(input('enter a number'))
number=198

rev=0
while(number>0):
    dig=number%10
    print("dig: "+str(dig))
    rev=rev*10+dig
    print("\nrev: "+str(rev))
    number=number//10
    print("\nnumber: "+str(number))
print("The reverse of the number:",rev)