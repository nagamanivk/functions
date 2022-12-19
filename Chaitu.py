# def function(a):
#     i=0
#     while i<len(a):
#         d=a[i]
#         e=d.capitalize()
#         print(e,end="")
#         i+=1
# function(["ice cream"])

# a=["mani","jyo"]
# i=0
# j=-1
# b=[]
# while i<len(a):
#     c=a[i][j]
#     b.append(c)
#     i+=1
# print(b)

# a=["mani","jyo"]
# def fun(a):
#     i=0
#     j=-1
#     b=[]
#     while i<len(a):
#         c=a[i][j]
#         b.append(c)
#         i+=1
#     print(b)
# fun(a=["mani","jyo"])

# a=["a","b","a","a","d","e","c","f"]
# def fun(a):
#     i=0
#     while i<=len(a):
#         d=a[i]+a[i+1]
#         i+=3
#         print(d,end="")
# fun(a=["a","b","a","a","d","e","c","f"])

# a=["a","a","e","e","b","d","d","a","h","e"]
# i=0
# count=0
# while i<len(a):
#     d=a[i]
#     e=d.count(a[i])
#     i+=1
#     count+=1
# print(count)

def function(a):
    i=0
    c=[]
    while i<len(a):
        b=a.count(a[i])
        if a[i] not in c:
            c.append(a[i])
            print(a[i]+str(b),end="")
            
        i=i+1
function("mani")



# b=[]
# i=0
# while i<len(a):
#     d=a[i]
#     j=0
#     c=[]
#     count=0
#     while j<len(a):
#         k=a[j]
#         if d==k:
#             count=count+1
#         j=j+1
#     c.append(d)
#     c.append(count)
#     if c not in b:
#         b.append(c)
#     i=i+1
# print(b)









# def function(str1,str2):
#     if (str1)==(str2):
#         print("both are anagrams")
#     else:
#         print("not anagrams")
# str1="python"
# str2="ythopn"
# function(str1,str2)


# def function(a):
#     i=0
#     c=[]
#     while i<len(a):
#         b=a.count(a[i])
#         if a[i] not in c:
#             c.append(a[i])
#             print(a[i]+str(b),end="")
            
#         i=i+1
# function("mani")

# def function(str1,str2):
#     if sorted(str1)==sorted(str2):
#         print("both are anagrams")
#     else:
#         print("not anagrams")
# str1="python"
# str2="ythopn"
# function(str1,str2)

# def is_anagram(a,b):
#     l1=len(a)
#     l2=len(b)
#     count=0
#     if l1==l2:
#         for i in a:
#             for j in b:
#                 if i==j:
#                     count+=1
#     if count==l1:
#         print("both are anagrams")
#     else:
#         print("not anagrams")
# a=input("enter the word:")
# b=input("enter the word:")
# is_anagram(a,b)


# def is_anagram(a,b):
#     l1=len(a)
#     l2=len(b)
#     count=0
#     i=0
#     while i<len(a):
#             if a[i] in b:
#                 count+=1
#             i+=1
#     if count==l2:
#         print("anagram")
#     else:
#         print("not")
# is_anagram("bad","dad")

# def function(a):
#     i=0
#     b=[]
#     c=[]
#     while i<len(a):
#         if a[i]!=[]:
#             b.append(a[i])
#         else:
#             c.append(a[i])
#         i+=1
#     print(b)
#     print(c)
# function([[],2,[],4,[],6,[],8,[],10])

# a="meena"
# a=143
# b=str(a)
# print("meena"+str(a))

# a="ishu"
# b="mani"
# c=18.0
# d=10
# e=int(c)
# f=d+e
# print(a,b+"@"+"#",f)


