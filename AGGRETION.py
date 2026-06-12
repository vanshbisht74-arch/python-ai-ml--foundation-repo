class Customer:
    def __init__(self,gender,address):
        self.gender=gender
        self.address=address

    def edit_profile(self,new_name,new_city,new_pin,new_state):
        self.new_name=new_name
        self.address.edit_address(new_city,new_pin,new_state)

    def print_address(self):
        print(self.address.city, self.address.pincode,  self.address.state)

class Address:
    def __init__(self,city,pincode,state):
        self.city=city
        self.pincode=pincode
        self.state=state

    
        
    def edit_address(self,new_city,new_pin,new_state):
        self.new_city=new_city
        self.new_state=new_state
        self.new_pin=new_pin

add1=Address("almora","220107","uttrakhand")
cust=Customer("Male",add1)
cust.print_address()