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


# #item size --->>>> tells how much each item acquire the shape
# a2.itemsize


# #dtype----.tells the data type 
# a2.dtype
# a1.dtype




# #CHANGING DATATYPES

# a2.astype(np.int32) #reducing the space taken from int64------> to int 32..




#SCALAR OPERATIONS
import numpy as np
a1=np.arange(1,11).reshape(5,2)
a2=np.arange(12,24).reshape(3,4)

#arthimatic op
print(a1)
print(a1*2)
print(a1-2)
print(a1+4)

#relational operators
print(a2>5)
print(a2==6)

#VECTOR
#SAME  SHAPE OF TWO ARRAY THEN 
# a1+a2 can be performed and all things also


#Array functions
import numpy as np
n1=np.random.random((3,3))
n1=np.round(n1*100)
print(n1)

np.max(n1)
np.min(n1)
np.sum(n1)
np.prod(n1)



#row max
np.max(n1,axis=1) #riw wise


#column max
np.max(n1,axis=0)  #column wise



#MEAN
np.mean(n1)

#median
np.median(n1)


#variance
np.var(n1)


#trignometric funtions 
np.sin(n1)



np.cos(n1)




# DOT PRODUCT 
# Criteria for Dot Product
# 1. Two 1-D Arrays (Vectors)

# Both vectors must have the same number of elements.

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.dot(a, b))

# Output:

32

# Calculation:

# (1×4) + (2×5) + (3×6) = 32
# 2. Two 2-D Arrays (Matrices)

# Number of columns of the first matrix = Number of rows of the second matrix

# If A is (m × n) and B is (n × p), then:

# A · B = (m × p)

# Example:

# A = np.array([[1, 2],
#               [3, 4]])

# B = np.array([[5, 6],
#               [7, 8]])

# print(np.dot(A, B))

# Output:

# [[19 22]
#  [43 50]]
import numpy as np
a1=np.arange(1,13).reshape(3,4)
a2=np.arange(12,24).reshape(4,3)
print(a1)
print(a2)

print(np.dot(a1,a2))4

np.log(a1)



# #ROUND OFF TO THE NEAREST INTERGER
# np.round(np.random.random((3,3))*100)

# #FLOOR  -> rounds to previous interger
# np.floor(np.random.random((3,3))*100)

# np.ceil(np.random.random((3,3))*100)
# #ceil-> rounds to suceeeding interger











#-------------------------------------------------------------------------------------

#INDEXING AND SLICING 





import numpy as np

a1=np.arange(1,13)
a2=np.arange(12,24).reshape(4,3)
a3=np.arange(8).reshape(2,2,2)


# print(a1)


# print(a1[3])

# #FOR 2D
# print(a2)
# # print([row][column])
# print(a2[2][2]) #print 20
# print(a2[1][2]) #print 17


# #FOR 3D 
# print(a3)

# # [[[0 1]
# #   [2 3]]

# #  [[4 5]
# #   [6 7]]]

# # print([konse no. matrix me hai][row],[column])
# print(a3[1][0][1]) #prints 5
# print(a3[0][0][1]) #prints 1


# #Slicing
# print(a1[1:5:2])


#2D
# print(a2)
# # print(a2[:,1])


# print()
# print(a2[2:,0:2])

# a4=np.arange(12).reshape(3,4)
# print(a4)
# print(a4[1,::3])

# print(a4[0:2,1:])





# a5=np.arange(27).reshape(3,3,3)
# print(a5)
# print()
# print(a5[1][:][:])
# print(a5[0][1])

# print()
# print(a5[1,:,1])

#ITERATION
for i in a1:
    print(a1)

#2D   prints 2d arrays 
for i in a2:
    print(a2)

#3D
for i in a3:
    print(a3) #prints the 3-2d arrays

#To print the items of array 1 by 1 we use the nditer func.

for i in np.nditer(a3):
    print(i)



# #RESHAPING 
# #1.TRANSPOSE
# print(np.tranpose(a2)) 
# #or 
# a2.T  


# #RAVEL --> CONVERTS ANY DIMENSIONAL ARRAY TO THE 1 D ARRAY.
# print(a3.ravel)

#----------------------------------------------------------------------------------------
#STACKING
#shape should be same 
#HORIZONTAL STACKING
import numpy as np
a1=np.arange(12).reshape(3,4)
a2=np.arange(12,24).reshape(3,4)


#hstacking 

print(np.hstack((a1,a2,a1)))

#v stackin

print(np.vstack((a1,a2,a1)))
#------------------------------------------------------------------------------------------
#Horizontal spliting

np.hsplit(a2,2)  #splited in 2 equal halfs   dono dekhne me ulte hai okay.

np.vsplit(a2,2)  # splited in two halves . v