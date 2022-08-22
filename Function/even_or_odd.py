def even_or_odd(x):
        if x%2==0:
            return True
        else:
            return False
n=eval(input())
s=[]
l=[]
for i in n:
    if even_or_odd(int(i)):
        s.append(i)
    else:
        l.append(i)
print(s,l)