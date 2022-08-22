list=[1,2,3,4,56,]
check=int(input('Enter no to be search'))
#list=[5,9,8,7,6,3,2] list change krne ke liye
if check in list:
    x=list.index(check)
    print('Exist on index:',x)
else:
    print('not found') 