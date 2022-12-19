def fibonacci(a):
    if a<=1:
        return a
    else:
        return (fibonacci(a-1)+fibonacci(a-2))
n=int(input("enter the number"))
if n>0:
    i=0
    while i<=n:
        print(fibonacci(i))
        i=i+1