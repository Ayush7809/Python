a=int(input('Enter the number'))
s=0
for i in range(1,a):
    if a%i==0:
        s+=i 
if s==a:
    print('number is perfect')
else:
    print('number is not perfect')