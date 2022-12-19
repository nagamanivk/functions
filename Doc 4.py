"""4.Write a Python program to reverse a string.
Sample String : "1234abcd"
Output : "dcba4321"""

# def rev(a):
#     i=1
#     b=[]
#     while i<=len(a):
#         d=a[-i]
#         b.append(d)
#         i+=1
#     print(b)
# rev("1234abcd")

def rev(a):
    i=len(a)
    b=""
    while i>0:
        b=b+a[i-1]
        i-=1
    print(b)
rev('"1234abcd"')




    
