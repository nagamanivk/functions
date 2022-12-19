"""Q26. Write a function called fizz_buzz that takes a number.
If the number is divisible by 3, it should return “Fizz”.
If it is divisible by 5, it should return “Buzz”.
If it is divisible by both 3 and 5, it should return “FizzBuzz”.
Otherwise, it should return the same number."""
def function():
    i=0
    while i<=100:
        if i%3==0 and i%5==0:
            print("fizz buzz")
        
        elif i%3==0:
            print("fizz")
        
        elif i%5==0:
            print("buzz")
        
        else:
            print(i)
        i=i+1
function()
        
