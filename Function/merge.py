def merge_the_tools(string, k):
    n=len(string)
    
    for i in range (0,n,k):
        string=string[i:i+k]
        l=[]
        for j in string:
            if j not in l:
                l.append(j)
            
        print ("".join(l))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    