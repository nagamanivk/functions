"""Q46. Draw a flowchart to take a list of N numbers from the user, 
print True if the complete list consists of consecutive numbers with a difference of one. 
Print False otherwise. 

Sample Input:
1 2 3 4 5 6 7
Sample Output:
True
Sample Input:
45 46 47 48 49 51 52
Sample Output:
False
Sample Input:
4 5 6 7 8 9 10
Sample Output:
True

Sample Input:
-5 -6 -7 -8

Sample Output:
False
Sample Input:
-3 -2 -1 0 1
Sample Output:
True"""

def function(a):
    i=0
    b=0
    c=0
    while i<len(a)-1:
        if a[i+1]-a[i]==1:
            b+=1
        else:
            c+=1
        i+=1
    if c==1:
        print("false")
    else:
        print("true")
function([56,57,58,51,52])

# def function(a):
#     i=0
#     while i<len(a)-1:
#         d=a[i+1]-a[i]
#         if d!=1:
#             return False
#         else:
#             return True
#     i+=1
# print(function([45, 46, 47, 48, 49, 51, 52]))















