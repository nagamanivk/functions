"""Q36. I would like to be able to pass an array with two elements to my swapValues function to swap the values. However it appears that the values aren't changing.
Can you figure out what's wrong here?"""

def function(a,b):
    c=a
    a=b
    b=c
    print(a,b)
function(2,5)
