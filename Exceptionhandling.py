# IndexError
# The IndexError is thrown when trying to access an item at an invalid index.

# ModuleNotFoundError
# The ModuleNotFoundError is thrown when a module could not be found.

# KeyError
# The KeyError is thrown when a key is not found.

# TypeError
# The TypeError is thrown when an operation or function is applied to an object of an inappropriate type.

#name error 
# Name error is thrown when an object is not found (like not declared and printing it)




#THESE ERROR MESSAGES IN CONSOLE OF ANY TYPE AND KNOW AS ""STACK TRACE"".
# AttributeError

# Traceback (most recent call last)

# <ipython-input-80-dd5a29625ddc> in <module>
#       1 # AttributeError
#       2 L = [1,2,3]
# ----> 3 L.upper()

# AttributeError: 'list' object has no attribute 'upper'



# Catching specipic exeption
try:
    m=5
    f=open("select.txt","r")
    

#ERRORS ARE CATCHED HERE
except FileNotFoundError:
    print("File Not Found")
except NameError:
    print("Varible not found")
except Exception as e:
    print(e)

# We Write that code inside the else block and that needs to execute when their is no
#Error in the try block , when the exept block is skiped.
else:
    print(m)
    print(f.read())


finally:
    print("THIS WILL PRINT ")


# ----------------------------------------------------------------------------------
#RAISE
class Bank:
    def __init__(self,balance):
        self.balance=balance

    def withdraw(self,amount):
        if amount <=0:
            raise Exception("Amount can't be negative or zero ")
        if amount>self.balance:
            raise("Insufficient Funds")
        
        else:
            self.balance-=amount

obj=Bank(10000)

try:
    obj.withdraw(1000)

except Exception as e:
    print(e)

else:
    print("Remaining Funds",obj.balance)

finally:
    print("Thank you for using")



#----------------------------------------------------------------------------------------
#MAKING OWN CUSTOM CLASSES FOR EXCEPTION HANDLING 
class Myexception(Exception):
  def __init__(self,message):
    print(message)


class Bank:
    def __init__(self,balance):
        self.balance=balance

    def withdraw(self,amount):
        if amount <=0:
            raise Myexception("Amount can't be negative or zero ")
        if amount>self.balance:
            raise Myexception("Insufficient Funds")
        
        else:
            self.balance-=amount

obj=Bank(10000)

try:
    obj.withdraw(1000000)

except Myexception as e:
  pass

else:
    print("Remaining Funds",obj.balance)

finally:
    print("Thank you for using our system")



#--------------------------------------------------------------------------------------------

#CUSTOM CLASSES



class SecurityError(Exception):
  def __init__(self,message):
      print(message)
  def logout(self):
    print("Logout done")

class Google:
  def __init__(self,name,email,password,device):
      self.name=name
      self.email=email
      self.password=password
      self.device=device
  

  def login(self,email,password,device):
        
        if device!=self.device:
          raise SecurityError("LOGIN FROM A NEW OR UNREGISTERED DEVICE FOR SECURITY REASONS LOGGING OUT FROM ALL DEVICES.......")
        if email==self.email and password==self.password:
          print("WELCOME.....")

        else:
          print("WRONG EMAIL OR PASSWORD PLEASE TRY AGAIN")


obj=Google("Vansh","vanshbisht74@gmail.com","1234","android")

try:
  obj.login("vanshbisht74@gmail.com","1234","IOS")

except SecurityError as e:
  e.logout()

else:
  print("--->",obj.name)

finally:
  print("DATABASE CONNECTION DISCONNECTED ")



  
#-------------------------------------------------------------------------------------