"""Q40. Write a function For example, if we give 9119  the function should return  811181, as the  square of 9 
is 81 and sq"""
def function(n):
    a=""
    while n>0:
        b=n%10
        a=str(b**2)+a
        n=n//10
    print(a)
n=int(input("enter the number"))
function(n)
    

