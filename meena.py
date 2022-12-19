# def function(a):
#     i=0
#     u_l=0
#     l_l=0
#     while i<len(a):
#         if a[i].isupper():
#             u_l+=1
#         else:
#             l_l+=1
#         i+=1
#     print(u_l)
#     print(l_l)
# function("My NaMe iS MeEnA")

def function(a):
    i=0
    b=[]
    c=[]
    while i<len(a):
        if a[i]!=[]:
            b.append(a[i])
        else:
            c.append(a[i])
        i+=1
    print(b)
    print(c)
function([[],2,[],4,[],6,[],8,[],10])