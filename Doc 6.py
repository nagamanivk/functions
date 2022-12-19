"""6.Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]."""

# def even(a):
#     i=0
#     b=[]
#     while i<len(a):
#         if a[i]%2==0:
#             b.append(a[i])
#         i=i+1
#     print(b)
# even([1, 2, 3, 4, 5, 6, 7, 8, 9])
n=int(input("enter the no:"))
i=1
max=0
min=1000
while i<=n:
    user=int(input("enter the no:"))
    if user>max:
        max=user
    if user<min:
        min=user
    i=i+1
print("largest value is",max)
print("smallest no is",min)
