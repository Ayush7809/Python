def squaresum(x):
    c=d=0
    li=[]
    for i in x:
        if i%2==0:
            c=c+i**2
            
        else:
            d=d+i**2
    li.append(c)
    li.append(d)
    return(li)            
n=list(map(int,input().split()))
print(squaresum(n))
