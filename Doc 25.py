"""Q25. Given a list of numbers, write a Python program to count positive and negative numbers in a List using function.
Example:
list1 = [2, -7, 5, -64, -14]
Output: pos = 2, neg = 3"""

def pnc(a):
    i=0
    p_n=0
    n_n=0
    while i<len(a):
        if a[i]>0:
            p_n+=1
        else:
            n_n+=1
        i+=1
    print(p_n)
    print(n_n)
pnc([2, -7, 5, -64, -14])