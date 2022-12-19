"""Q2.Write a Python function to find the Max of three numbers."""

def max(a):
    i=0
    max=0
    while i<len(a):
        if a[i]>max:
            max=a[i]
        i+=1
    print(max)
max([10,20,30])


