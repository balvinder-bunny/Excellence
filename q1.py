"""Question1
Use python lists and make an list of numbers.
Write a function which returns sum of the list of numbers"""

def sum(num):
    ans=0
    for i in num:
        ans+=i
    return ans

print(sum([int(i) for i in input().split()]))
