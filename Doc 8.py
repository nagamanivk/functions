"""Q8.Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Uppercase characters : 3
No. of Lower case Characters : 12"""

def case(a):
    u_c=0
    l_c=0
    i=0
    while i<len(a):
        if a[i].isupper():
            u_c+=1
        if a[i].islower():
            l_c+=1
        i+=1
    print(u_c)
    print(l_c)
case('The quick Brow Fox')

