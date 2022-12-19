"""Q34. Write a function which converts the input string to uppercase.
Write a function which converts the input string to uppercase.
For example:-
[10, 14, 2, 23, 19] -->  42 (= 23 + 19)
[99, 2, 2, 23, 19]  --> 122 (= 99 + 23)
Input sequence contains minimum two elements and every element is an integer."""

def add(a):
    i=0
    max1=0
    max2=0
    while i<len(a):
        if a[i]>max1:
            max1=a[i]
        elif a[i]>max2:
            max2=a[i]
        i+=1
    print(max1+max2)
a=[10, 14, 2, 23, 19]
add(a)


            