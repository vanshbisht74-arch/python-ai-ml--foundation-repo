#NUMPY IS A OPEN SOURCE  PYTHON LIBRARY USED FOR NUMERICAL AND SCIENTIFIC CALCULATING.
#IT PROVIDES SUPPORT FOR MULTIDIMENTIONAL ARRAY,MATRICES AND FUNCTIONS,MAKING THE CALCULATION
#FASTER AND EFFICIENT THAN STANDARD PYHTON LIST.
#1.The numpy array have a fixed size unlike python list whose size can be changed 
#2.the elements inside a numpy array should be of same data type

#2D
import numpy
a=np.array([[2,3,4],[4,5,6]])
print(a)



#3D 
import numpy as np 
a=np.array([[[1,2],[2,3]],[[5,6],[8,9]]])
print(a)



#dtype 
import numpy as mp
w=np.array([1,2,3],dtype=float)
print(w)



#Arange
np.arange(1,11)


np.arange(1,11,2)


#Reshape 
np.arange(1,11).reshape(2,5)

np.arannge(1,13).reshape(4,3)


#np.ones and np.zeros 
#Used for the fast initialization of the values.

np.ones((2,3))


np.zeros((2,5))




np.random.random((3,4)) #random numbers between 0 and 1, (0-1)


#Np.linspace
#np.linspace(start,end,how many numbers you want)
#give the number of numbers between the given range.

import numpy as np
print(np.linspace(4,10,10))
print(np.linspace(8,16,10))


np.identity(3)  #used to make a identity matrix in numpy array

# ------------------------------------------------------------------------------------------


import numpy as np
#ndim calculates the dimensions
a1=np.arange(0,11)
a2=np.arange(6).reshape(2,3)


# #shape 
a1.shape


#size gives total items
print(a2.size)


#item size --->>>> tells how much each item acquire the shape
a2.itemsize


#dtype----.tells the data type 
a2.dtype
a1.dtype




#CHANGING DATATYPES

a2.astype(np.int32) #reducing the space taken from int64------> to int 32..