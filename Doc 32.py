"""Q32.Complete the function that takes a non-negative integer n as input, and returns a list of all the powers of 2 with the exponent ranging from 0 to n (inclusive). 
n=0 == >[1]   #[2^0]
n = 1  ==> [1, 2]     # [2^0, 2^1]
n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]."""

# b=[]
# def power(n):
#     i=0
#     while i<=n:
#         c=2**i
#         b.append(c)
#         i+=1
# n=int(input("enter the no:"))
# print(power(n),(b))


# x=[3,4,5]
# a,b,c=x
# print(a+b+c)

# a="apple"
# b="banana"
# c=a+b
# d=b+a
# e=(str(c),"or",str(d))
# print(e)
# e=(str(c or d))
# f=(str(d or c))
# print(str(e),(str(f)))

a="apple"
a="banana"
b='"applebanana"'
c='"bananaapple"'
print(b,"or" +c)