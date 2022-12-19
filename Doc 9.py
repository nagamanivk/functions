"""Q9.Write a Python program to generate and print a list of first and last 5 elements where 
the values are square of numbers between 1 and 30 (both included).
Output :-([1, 4, 9, 16, 25], [676, 729, 784, 841, 900])."""

# def num():
#   i=1
#   b=[]
#   while i<=30:
#     b.append(i**2)
#     i+=1
#   a=b[1:6]
#   c=b[25:31]
#   print((a,c))
# num()
def num():
  d=30
  i=1
  b=[]
  c=[]
  while i<=d:
    if i<=n:
      b.append(i**2)
    if i>d-n and i<=d:
      c.append(i**2)
    i+=1
  print(b,c)
n=int(input("enter the no:"))
num()

  


