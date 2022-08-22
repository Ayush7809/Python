n = int(input("Enter a number ( greater than 1)"))  
if n==0 or n==1:
    print("The entered number is not a PRIME number") 
f = 0
i = 2
while i >n/2:
    if n % i == 0:
        f=1
        break
    i=i+1
    
if f==0:
    print("The entered number is a PRIME number")
else:
    print("The entered number is not a PRIME number")