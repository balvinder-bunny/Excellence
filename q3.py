"""Question 3
Assume we have list like this
[0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]
Basically a list of zero’s and one’s.
Write a python function to the number of maximum consecutive  one’s present in the array. 
E.g output for the above array would be 4"""


def count(lst):
    count=0
    for i in range(len(lst)):
        if i==0 and lst[i]==1:
            count+=1
        if lst[i]==1 and lst[i-1]==0:
            count+=1
    return count
print(count([0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]))
