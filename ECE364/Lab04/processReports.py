#! /usr/bin/env python3.4
#
# $Author: ee364c10 $:
# $Date: 2015-02-11 11:24:10 -0500 (Wed, 11 Feb 2015) $:
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364c10/Lab04/processReports.py $:
import os
import math
import sys
import glob
def usrId():
    fn = "users.txt"
    f = open(fn, 'r')
    count = 0
    d = {}
    for lines in f:
        nm = [[]]
        if count == 0 or count == 1:
            count = count + 1
            continue
        else:
            #print type(lines)
            cont = lines.split()
            #print cont
            #cont = lines.strip(",""|")
            #print cont
            #cont = lines.
            fn = cont[1]
            #print fn
            ln = cont[0]
            #print ln
            id_num = cont[3]
            #print id_num
            f_n = fn + " " + ln
            f_n = f_n.strip(",")
            #print f_n
            #print id_num
            d.update({id_num:f_n})
    f.close()
    return d

def generateReportForAllUsers1():
    files = []
    files = (glob.glob("reports/*.txt"))
    #print files
      
    id_un_co = {}
    #un_mon = [[]]
    for i in range(0, len(files)):
        f = files[i]
        fh = open(f,'r')
        count  = 0
        units = 0
        cost = 0 
        ID = ""
        t = ()
        for lines in fh:
            if count == 0:
                cont = lines.split()
                #print len(cont)
                count = count + 1
                ID = cont[2]
                #print ID
            elif count in range(1,4):
                count = count + 1
            else:
                cont = lines.split()
                #print len(cont)
                #units = units + int(cont[2])
                un = cont[2]
                #print un
                units = units + int(un)
                mon = cont[3].strip("$")
                cost = cost + float(mon)
                #print mon
                #cost = cost + float(cont[3])
                #print units
                #print cost
                #un_mon[i].append(int(un), float(mon))
        t = (int(units),float(cost))
        #print t
        #print ID
        #now we have ID, tuple
        if ID in id_un_co:
            tup = id_un_co[ID]
            #print tup
            u_u = tup[0] + t[0]
            u_m = tup[1] + t[1]
            tupf = (u_u,u_m)
            id_un_co.update({ID:tupf})
        else:
            id_un_co.update({ID:t})
    #return id_un_co
    #print id_un_co
    userID = usrId()
    #compare betwn userID & id_un_co dictionaries
    f_d = {}
    for keys in userID:
        name = userID.get(keys)
        #print name
        v = id_un_co.get(keys)
        #print v
        f_d.update({name:v})
    return f_d
     

def generateReportForAllUsers():
    files = []
    files = (glob.glob("reports/*.txt"))
    #print files
      
    id_un_co = {}
    #un_mon = [[]]
    for i in range(0, len(files)):
        f = files[i]
        fh = open(f,'r')
        count  = 0
        units = 0
        cost = 0 
        ID = ""
        t = ()
        for lines in fh:
            if count == 0:
                cont = lines.split()
                #print len(cont)
                count = count + 1
                ID = cont[2]
                #print ID
            elif count in range(1,4):
                count = count + 1
            else:
                cont = lines.split()
                #print len(cont)
                #units = units + int(cont[2])
                un = cont[2]
                #print un
                units = units + int(un)
                mon = cont[3].strip("$")
                cost = cost + float(mon)
                #print mon
                #cost = cost + float(cont[3])
                #print units
                #print cost
                #un_mon[i].append(int(un), float(mon))
        t = (int(units),float(cost))
        #print t
        #print ID
        #now we have ID, tuple
        if ID in id_un_co:
            tup = id_un_co[ID]
            #print tup
            u_u = tup[0] + t[0]
            u_m = tup[1] + t[1]
            tupf = (u_u,u_m)
            id_un_co.update({ID:tupf})
        else:
            id_un_co.update({ID:t})
    #return id_un_co
    #print id_un_co
    userID = usrId()
    #compare betwn userID & id_un_co dictionaries
    f_d = {}
    for keys in userID:
        name = userID.get(keys)
        #print name
        v = id_un_co.get(keys)
        #print v
        if v is None:
            continue
        else:
            f_d.update({name:v})
            
    return f_d
     

def generateReportForAllViruses():
    files = []
    files = (glob.glob("reports/*.txt"))
    vir_un_co = {}
    for i in range(0, len(files)):
        f = files[i]
        fh = open(f,'r')
        count  = 0
        units = 0
        cost = 0 
        for lines in fh:
            if count == 0:
                count = count + 1
            elif count in range(1,4):
                count = count + 1
            else:
                cont = lines.split()
                #print cont
                un = cont[2]
                nm = cont[1]
                #print un
                units = units + int(un)
                mon = cont[3].strip("$")
                cost = cost + float(mon)
                t=()
                t=(int(units),float(cost))
                if nm in vir_un_co:
                    tup = vir_un_co[nm]
                    u_u = tup[0] + t[0]
                    u_m = tup[1] + t[1]
                    tupf = (u_u,u_m)
                    vir_un_co.update({nm:tupf})
                else:
                    vir_un_co.update({nm:t})
    #print vir_un_co
    return vir_un_co   
                

def getUsersWithoutReports():
    st = set()
    for keys in f_d_none:
        if f_d_none.get(keys) is None:
            st.add(keys)
    return st

def getTotalSpending():
    f_d = generateReportForAllUsers()
    tot = 0
    for keys in f_d:
        v = f_d.get(keys)
        #print v[1]
        tot = tot + float(v[1])
        #print tot
        
    return tot
          
if __name__ == "__main__":
    userId = usrId()
    #print userId
    f_d_none = generateReportForAllUsers1()
    #print f_d
    vir_un_co=generateReportForAllViruses()
    #print vir_un_co
    f_d = generateReportForAllUsers()
    #print f_d
    st = getUsersWithoutReports()
    #print st
    tot_sp = getTotalSpending()
    #print tot_sp
