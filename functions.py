from multipledispatch import dispatch

@dispatch (int, int, int)
def sum(a,b,c):
    result=a+b+c
    print(result)

@dispatch (float,float,float)
def sum(u,r,t):
    result=u+r+t
    print (result)

sum(2,3,4)
sum(3.2,1.2,5.1)