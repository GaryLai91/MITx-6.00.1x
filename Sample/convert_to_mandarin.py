# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 03:23:19 2017

@author: Gary
"""
trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
          
def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    # FILL IN YOUR CODE HERE
    x = int(us_num)
    if x <= 10:
        return trans[us_num]
    elif x > 10 and x < 20:
        word = trans['10'] + " "
        word += trans[us_num[1]]
        return word
    elif x % 10 == 0:
        word = trans[us_num[0]] + " " + trans['10']
        return word
    else:
        first = us_num[0]
        word = trans[first] + " " + trans['10'] + " "
        second = us_num[1]
        word += trans[second]
        return word