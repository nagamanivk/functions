def function():
    if len (password)>=6:
        if  password in "@"  or "#" or "$" or password:
            if password>="A"  or password<="Z":
                if password>="a" or password<="z":
                    if password>="0" or password<="9":
                        print("strong password")
                    else:
                        print("enter proper number")
                else:
                    print("enter proper lower case")
            else:
                print("enter valid upper case")
        else:
            print("enter proper special character")
    else:
        print("enter valid length")
password=input("enter the no:")
function()

