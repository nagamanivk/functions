"""Q7.Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese" """

def function(weight,height):
    bmi=(weight/(height*height))*10000
    if bmi<=18.5:
        c="Underweight"
        return c
    elif bmi<=25.0:
        c="normal"
        return c
    elif bmi<=30.0:
        c="overweight"
        return c
    elif bmi>30:
        c="Obese"
        return c
weight=(int(input("enter the no:")))
height=(int(input("enter the no:")))
print(function(weight,height))

    







