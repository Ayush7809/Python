a=input()
mx=max(a)
a=a.replace(mx,'')
mx=max(a)
print(mx)



'''lst=input()
b=lst.split()
b=list(map(int ,b))
mx=b[0]
for i in b:
    if mx<i:
        mx=i
print('max',mx)
m=b[0]
for i in b:
    if i>m and i<mx:
        m=i
print('max',m)'''