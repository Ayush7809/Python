def prime(x):
    if x==0 or x==1:
        return False
    for i in range(2,x):
            if x%i==0:
                return False
    else:
        return True
n=eval(input())
print(prime(n))