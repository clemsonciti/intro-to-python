# -*- coding: utf-8 -*-
"""
Created on Mon May 18 11:48:31 2020

@author: aantao
"""
#%%
#Code Block
#For Loops
word_list = ['Strawberry','Spam','eggs','Nicholas','cage', 'tigers']
for obj in word_list:
    print(obj)
    print(obj.upper())

print(obj.capitalize())

#%%
#Conditionals and Boolean Operations
x = 10  #Assignment operation
#if-else statements
if x == 4:            #Boolean Operation, comparing
    print("Value is equal to 4")
#else if
elif x < 4:
    print("Value is less than 4")
else:
    print("Value is greater than 4")
#%%
#Combine For Loops and if-else statements
number_list=[1,2,3,4,5,6,7,8,9]
    
for num in number_list:
    #print(num)
    if num == 4:
        #print(num)
        print("Value is equal to 4")
    elif num < 4:
        print("Value is less than 4")
    else:
        print(num)
        print("Value is greater than 4")
#%%
import fibonacci

print(fibonacci.fibo_range(6))        