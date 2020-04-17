my_list=[]
count=1
print('Creating the list')
while len(my_list)<7: #creating the list
    print('Enter the integer number',count,end='')
    a=input(':')
    try:
        val=int(a)
        my_list.append(val)
        count+=1
    except ValueError:
        try:
            val=float(a)
            print('You entered a float. ')
            pass
        except ValueError:
            print('You did not enter a number. ')
            pass
index_list=[]
count_1=0
while len(index_list)<2: #inputting indexes
    print('Enter the index number',count_1+1,end='')
    b=input(':')
    try:
        val=int(b)
        if val<=6 and val>=0:
            index_list.append(val)
            count_1+=1
        else:
            print('Your entered number is not in range.')
    except ValueError:
        try:
            val=float(b)
            print('You entered a float.')
        except ValueError:
            print('You did not enter a number.')
x=index_list[0]
y=index_list[1]
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
    

    
        



