"""Q10.Create a function that takes 2 positive integers in form of a string as an input, and outputs the sum (also as a string):

"4",  "5" --> "9"
"34", "5" --> "39"""

def num(a,b):
    i=0
    while i<len(a):
        d=int(a)+int(b)
        i+=1
    print(d)
num("4",  "5")


