# -*- coding: utf-8 -*-
"""
Created on Mon May 18 12:22:28 2020

@author: aantao
"""
##0,1,1,2,3,5,8
##n = n-1 + n-2
def fibo_range(n = 10):
    fibo_list = [0,1]
    for i in range(2,n):
        fibo_list.append(fibo_list[i-1]+fibo_list[i-2])
    return(fibo_list,fibo_list[n-1])

#Why n-1 and not n in fibo_list[n-1] ?