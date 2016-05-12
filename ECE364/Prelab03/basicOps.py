#! /usr/bin/env python3.4
#
# $Author: ee364c10 $:
# $Date: 2015-01-31 16:20:00 -0500 (Sat, 31 Jan 2015) $:
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364c10/Prelab03/basicOps.py $:
"""
Script samples for ECE 364.
"""

__version__ = '1.0.0'
__author__ = "Pranjit Kalita"
__date__ = '2015-January-30'

import os
import math
import sys

def addNumbers():
    #compute the sum of numbers between 0 and 1000
    sum_a = 0
    for i in range(0, 1001):
        #print i
        sum_a = sum_a + i    
    return sum_a
  
def addMultiplesOf(num):
    #compute the sum of multiples of num between 0 and 1000
    sum_m = 0
    max_m = (1000 / num)
    #print max_m
    for i in range(0, max_m + 1):
        tmp = i * num
        #print tmp
        sum_m = sum_m + tmp
    return sum_m
 
def getDigitalSum(string):
    #compute sum of digits of a string 
    number = int(string)
    #print number
    sum_dig = 0
    while (number != 0):
        digit = number % 10
        #print digit
        number = number / 10
        sum_dig = sum_dig + digit
    return sum_dig
 
def getNumberFrequency(num):
    #frequency of a digit in a string
    str_num = str(num)
    string = "The value of Pi is 3 . 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2 6 4 3 3 8 3 2 7 9 5 0 2 8 8 4 1 9 7 1 6 9 3 9 9 3 7 5 1 0 5 8 2 0 9 7 4 9 4 4 5 9 2 3 0 7 8 1 6 4 0 6 2 8 6 2 0 8 9 9 8 6 2 8 0 3 4 8 2 5 3 4 2 1 1 7 0 6 7 9 8 2 1 4 8 0 8 6 5 1 3 2 8 2 3 0 6 6 4 7 0 9 3 8 4 4 6 0 9 5 5 0 5 8 2 2 3 1 7 2 5 3 5 9 4 0 8 1 2 8 4 8 1"
    len_str = len(string)
    freq = 0
    #print len_str
    #print str_num
    for i in range(0, len_str):
        #print string[i]
        if str_num == string[i]:
            #print "yes"
            #print string[i]
            #print str_num      
            freq = freq + 1
    #print i
    return freq

def capitalizeMe(string):
    len_str = len(string)
    l = list(string)
    for i in range(0, len_str):
        if i == 0 or l[i - 1] == ' ' or i == (len_str - 1) or l[i + 1] == ' ':
            #print string[i]
            s = l[i].upper()
            l[i] = s
        if l[i].isalpha() == False:
            s = l[i - 1].upper()
            l[i - 1] = s
    string = ''.join(l)
    return string

def getSequenceWithoutDigit(num):
     strList = ["736925233695599303035509581762617623184956190649483967300203776387436934399982",

"943020914707361894793269276244518656023955905370512897816345542332011497599489",

"627842432748378803270141867695262118097500640514975588965029300486760520801049",

"153788541390942453169171998762894127722112946456829486028149318156024967788794",

"981377721622935943781100444806079767242927624951078415344642915084276452000204",

"276947069804177583220909702029165734725158290463091035903784297757265172087724",

"474095226716630600546971638794317119687348468873818665675127929857501636341131"] 
     list_len = len(strList)
     print list_len
     mapping = []
     for i in range(0, list_len):
         size = 0
         s = ''.join(strList[i])
         #print s
         for j in range(0, len(s)):
             #print j
             if s[j] != str(num):
                 size = size + 1
             else:
                 size = 0
         #print size
         mapping.append(size)
     #print "Now printing mapping contents"
     '''
     for i in range(0, list_len):
         print mapping[i]
     '''
     comp = mapping[0]
     #print comp
     ind = 0
     for k in range(1, list_len):
         #print comp
         if comp < mapping[k]:
             comp = mapping[k]
             ind = k
     #print ind
     string = ''.join(strList[ind])
     return string

if __name__ == "__main__":
    sum_a = addNumbers()
    print "The sum of 0 to 1000 inclusive both ends is: "
    print sum_a
    num = int(input("Enter a number whose multiple's sum is required:"))
    sum_m = addMultiplesOf(num)
    print "Sum of multiples is: "
    print sum_m
    sum_to_be_calc = raw_input("Enter a string with numbers whose digits' sum needs to be calculated: ")
    sum_digital = getDigitalSum(sum_to_be_calc)
    print "Sum of digits: "
    print sum_digital
    num_c = int(input("Enter a number whose frequency in the string is required:"))
    freq = getNumberFrequency(num_c)
    print "The frequency is: "
    print freq
    string = raw_input("Enter the string that needs to be capitalized selectively: ")
    string = capitalizeMe(string)
    print "The capitalized string is: "
    print string
    num_pattern = int(input("Enter a number whose whose longest streak within the list needs to be calculated:"))
    string_streak = getSequenceWithoutDigit(num_pattern)
    print "The string with the longest streak is: " 
    print string_streak

    

