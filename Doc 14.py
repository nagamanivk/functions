"""Q14.Write a function to check if a number is prime or not."""
def prime():
    i=1
    c=0
    while i<=n:
        if n%i==0:
            c+=1
        i+=1
    if c==2:
        print("prime")
    else:
        print("not prime")
n=int(input("enter the no:"))
prime()
    


