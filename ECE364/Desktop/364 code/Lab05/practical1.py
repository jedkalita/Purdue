#! /usr/bin/env python3.4
#
# $Author: ee364c10 $:
# $Date: 2015-02-18 10:47:10 -0500 (Wed, 18 Feb 2015) $:
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364c10/Lab05/practical1.py $:
import os
import math
import sys
import glob
ls = []
pd={}
def find_h(ls):
    t = ()
    prod = 0
    four_num=[]
    row=0
    for i in range(0, len(ls)):
        #print ls[i][2]
        for j in range(0,17):
            st = j
            end = j+3
            product = int(ls[i][j])*int(ls[i][j+1])*int(ls[i][j+2])*int(ls[i][j+3])
            if product > prod:
                prod = product
                four_num = ls[i][j:j+4]
                t=(four_num,prod,'H')
                row=i
            else:
                continue
    #print row
    return t        

def find_v(ls):
    t = ()
    prod = 0
    four_num=[]
    col=0
    for i in range(0, 20):
        #print ls[i][2]
        for j in range(0,17):
            st = j
            end = j+3
            product = int(ls[j][i])*int(ls[j+1][i])*int(ls[j+2][i])*int(ls[j+3][i])
            if product > prod:
                prod = product
                four_num = ls[j][i] + "," + ls[j+1][i] + "," + ls[j+2][i] + "," + ls[j+3][i] + ","
                t=(four_num,prod,'V')
                col=i
            else:
                continue
    #print col
    return t

def getDirectory(f2):
    #pd={}
    for lines in f2:
        #print lines
        cont = lines.split()
        #print cont
        list_each=[]
        fn=cont[0]
        mi=cont[1]
        ln=cont[2]
        phone=cont[3]+cont[4]
        name=()
        list_each.append(fn)
        list_each.append(mi)
        list_each.append(ln)
        #print list_each
        name = tuple(list_each)
        #name
        pd.update({name:phone})
    return pd

def getLargestProduct():
    t = find_h(ls)
    print "Highest horizontally: ", t
    t2 = find_v(ls)
    print "Highest vertically: ", t2

def getPhoneByPartialName(partialName):
    #print pd
    list_pn=[]
    for keys in pd:
        cont=keys
        #print keys
        fn=cont[0]
        ln=cont[2]
        #print type(fn)
        #print type(ln)
        if fn == partialName or ln == partialName:
            list_pn.append(pd.get(keys))
            #print partialName
            #print fn
            #print ln
            #print pd.get(keys)
            #print list_pn
        else:
            continue
    return list_pn

def reverseLookup(areaCode):
    list_n = []
    for keys in pd:
        v = pd.get(keys)
        #print v
        comp = v[1:4]
        if comp == areaCode:
            list_n.append(keys)
        else:
            continue
    return list_n

if __name__ == "__main__":
    #list_pn=getPhoneByPartialName("Gloria")
    #print list_pn
    f = open("Number Grid.txt", 'r')
    i = 0  
    for lines in f:
        #print lines.split()
        #print lines
        ls.append(lines.split())
        i=i+1
    #for j in range(0,len(ls)):
    #    print ls[j]
    #print len(ls)
    #print len(ls[2])
    #now the function for horizontal
    getLargestProduct()
    f.close()
    f2=open("Phone Directory.txt",'r')
    #list_pn=getPhoneByPartialName("Gloria")
    #print list_pn
    pd=getDirectory(f2)
    #print pd
    list_pn=getPhoneByPartialName("Gloria")
    #print list_pn
    list_pn2=getPhoneByPartialName("Clark")
    #print list_pn2
    list_n=reverseLookup("999")
    #print list_n
    list_n2=reverseLookup("636")
    #print list_n2
    list_n3=reverseLookup("510")
    #print list_n3
