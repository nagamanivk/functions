"""Q44.Bonus - Given the same list, print the last ‘N’ elements in reverse order.
Sample Input:
2
Sample Output:
q
b 
Sample Input:
3
Sample Output:
q
b 
5"""
def function(a):
    n=int(input("enter the no:"))
    d=-1
    while d>=-(len(a)-n):
        print(a[d])
        d-=1
function(["a",1,"2",5,"b","q"])

    
