"""Q3.Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Output : 20."""

def sum(a):
    i=0
    sum=0
    while i<len(a):
        sum=sum+a[i]
        i=i+1
    print(sum)
sum([8, 2, 3, 0, 7])

