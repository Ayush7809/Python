from re import S


'''def perfect(x):
    s=0
    for i in range(1,x):
        if x%i==0:
            s+=i
    if s==x:
        return ('perfect')
a=int(input())
print(perfect(a))'''




def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
a=int(input())
print(perfect_number(a))