# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 03:07:53 2017

@author: Gary
"""
def calcList(L1):
    x = 0
    for i in L1:
        x += i
    return x

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    # Your code here
    longest_increase = []
    longest_decrease = []
    """
    find longest run for monotonically increasing
    """
    
    for i in range(len(L)):
        test_increase = []
        test_increase.append(L[i])
        for j in range(i+1,len(L)):
            if L[j] >= test_increase[len(test_increase) - 1]:
                test_increase.append(L[j])
            else:
                break
        if len(test_increase) > len(longest_increase):
            longest_increase = test_increase[:]

    """
    find longest run for monotonically decreasing
    """
    
    for i in range(len(L)):
        test_decrease = []
        test_decrease.append(L[i])
        for j in range(i+1,len(L)):
            if L[j] <= test_decrease[len(test_decrease) - 1]:
                test_decrease.append(L[j])
            else:
                break
        if len(test_decrease) > len(longest_decrease):
            longest_decrease = test_decrease[:]

    """
    calculate sum of the longest array as x
    return x
    """
    x = 0
    if len(longest_increase) > len(longest_decrease):
        x = calcList(longest_increase)
    elif len(longest_increase) < len(longest_decrease):
        x = calcList(longest_decrease)
    else:
        if L.index(longest_increase[0]) < L.index(longest_decrease[0]):
            x = calcList(longest_increase)
        else:
            x = calcList(longest_decrease)
    return x