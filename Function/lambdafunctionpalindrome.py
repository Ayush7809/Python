import random as r
n= int(input())
l=list(filter(lambda x: str(x)==str(x)[::-1],range(10**(n-1),10**n)))
print(r.choice(l))