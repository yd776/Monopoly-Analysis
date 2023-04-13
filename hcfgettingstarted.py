#basics of python
def gcd(a,b):
    for i in range(1,min(a,b)+1):
        if (a%i==0) and(b%i==0):
            print(i)
def is_prime(n):
    if n==2:
        return True
    for i in range(2,int(n**.5)+1):
       
        if(n%i==0):
            return False
    
    return True

def factors(n):
    a=[]
    for i in range(1,int(n//2)):
        if n%i==0:
            a.append(i)
    return a
def primesupto(m):
    pl=[]
    for i in range(1,m):
        if(is_prime(i)):
            pl.append(i)
    return pl

def firstrimes(m):
    (count,i,pl)=(0,1,[])
    while(count<m):
        if(is_prime(i)):
            (count,pl)=(count+1,pl+[i])
        i=i+1
    return pl


def prime(m):
    result=True
    for i in range(2,m):
        if (m%i)==0:
            return False
            break
    return False

#using dictionaries

def primediffs(n):
    lastprime=2
    pd={}
    for i in range(3,n+1):
        if(is_prime(i)):
            d=i-lastprime
            lastprime=i
            if d in pd.keys():
                pd[d]=pd[d]+1
            else:
                pd[d]=1
    return pd


