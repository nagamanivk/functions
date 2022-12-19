"""Q27. Write a function for checking the speed of drivers. This function should have one parameter: speed.
If speed is less than 70, it should print “Ok”."""

def function(speed):
    if speed<70:
        print("ok")
    if speed>70:
        i=70
        while i<=70:
            point=(speed-70)//5
            if point>12:
                print(point,speed,"licence suspend")
            else:
                print(point,speed,"ok")
            i+=1
speed=int(input("no"))
function(speed)
        