"""Q42. Find the sum of number digits in List.
The original list is : [12, 67, 98, 34]
List Integer Summation : [3, 13, 17, 7]
Explanation: 1+2 = 3, 6+7=13, 9+8=17, 3+4=7
The original list is : [15, 81, 11, 234]"""


def function(a):
    b=[]
    i=0
    while i<len(a):
        sum=0
        while a[i]>0:
            sum=sum+a[i]%10
            a[i]=a[i]//10
        i+=1
        b.append(sum)
    print(b)
function( [12, 67, 98, 34])


    


