n=1000000
sum=0
import math

t=[]
for i in range(0,n+1):
    t.append(0)
t[1]=1
 
#to exam the circulatory prime number
def ex(x):
    z=0
    c=x
    while(c>0):
        z=z+1
        c=c/10
        a=z+c
    b=10**(z-1)
    c=x
    for i in range(0,z):
        if(t[c] and a!=c):
            return 0
        else:
            c=c/10+(c%10)*b
    return 1
     
#find prime numbers from 2 to 1000000
l=int(math.sqrt(n))
for i in range(2,l+1):
    if(not t[i]):
        c=2*i       
        s=2*c
        while(not c>n):
            t[c]=1
            c=c+i

for i in range(1,n+1):
    if((not t[i]) and ex(i)): 
        sum=sum+1
print (sum)
