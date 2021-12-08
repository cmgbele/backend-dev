print("Welcome To CHRISBANK")
Trials = 3
Userpin = 1234 

while Trials != 0:
    pin = int(input("Please Enter Your 4 digit pin Number: :")) 
    if pin != Userpin:
        Trials -= 1 
        print("Wrong pin Number,You Have,Trials", Trials,"Trials Left")
    else: 
         Userchoice = input("d:Deposit or w: Withdraw: ")
         if Userchoice == "d": 
                UserDeposit = input("Enter TheAmount You Would like to Deposit: ") 
                print(UserDeposit, "$ Have Been Deposited Into your Account") 
         if Userchoice == "u": 
                UserDeposit = input("Enter TheAmount You Would like to withdraw: ") 
                print(UserDeposit, "$ Have Been withdrawn Into your Account") 
UserExit = input("Would You Like To Continue? Y/N: ") 
if UserExit == "N":
    print("Thank You For Using CHRISBANK ")
   
    


