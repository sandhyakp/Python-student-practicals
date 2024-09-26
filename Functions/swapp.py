def swap(a,b):
    c=a
    a=b
    b=c
    return a,b


x=2
y=9
x,y=swap(x,y)
print(x,y)
