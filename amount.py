A=int(input('Enter the amount'))
if A>25000:
    print('you are in gold category')
    d=A*.20
    a=A-d
    print("Total amount you pay is:",a)
elif A>15000 and A<=25000 :
    print('you are in silver category')
    d=A*.15
    b=A-d
    print('Total amount you pay is:',b)
else:
    print('you are in bronze category')
    d=A*.10
    c=A-d
    print('Total amount you pay is:',c)