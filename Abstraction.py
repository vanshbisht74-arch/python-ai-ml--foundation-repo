from abc import ABC,abstractmethod
class Bankapp(ABC):
    def database(self):
        print("Connected to Database")
    @abstractmethod
    def security(self):
        pass

class Mobileapp(Bankapp):
    def mobile_login(self):
        print("Mobline login")

    def security(self):
        print("This is mobile security")
    
m=Mobileapp()
print(m.database())
print(m.security())