def balance(transaction,balence):
    if transaction==1:
                balenceenquiry=input("enter the balence enquiry:")
                if balenceenquiry== "saving":
                    print("your balence",balence)
                else:
                    print("not enquiry")
def withdrawel(transaction,balence):
    if transaction==2:
                withdrawel=int(input("enter the withdrawel amount:"))
                if withdrawel<=balence:
                    print("collect your cash",withdrawel)
                    print("remaining balence is",balence-withdrawel)
                else:
                    print("not withdrawel")
def ministatement(transaction):
    if transaction==3:
                ministatement=input("enter the ministatement:")
                if ministatement=="kcc":
                    print("take your ministatement")
                else:
                    print("not coming")
def deposit(transaction):
     if transaction==4:
                deposit=int(input("enter the amount:"))
                if deposit>=10:
                    print("your deposit is successfully completed")
                else:
                    print("not completed")
def exit():
    print("thank you for visiting")

def mainfun():
     balence=50000
     passcode=1234
     if language=="english":
        passcode=int(input("enter the pin:"))
        if passcode==1234:
            print("1.balence enquiry") 
            print("2.withdrawel")
            print("3.ministatement") 
            print("4.deposit")  
            print("5.exit")
            transaction=int(input("enter transaction:"))
            if transaction==1:
                balance(transaction,balence)
            if transaction==2:
                withdrawel(transaction,balence)
            if transaction==3:
                ministatement(transaction)
            if transaction==4:
                deposit(transaction)
            if transaction==5:
                exit()
print("insert your card")
print("welcome to S.B.I")
print("please select your language")
language=input("enter the language:")
mainfun()




            
    






    



    