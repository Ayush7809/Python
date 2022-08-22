def SQUARE_SEQUENCE(x,y):
    return [i**2 for i in range(x,y)]
n=int(input())
m=int(input())
li = SQUARE_SEQUENCE(n,m)
print(li)