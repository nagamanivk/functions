"""Q35. Kids drink toddy.
	Teens drink coke.
	Young adults drink beer.
	Adults drink whisky.
	Make a function that receive age, and return what they drink.
Rules:-
Children under 14 old.
Teens under 18 old.
Young under 21 old.
Adults have 21 or more.
Examples: (Input --> Output)

13 --> "drink toddy"
17 --> "drink coke"
18 --> "drink beer"
20 --> "drink beer"
30 --> "drink whisky"."""

def function(n):
    if n<=14:
        print("drink toddy")
    elif 14<=n and n<=18:
        print("drink coke")
    elif 18<=n and n<=21:
        print("drink beer")
    elif n>=21 and n<30:
        print("drink beer")
    elif 30<=n:
        print("drinks whiskey")
    else:
        print("invalid")        
function(int(input("enter the no:")))
