# Program to find +ve numbers in the list
# empty lists
alist = []
newlist = []

# taking input
n = input('Enter some numbers seperated by commas: ')

# creating a list of input
mylist = n.split(',')

# typecasting to integer and entering to a new list 'alist'
for x in mylist:
    y = int(x)
    alist.append(y)

# printing list enterd by user
print(alist)

#checking positive numbers in 'alist'
for y in alist:
    if abs(y) == y:
        newlist.append(y)

#printing positive numbers
if len(newlist) == 0:
    print('There is no positive number in this list.')
else:
    print('Positive numbers are:',newlist)