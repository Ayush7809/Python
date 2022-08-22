n=int(input('Enter the amount'))-100
tt=0
fh=0
h=0
tt=n//2000
n=n-tt*2000
fh=n//500
n=n-fh*500
h=n//100+1
out=f'''2000 notes {tt}
500 notes {fh}
100 notes {h}'''
print(out)