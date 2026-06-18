# #Iteration:Iteration is a general item for taking out something one by one .
# #Iterator:Iterator is a object that allow user to take out the data one by one from
# #the sequence without having to store the entire document in the memory.

# import sys
# sys.getsizeof() #-----> bytes
# #Used to calculate the amount of memory consumed by something 



# #What is iterable?
# #iterable is a object that can be iterated over.
# #means aaysa object jiske upper iteration ho skta hai.

# #'TRICK' TO CHECK IF A FUNCTION IS ITERATABLE OR NOT.
# #EXAMPLE->>1.
# a=2
# for i in a:
#     print(i)  #ERROR not iterable

# #OR   #2.
# dir(a) #__iter__ not present 
# #if there is "__iter__" is dir of a then it is iterable else not

# t=(1,2,3,4)
# dir(t) #__iter__  present.


#---------------------------------------------------------------------------------------
#TO CHECK FOR A OBJECT IS ITERATOR OR NOT.
#CHECK FOR DIR() THEN CHECK FOR __next__ AND __iter__

#""""HAR ITERABLE - ITERATOR NAHI HOTA PAR HHAR ITERATOR-- ITERABLE HOTA HAI"""""


#HOW FOR LOOP WORKS--->

num=[1,2,3]
#step 1:
#fetchs the iterator using the iter function.
num_iterator=iter(num)
#step 2:
#uses the next function to move ahead .
next(num_iterator)
next(num_iterator)
next(num_iterator)
next(num_iterator) # Until it throws an error.



#MAKING MY OWN FOR LOOP:
def My_own_for_loop(iterable): #it will get a iterable object  as input
    iterable_ka_iterator=iter(iterable) #fetching the iterator  of the  iterable object 

    while True:
        try:
            print(next(iterable_ka_iterator))
        except:
            break


a=[1,2,3,4]
b=[2,3,5]
My_own_for_loop(a)
My_own_for_loop(b)


#CREATING OWN RANGE FUNCTION

class mera_range:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return mera_range_iterator(self)


class mera_range_iterator:

    def __init__(self, iterable_obj):
        self.iterable = iterable_obj

    def __iter__(self):
        return self

    def __next__(self):

        if self.iterable.start >= self.iterable.end:
            raise StopIteration
        
        current=self.iterable.next
        self.iterable.start+=1
        return current