x=int(input('Enter the side x'))
y=int(input('Enter the side y'))
z=int(input('Enter the side z'))
if x==y==z :
    print('equilatrial triangle')
elif x==y or y==z or z==x:
    print('isosceles triangle')
elif x==(y**2+z**2)**.5 or y==(x**2+z**2)**.5 or z==(x**2+y**2)**.5 :
    print('right angled tringle')

else :
    print('scalene triangle')

