
def function():
    if language=="english":
        passcode=int(input("enter the no:"))
        if passcode==4882:
            print("1.withdrawal") 
            print("2.balence enquiry")
            print("3.ministatement") 
            print("4.deposit") 
            print(" 5.pin genration") 
            balence=100000
            transaction=int(input("enter transaction:"))
            if transaction==1:
                withdrawel=int(input("enter the withdrawel amount:"))
                if withdrawel<=balence:
                    print("collect your cash",withdrawel)
                    print("remaining balence is",withdrawel-balence)
                else:
                    print("not withdrawel")
            if transaction==2:
                balenceenquiry=input("enter the balence enquiry:")
                if balenceenquiry== "saving":
                    print("your balence",balence)
                else:
                    print("not enquiry")
            if transaction==3:
                ministatement=input("enter the ministatement:")
                if ministatement=="kcc":
                    print("take your ministatement")
                else:
                    print("not coming")
            if transaction==4:
                deposit=int(input("enter the amount:"))
                if deposit>=10:
                    print("your deposit is successfully completed")
                else:
                    print("not completed")
            if transaction==5:
                pingenration=int(input("enter the new pin:"))
                if pingenration==1234:
                    print("new pin is successfully completed")
                    print("thank you")
                else:
                    print("not genrated new pin")
    else:
        print("enter valid language")
print("insert your card")
print("welcome to S.B.I")
print("please select your language")
language=input("enter the language:")
function()

