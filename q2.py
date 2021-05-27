"""Question2 
Setup a dict structure like this in python
Dict1: (this is a key, value pair of user id and username)
{
   “1” : “name1”,
   “2” : “name2”,
   “3” : “name3”
} etc.. 
Dict2: (this is a key value pair of user id and exam score) 
{
   “1” : 50,
   “2” : 60
   “3” : 70
}
These are just sample data assume there are hundreds of users
Write a function in python in python, which will return maximum i.e function should return dictionary like
{
  “3” : 70
}
"""


def dict_1_2(n):
    l=[str(i) for i in range(1,n+1)]
    dict1={}
    dict2={}
    dict3={}
    for i in l:
        dict1[i]=input("please enter the name of student")
    for i in dict1:
        dict2[i]=int(input("enter the marks of the student"))
    ans=max(dict2.items())
    dict3[ans[0]]=ans[1]
    return dict3
n=int(input("enter the length of the dictionary"))
print(dict_1_2(n))
