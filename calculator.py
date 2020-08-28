def add(x, y):
    return x+y

def factorial(n):
    if (n<0): #not gonna do this case
        return None
    else:
        i=1
        while(n>0):
           i *= n
           n -= 1
        return i 

def sin(x, N):
    N = abs(N)
    tot = 0
    while(N>=0):
        tot += (-1)**N*x**(2*N+1)/factorial(2*N+1)
        N -= 1
    return tot

def divide(a, b):
    return a/b

def cos(x, N):
    N = abs(N)
    tot = 0
    while(N>=0):
        tot += (-1)**N*x**(2*N)/factorial(2*N)
        N -= 1
    return tot

def tan(x, N):
    return sin(x, N)/(cos(x, N))