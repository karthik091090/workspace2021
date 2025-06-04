a=int(input("Enter number: "))

# maxrange=a//2+1
maxrange=(a//2)+1
print(maxrange)

k=0
for i in range(2,maxrange):
    if(a%i==0):
        k=k+1
if(k<=0):
    print("Number is prime")
else:
    print("Number isn't prime")