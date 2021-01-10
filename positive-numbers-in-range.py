# creating empty list
mylist = []

# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, n): 
    ele = int(input()) 
    mylist.append(ele) # adding the element 

print('List entered by you : ',mylist)

# checking +ve numbers
print('Printing Positive Numbers in the list : ')
for x in mylist:
    if abs(x) == x:
        print(x,end=' ')