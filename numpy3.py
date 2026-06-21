import numpy as np
a=np.random.randint(1,100,15)

b=np.random.randint(1,100,24).reshape(4,6)

print((np.sort(a)))

print(np.sort(b,axis=1)) #for column
print(np.sort(a,axis=0)) #for row  sorting

print(np.sort(a)[::-1]) #for decending order sorting


#np.append

np.append(a,200)

np.append(b,np.random.random(b.shape([0],1)),axis=1)
#append a column at the last of b.

c=np.arange(6).reshape(2,3)
d=np.arange(6,12).reshape(2,3)

np.concatenate(c,d,axis=0) #row wise concatenation
np.concatenate(c,d,axis=1) #column wise concatenation



#np.unique
e=np.array([1,1,1,3,3,4,5,6,7,7,8,9,9,9])
np.unique(e)    


#np.expand_dims: with the help of this method we can expand the dimensions of ann array

a1=np.random.randint(1,100,15)
np.expand_dims(a1,axis=1)
#mainly used in ML where a ml model want a 2d input but we have 1d to give so we tranform to 2d with np.expand_dims()
#to convert to 2d or more to give to the model


#np.where : returns the indices of the elements where the given condition is satisfied 
np.where(a1>50)


#np.where(condition,true hua toh, false hua toh)
np.where(a1>50,0,1)

#if condition true repplace with 0 else with 1

np.where(a%2==0,0,1) #replace the even with 1s and odd with 1



#np.arg_max():give the index(position) of the largest element
np.argmax(a1)
np.argmax(b,axis=0) #row wise maximum
np.argmax(b,axis=1) #column wise



#cumsum and cumprod
np.cumsum(b,axis=1)
np.cumprod(b)
np.cumprod(b,axis=0)


#percenntile
import numpy as np
per=np.array([1,5,7,89,67,87,99,45])
print(np.percentile(per,100))

#NUMPY.HISTOGRAM is a function which represents a frequency if data distribution in graphical form.

array=np.array([56,78,90,89,67,199,34,56,86,23,45,67,43,21,78,95,47,89])
bin=np.histogram(array,bins=[0,10,20,30,40,50,70,100,200])
print(bin)

#corelation coefficient

salary=np.array([20000,30000,40000])
exp=np.array([1,2,3])

np.corrcoef(salary,exp)


#np.isin to search the multiple items.
import numpy as np

w=np.array([56,78,90,89,67,199,34,56,86,23,45,67,43,21,78,95,47,89])
items=np.array([34.67,90,56])
print(w[np.isin(w,items)])

#np.put
# the numpy.put function replaces specific elements of an array with given values of p_array
np.put(w,[0,1],[110,890])
# np.put(array,[index positions],[items])

#Set functions


n=np.array([1,2,3,4,5])
m=np.array([3,4,5,7,8])



np.union1d(m,n) #calculates the union


np.intersect1d(n,m)



np.setdiff1d(n,m)


np.setxor1d(n,m)




#np.clip : use dto clip(limit ) the values in an array.

w=np.array([56,78,90,89,67,199,34,56,86,23,45,67,43,21,78,95,47,89])

np.clip(w,w_min=50,w_max=100)
#now all the values will be the 50 and 100
