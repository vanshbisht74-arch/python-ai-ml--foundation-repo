class Atm:
    def __init__(self):
        
        self.pin=''
        self.balance=0
        self.menu()

    def menu(self):
        user_input=input('''HOW CAN I HELP YOU
              PRESS 1 FOR CREATE PIN
              PRESS 2 FOR CHANGE PIN 
              PRESS 3 TO CHECK BALANCE
              PRESS 4 FOR EXITING 
              ''')
        
        if user_input=='1':
            self.create_pin()


        elif user_input=='2':
            self.change_pin()

        elif user_input=="3":
            self.check_balance()

        elif user_input=="4":
            self.

        

        elif user_input=="5":
            exit()

        else:
            print("INVALID INPUT")

        

        
    def create_pin(self):
        user_pin=int(input("ENTER YOUR PIN"))
        self.pin=user_pin

        user_balance=int(input("ENTER YOUR BALANCE"))
        self.balance=user_balance
        print("PIN CREATED  SUCESSFULLY")
        self.menu()


    def change_pin(self):
        old_pin=int(input("ENTER OLD PIN TO CONTINUE CHANGING YOUR PIN"))
        if old_pin==self.pin:
            new_pin=int(input("ENTER NEW PIN "))
            self.pin=new_pin
            print("PIN CHANGED SUCCESSFULLY")
            self.menu()
        else:
            print("WROUNG PIN ,RE-ENTER YOUR PIN1")
            self.change_pin()

    def check_balance(self):
        cb_pin=input("ENTER YOUR PIN")
        if cb_pin==self.pin:
            print("YOUR BALANCE = ",self.balance)
        else:
            print("WROUNG PIN  , RE-ENTER")
            self.check_balance()

        self.menu()


    def withdraw(self):
        w_pin=input("ENTER YOUR PIN")
        if w_pin==self.pin:
            enter_money=input("ENTER AMPOUNT TO WITHDRAW")
            if enter_money<=self.balance:
                self.balance-=enter_money
                print("WITHDRAWL SUCESSFULL ")
                print("Balance left",self.balance)

            else:
                print("INSUFFICENT BALANCE")
                self.withdraw()

        else:
            print("THIS PIN IS NOT CORRECT PLEASE RE-ENTER YOUR PIN TO PROCEED ")
            self.withdraw()

        self.menu()






obj=Atm()
     
