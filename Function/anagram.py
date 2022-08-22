def ana(x,y):
    if sorted(x)==sorted(y):
        print('anagram')
    else:
        print('not anagram')
s,y=input().split()
ana(s,y)
