"""1.Write a Python program to count the number of strings where the string length is 2     or more and the first and last characters are the same from a given list of strings.
 ist=['abc', 'xyz', 'aba', '1221']
result= 2."""

l=['abc', 'xyz', 'aba', '1221']
def result(l):
    i=0
    s=0
    while i<len(l):
        d=l[i]
        n=d[::-1]
        if d==n:
            s+=1
        i+=1
    print(s)
result(['abc', 'xyz', 'aba', '1221'])





