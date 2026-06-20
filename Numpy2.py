#Numpy arrays vs Python lists
#1.Speed:-

#Time func:
import time 
start=time.time()


 



    
    #Lists:

a=[i for i in range(1000000)]
b=[i for i in range(1000000)]

c=[]
for i in range(len(a)):
    c.append(a[i]+b[i])
    time_taken=time.time()-start

print("Time taken by the lists",time_taken)
#time taken by python lists --0.3559536933898926

    #Numpy array
import numpy as np
a1=np.arange(10000000)
b1=np.arange(10000000,20000000)
start=time.time()
c1=a1+b1
time_taken2=time_taken=time.time()-start
print("Time taken by the Numpy arrays",time_taken2)

#time taken by numpy arrays -- 0.024726152420043945




#This tells us that how faster the numpy arrays re in comapre to the python's standard list


#-----------------------------------------------------------------------------------------

#In terms of memory
# lists
a=[i for i in range(1000000)]
import sys
sys.getsizeof(a)




# numpy

a1=np.arannge(10000000,dtype=np.int32)
sys.getsizeof(a1)




#-----------------------------------------------------------------------------------------

#ADVANCED INDEXING
#1.FANCY INDEXING:-->IN FANCY INDEXING WE JUST TAKE A LIST AND ADD WHATEVER WE WANT
import numpy as np
a=np.arange(12).reshape(4,3)
print(a)
print()
print(a[[0,2,3]]) #first ,third ,fourth row prints


b=np.arange(24).reshape(6,4)
print(b)
print(b[:,[0,3]])
print(b[[0,4]])



#Boolean indexing
# Boolean Indexing->>we can applly a condition and find out anything
# a = np.random.randint(start,end,range)
a=np.random.randint(1,100,24).reshape(6,4)                   
print(a[a%2==0])

print(a[a>50])


print(a[(a>50) & (a%2==0)])


print(a[a%7==0])




# BROADCASTING
# Broadcasting Rules

# 1. Make the two arrays have the same number of dimensions.

# If the numbers of dimensions of the two arrays are different, add new dimensions with size 1 to the head of the array with the smaller dimension.

# 2. Make each dimension of the two arrays the same size.

# If the sizes of each dimension of the two arrays do not match, dimensions with size 1 are stretched to the size of the other array.
# If there is a dimension whose size is not 1 in either of the two arrays, it cannot be broadcasted, and an error is raised.



#WORKING WITH MATHEMATICAL FORMULAS :--
#Sigmoid 
import numpy as np
def sigmoid(array):
    return 1/(1+np.exp((-array)))

a=np.arange(10)
print(sigmoid(a))


#Mean squared error --> we calculate the error in the algorithm by (actual-predicated) ^2 .
actual=np.random.randint(1,50,25)
predicted=np.random.randint(1,50,25)
def mean_squared_error(actual,predicted):
    return np.mean((actual-predicted)**2)

mean_squared_error(actual,predicted)

#----------------------------------------------------------------------------------------------------------------------
#Working with the missing values 
a=np.array([1,2,3,4,np.nan,6])
print(a)
#these nan values are headache and we learn to remove these nan values

print(a[~np.isnan(a)]) #removes all the missimg values form the list

--------------------------------------------------------------------------------------------------------------------

#Plotting graphs
import matplotlib.pyplot as plt
import numpy as np
#x=y
x=np.linspace(-10,10,100)
y=x
plt.plot(x,y)
plt.show()




#y=x^2

x=np.linspace(-10,10,100)
y=x**2
plt.plot(x,y)
plt.show()

# y=sin(x)
x=np.linspace(-10,10,100)
y=np.sin(x)
plt.plot(x,y)
plt.show()

#y=xlogx

x=np.linspace(-10,10,100)
y=x*np.log(x)
plt.plot(x,y)
plt.show()


#sigmoid


x=np.linspace(-1-0,10,100)
y=1/(1+np.exp(-x))
plt.plot(x,y)
plt.show()
