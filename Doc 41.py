"""Q41. Write a Python program to find the list with maximum and minimum length.
Original list:[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
List with maximum length of lists:
(3, [13, 15, 17])
List with minimum length of lists:
(1, [0])"""

def function(a):
    i=0
    max_l=a[i]
    min_l=a[i]
    while i<len(a):
        if a[i]>max_l:
            max_l=a[i]
        elif a[i]<min_l:
            min_l=a[i]
        i+=1
    print((len(max_l),max_l))
    print((len(min_l),min_l))
function([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])