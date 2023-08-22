# %%
# 1) Recursion
# Write a function that takes a number and returns the factorial of that number.

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(0))
print(factorial(5))


# Write a function that takes a number and returns the fibonacci of that number.
def fibonacci_recursive(n):
    if n<=1:
       return n 
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
print(fibonacci_recursive(10))
print(fibonacci_recursive(20))

# The most important thing to remember is the following law:
# Python + Recursion = https://youtu.be/31g0YE61PLQ
# (Stack Overflow Error) (Yes, this is where the website got its name from)
# Instead, use loops. They are much faster, more efficient and will not blow up
# in your face. Example:

def fibonacci_loop(n): # produces each element and keeps track and updates each element
    e1=0
    e2=1
    for i in range(0,n-1):
        e3=e1+e2
        e1=e2
        e2=e3
    return e3

print(fibonacci_recursive(10))
print(fibonacci_loop(10))

# This is still fast for 10 but if you try to calculate fibonacci(10000) you will see the difference. One will make your computer sound like a airplane then may crash when it runs out of juice (pun intended) and the other will be done in a second.
# %%
# 2) Lists/Tuples/Dictionaries

# Lists
# Create a list of 10 numbers from 0 to 9
my_list = [x for x in range(0,10)]
print(my_list)
# remove all even numbers from the list
rem_odd = [x for x in my_list if x%2!=0]
print(rem_odd)
# remove all odd numbers from the list
rem_even = [x for x in my_list if x%2==0]
print(rem_even)
# reverse the order of the elements in the list
rev = my_list[::-1]
print(rev)
# print the first 5 elements of the list
first = my_list[0:5]
print(first)

# 2-D Lists
# Create a 2-D list of 10 numbers from 0 to 9 
my_2d_list = [[1,2,3],[4,5,6],[7,8,9]] # Not sure if you wanted an automated one that takes the number of columns and rows in a nested for loop
row = 3
column = 3

# If I had 3 rows and 3 columns I assume only 9 elements can fit. I will make a 2D list from 1 to 9 instead. 
print(my_2d_list)
# Access the 3rd element of the 2nd row
element = my_2d_list[1][2]
print(element)
# %%
# Can you figure out how to make the disgusting mess that is recursive 
# fibonacci slightly less horrific using lists?


def fibonacci_list(n): #Similar to the loop but the elements are stored in a list
    e1=0
    e2=1
    f_list=[e1,e2]
    for i in range(0,n-1):
        e3=e1+e2
        f_list.append(e3)
        e1=e2
        e2=e3
    return f_list[n]

#print(fibonacci_list(35))
#print(fibonacci_recursive(35)) 
# A lot better but still not as fast as the loop version 
# source: Trust me bro 


# %%
# Tuples
# Just like lists but immutable (can't be changed)
# Won't waste time on them, the only notable difference is that you use () instead of [] when creating them. example:

tuples = (5,6,7,8)
# tuples[2] = 0 # This will give an error


# %%
# Dictionaries
# Associative arrays, key-value pairs
# If you have a lot of data and you want to access it quickly, use a dictionary
# This might sound a bit familiar, but won't waste time on 
# them, the only notable difference is that you use {} 
# instead of [] when creating them and you need to specify 
# the key when accessing them. example:

# Create a dictionary where the key is the name of the 
# person and the value is their age

dictionary = {'Joe Bidden': 80, 'Vladimir Putin': 70, 'Kim Jong-un': 39}
# NOTE that the names were chosen randomly. Any resemblance to actual persons, 
# dead or alive, is purely coincidental.

print(dictionary['Joe Bidden'])
print(dictionary['Vladimir Putin'])
print(dictionary['Kim Jong-un'])

# %%
# 3) Imports 

# First you need to install the package you want to use.

# Open the terminal and type: pip install UR PACKAGE NAME

# 2 ways to import stuff
# 1)
# Imagine my argumentation that proves that recursive functions are slower
# than the iterative version did not convince you. You want to try it yourself 
# by timing the runtime of each method for that you will need to import the 'time' function from the 'time' module 
# that deals with believe it or not, time.


# import Module  as your name 
# the as your name here is optional
import time as t

# reset the array
t1 = t.time()
fibonacci_list(500)
t2 = t.time()
print(t2-t1,' s')

t1 = t.time()
fibonacci_loop(500)
t2 = t.time()
print(t2-t1,' s')
# %%
# or if you want to import a specific function
# from Module import Function  as your name
# Again the as your name is optional
from time import time as tm

t1 = tm()
fibonacci_list(500)
t2 = tm()
print(t2-t1,' s')

t1 = tm()
fibonacci_loop(500)
t2 = tm()
print(t2-t1,' s')
# %%
# Read the File 'ReadFile.csv' and store the data in a 2-D list 
data_set=open('ReadFile.csv','r')
import numpy as np  # I am not sure if there is a way to do it manually, but that is usually how I do it 
data_2d_array=np.loadtxt(data_set,delimiter=',')#Since CSV stands for comma separted values 
#print(data_2d_array)
# Load the file

# %%
# Now write Files with the same data but as floats
data_2d_array_float=[[0]*len(data_2d_array[0])]*len(data_2d_array)
for i in range(0,len(data_2d_array)):
    for j in range(0,len(data_2d_array[0])):
        data_2d_array_float[i][j]=float(data_2d_array[i][j])

#print(data_2d_array_float)
# %%
import csv 
with open('ReadFile_float.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(data_2d_array_float)