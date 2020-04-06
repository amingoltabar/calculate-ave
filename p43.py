my_list=[]
for i in range(7):
    a=float(input('Create your list.Enter the integer '))
    while a!=int(a):
       a=float(input('You did not enter an integer.Enter the integer ') )
    a=int(a)
    my_list.append(float(input('Create your list.Enter the number ')))
x=float(input('Enter the  index '))
while x<0 or x>6 or x!=int(x):#Entered indexes must be integer and in the range of list.
    x=float(input('Index you have entered is out of range or non-integer.Enter the index again. '))
y=float(input('Enter the  index '))
while y<0 or y>6 or y!=int(y):
     y=float(input('Index you have entered is out of range or non-integer.Enter the index again. '))
x=int(x)
y=int(y)
def calculateave(array,x,y):#This function receives 2 indexes and a list.Then calculates the average of elements between these 2 indexes.
    s=0
    count=0
    if x<y:
        for i in range(x,y+1,1):
            s+=array[i]
            count+=1
        ave=s/count
    elif x>y:
        for i in range(y,x+1,1):
            s+=array[i]
            count+=1
        ave=s/count
    else:
        ave=array[x]
    return ave
if x>y:
    print(calculateave(my_list,x,y),'is the average of elements from index',y,'to index',x)
elif x<y:
    print(calculateave(my_list,x,y),'is the average of elements from index',x,'to index',y)
else:
    print('The average =',my_list[x])
    

    
        



