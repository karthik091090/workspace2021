
list=[1,3,3,4,5,6,6,7,8,9,9]

search_element=int(input("Enter the search element: "))    

index=0
for x in list:
    
    if x == search_element:
        print(f"search element: {search_element} is at index:  {index}")
        index=index+1
if index==0:
    print("Element not found")
    