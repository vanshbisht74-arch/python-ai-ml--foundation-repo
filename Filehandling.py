#CASE 1
# How I/0 is done in pyhton
# 1)Open a FA\ile
# 2)Read/Write Data
# 3)Close the File 
f=open("select.txt","w")
f.write("Hello Vansh")
f.close()

#NOW YOU CAN'T WRITE AGAIN BELOW CLOSE OPERATION
# f.write("hello") ----> "ERROR"

#----------------------------------------------------------------------------------
#Write multiline strings

f=open("select1.txt","w")
f.write("hello vansh")
f.write("\n hyyy")
f.close()
#-----------------------------------------------------------------------------------

#CASE 2: IF THE FILE IS ALREADY PRESENT AND WANNA ADD TEXT TO IT 
f=open("select.txt","w")
f.write("hello again vansh")
f.close()

#a mode 
f=open("select.text","a")
f.write("h")
f.close()
#appending




#wRITE LINES
l=["hello","hi","hola","bye"]
f=open("select.txt","w")
f.writelines(l)
f.close()


#--------------------------------------------------------------------------------------
#Reading from the files
#using read()
f=open("select.txt","r")
s=f.read()
print(s)
f.close()


#read upto 10(n) char
f=open("select.txt","r")
s=f.read(10)
print(s)
f.close()


#readline()--> read line by line
f=open("select.txt","r")
s=f.readline()
print(s)
f.close()



#---------------------------------------------------------------------------------------

#reading entire file using readline()
f=open("Select.txt","r")
data=f.readline()
while True:
    if data=="":
        break
    else:
        print(data,end="")

f.close()



#USING CONTEXT MANAGER (WITH):-
#so now there is no need to close the file again and again                       
with open("select.txt","w") as f:
    f.write("HELLO")


#using with for read()
with open("select.txt","r") as f:
    print(f.read())


#To load a big data into the memory we divide the data into the chunka and then push 
#it into the RAM.
big_l = ["hlo" for i in range(100)]

with open("select1.txt", "w") as f:
    f.write(" ".join(big_l))

with open("select1.txt", "r") as f:
    chunk_size = 100

    while True:
        chunk = f.read(chunk_size)

        if not chunk:
            break

        print(chunk, end="->")
#-------------------------------------------------------------------------------------





#seek and tell function
with open("select1.txt","r") as f:
    print(f.read(10))  
    print(f.tell()) #output-> 10   tells where is cursor or buffer right now
    f.seek(0)  #takes the cursor back or forth to any position 
    print(f.read(10)) #again prints the same character same as above
    print(f.tell())


#seek during write 

with open("select2.txt","w") as f:
    f.write("HELLO")
    f.seek(0) #back to 0
    f.write("XD") # output --> XDLLO   the text will not get replaced it will just change 
    #like this


#Working with the binary files
#opening the binary file
with open("photo.webp","rb") as f:
    with open("photo_copy.webp","wb") as wf:
        wf.write(f.read())


#---------------------------------------------------------------------------------------




#SERIALIZATION AND DESERIALIZATION 
#SERIALIZATION : The process of converting the pyhton data types to the JSON format
#DESERIALIZATION :The process of converting the JSOn format into the pytthon data types 
#Example---> #SERIALIZATION :
import json
l=[1,2,3,4,5,6,7,8,9,10]
with open("demo.txt","w") as f:
    json.dump(l,f)
    


d={
    "name":"vansh",
    "age":"18",
    "gender":"male"
}

with open("demo.txt","w") as f:
    json.dump(d,f)

#Example---->#DESERIALIZATION 
with open("demo.txt","r") as f:
    d=json.load(f)
    print(d)
    print(type(d))
    # So now here the type comes out to be the dict only but earlier when we were not using 
    #SERIALIZATION and DESERIALIZATION then every data type was automatically converted to 
    #string format and we are not able to perform the data types related operations but now 
    #the data types remains the same .

#---------------------------------------------------------------------------------------
                #SERIALIZATION AND DESERIALIZATION FOR CUSTOM CLASS OBJECT




class Person:
    def __init__(self,fname,lname,gender,age):
        self.fname=fname
        self.lname=lname
        self.gender=gender
        self.age=age


person=Person("vansh","bisht","male","18")




# import json
# with open("demo.txt","w") as f:
#    f.write(person) #---> error usko pata hi nahi hai ese kaise serialise krte hai 
##dict and list etc phele se pata hai vo universal hai ki unhe kaise serialize or deserialize 
##krte hai par apne class ke object ke leye hume pehele batana padaga ki usko kaise krna hai
        

import json



def show_object(person):
    if isinstance(person,Person):
        return  "{}  {}  age: {}  gender: {}  ".format(person.fname,person.lname,person.age,person.gender)
    


with open("demo.txt","w") as f:
    json.dump(person,f,default=show_object)


#THE PICKLING IS THE PROCESS WHERE THE A PYTHON OBJECT IS CONVERTED INTO A BYTE STREAM 
#UNPICKLING IS THE REVERSE PROCESS WHERE THE A BYTE STREAM IS CONVERTED BACK TO THE OBJECT 
#HEIRARCY.

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print('Hi my name is', self.name, 'and I am', self.age, 'years old')
p=Person("vansh")

import pickle
with open("pickle.txt","wb") as f:
    pickle.dump(p,f)
