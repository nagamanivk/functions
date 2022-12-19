"""Q12.Numbers ending with zeros are boring.

They might be fun in your world, but not here.

Get rid of them. Only the ending ones.

1450 -> 145
960000 -> 96
1050 -> 105
-1050 -> -105"""

# def zeros(a):
#     i=0
#     b=[]
#     c=[]
#     while i<len(a):
#         c=str(a[i])
#         b.append(c)
#         j=0
#         s=""
#         while i<len(b[i]):
#             if b[i][j]!="0":
#                 s=s+b[i][j]
#             j+=2
#         g=int(s)98
#         i+=1
#     print(g)
# zeros([1450,960000,1050,-1050])
            
def zero(a):
    i=0
    j=str(a)
    while i<len(j):
        if j[i]!="0":
            print(j[i],end="")
        i+=1
zero(int(input("enter the no:")))
        