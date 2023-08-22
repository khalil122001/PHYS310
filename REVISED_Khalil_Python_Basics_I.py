# %%
a = 56
b = 11
# 1) Basic Operations
# Addition +
# Subtraction -
# Multiplication *
# Division /
# Integer Division //
ans = a // b
print('Integer Division: ', ans)

# Modulo %
ans = a%b
print('Modulo: ', ans)

# Exponentiation **
# square one of the variables
''' 
Note that a ^ b  will run but give you the wrong results. 
In python the ^ operator does not exponentiate like a normal person would expect it to, instead it does a bitwise XOR (if you do not know what that means its not very important and you will probably never use it in this course... neither in the rest of your life)
'''
ans = b**2
print('Exponentiation: ', ans)
# %%
# 2) Loops

''' 
a) Using only one for loop, draw the following shape:

size = 5
*
**
***
****
*****

b) Using two for loops, draw the following shape:
(if you'r feeling adventurous try doing it with 1 for loop)

size = 5
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********
c) Using a while loop brute force trying to find the square root of a perfect square and print it. If the number is not a perfect square, print 'square root not found'.
'''
# a)
size = 5
# Fill in the code here
# i=1 (this was another idea I had, forgot to remove the i)
for i in range(1,size+1) : # since range stops at the last_digit-1
    print('*'*i) 

# b)
print('\n')
size = 5
# Fill in the code here 
for i in range(-size, size+1): # iterating from -5 to 5 and skipping 0 and 1 to avoid repetition of the single *
    if (i!=0) and (i!=1) :
        i=abs(i) 
        #for j in range(0, size-i):
        print(' '*(size-i), end="") #print an empty space each iteration and then reversing it once the positive numbers are reached   
        #for j in range(0, 2*i-1):
        print('*'*(2*i-1), end="") #printing 1,3,5,7,9 * each time
        print() #skipping a line 

# c)
print('\n')
'''
input_Value = 1
# Fill in the code here
i = 0 
while i*i <= input_Value:
    i=i+1
    if i*i == input_Value:
        print('The number is a perfect squaure with square root: ', i )
        break 
    if (i >=  (input_Value/2)): # since the square root will always be less than or equal to half the original value 
        print ('The number is not a perfect square')
'''
# NEW CODE:
input_Value = 0
# Fill in the code here
i = 1 
if input_Value != 0:
    while i*i <= input_Value:
        condition = False
        if (input_Value%i ==0) and (input_Value/i == i):
            condition = True 
            break
        i=i+1
    if condition:
        print('The number is a perfect square of square root: ', i )
    else:
        print('The number is NOT a perfect square.')
else:
    print('The number is a perfect square of square root: ', 0 )
# I had to start i from 0 rather than 1,
# %%

# 3) Functions 
#  Write a function that takes a String and checks if it is a palindrome or 
# not. (a palindrome is a word that is read the same left to right and right to left i.e.: 'civic', 'anna' and '1001001' are palindromes but 'car' is not ) 

# Fill in the code here
# The function will strip each input into its individual elements and put them into an array. It then puts the elements in an inverted order in another array.
# if the arrays are different, it changes the boolean condition to false. 
def isPalindrome(x):
    #condition = True 
    reverse_str=x[::-1]
    '''
    array=[0] * len(x)
    array_flipped=[0] * len(x)
    for i in range(0,len(x)-1):
        array[i]=x[i]
        array_flipped[i]=x[len(x)-1-i]
    
    for i in range(0,len(x)):
        if array[i] != array_flipped[i]:
            condition = False
    '''
    if x == reverse_str:
        print('The string is indeed a palindrome')
    else:
        print('The string is NOT a palindrome')
print('\n')
isPalindrome('anna')
isPalindrome('Khalil')
