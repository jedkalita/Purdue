#! /usr/bin/env python3.4
#
# $Author: ee364c10 $:
# $Date: 2015-02-25 11:27:22 -0500 (Wed, 25 Feb 2015) $:
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364c10/Lab06/parse_xml.py $:
import os
import math
import sys
import re
import os.path

def convertToAttrib():
    f=open("points.xml", 'r')
    #i=0
    lst = []
    for lines in f:
        lst.append(lines.split())
    #print "size of lines:", len(lst)
    #print lst[30]
    f2 = open("points_out.xml", 'w')
    f2.write("<?xml version=\"1.0\"?>")
    f2.write("\n<coordinates>\n")
    for i in range(0,len(lst)):
        #print lst[i]
        
        if re.search(r"(<point>)", str(lst[i])):
            #print "point found in: ", i
            f2.write("   <point ID=")
            j=i+1
            y = ""
            x = ""
            ID2 = ""
            while not re.search(r"(</point>)", str(lst[j])):
                #print j
                if re.search(r"(<X>)", str(lst[j])):
                    x = str(lst[j+1])
                    #print x
                    x=x.replace("[","")
                    x=x.replace("]","")
                    x=x.replace("'","")
                    j=j+1 
                    continue
                var1 = re.search(r"(?P<beginID><ID>)(?P<ID>[\w]+)(?P<endID></ID>)", str(lst[j]))
                if re.search(r"(?P<beginID><ID>)(?P<ID>[\w]+)(?P<endID></ID>)", str(lst[j])):
                    #print j
                    ID2 = var1.group("ID")
                    '''
                    f2.write("\"")
                    f2.write(ID2)
                    f2.write("\" ")
                    '''
                    j=j+1
                    continue
                var2 = re.search(r"(?P<beginy><Y>)(?P<Yf>[\d+-.]+)(?P<endy></Y>)", str(lst[j]))
                if re.search(r"(?P<beginy><Y>)(?P<Yf>[\d+-.]+)(?P<endy></Y>)", str(lst[j])):
                    y= var2.group("Yf")
                    '''
                    f2.write("\"")
                    f2.write(y)
                    f2.write("\" ")
                    '''
                    j=j+1
                    continue
                j = j+1
            #print "X:", x
            f2.write("\"")
            f2.write(ID2)
            f2.write("\" ")
            f2.write("X = ")
            f2.write("\"")
            f2.write(str(x))
            f2.write("\" ")
            f2.write("Y = ")         
            f2.write("\"")
            f2.write(y)
            f2.write("\" ")
            f2.write(" />\n")
    f2.write("</coordinates>")
    f2.close()
    f.close()

def getGenres():
    f = open("books.xml", 'r')
    genres = []
    lst = []
    for lines in f:
        lst.append(lines.split())
    for i in range(0,len(lst)):
        var1 = re.search(r"(?P<genrebeg><genre>)(?P<gn>[\w]+)(?P<genreend></genre>)", str(lst[i]))
        if re.search(r"(?P<genrebeg><genre>)(?P<gn>[\w]+)(?P<genreend></genre>)", str(lst[i])):
            x = var1.group("gn")
            #x=x.replace("[","")
            #x=x.replace("]","")
            #x=x.replace("'","")
            genres.append(x)
    #out of for
    genres.sort()
    f.close()
    return genres

def getAuthorOf(bn):
    f = open("books.xml", 'r')
    lst = []
    for lines in f:
        lst.append(lines)
    for i in range(0,len(lst)):
        if re.search(r"(<title>)", str(lst[i])):
            #print("asdasd")
            var1 = re.search(r"<title>(?P<bnf>.*)</title>", str(lst[i]))
            #print(var1.group("bnf"))
            if var1.group(1) == bn: #found
                #print "jjdjd"
                #print var1.group("bnf")
                author = ""
                j=i-1
                var2 = re.search(r"(?P<au1><author>)(?P<auf>.*)(?P<au2></author>)", str(lst[j]))
                author = var2.group("auf")
                #print author
                f.close()
                return author
def getBookInfo(bookID):
    f = open("books.xml", 'r')
    lst = []
    t = ()
    for lines in f:
        lst.append(lines.strip())
    for i in range(0,len(lst)):
        if re.search(r"(<book id=)", str(lst[i])):
            var1 = re.search(r"(book id=\")(?P<bid>.*)(\")", str(lst[i]))
            #print "kkkk"
            if var1.group("bid") == bookID:
                #print "jfjf"
                author = ""
                title = ""
                var2 = re.search(r"(?P<au1><author>)(?P<auf>.*)(?P<au2></author>)", str(lst[i+1]))
                var3 = re.search(r"(?P<t1><title>)(?P<ti>.*)(?P<t2></title>)", str(lst[i+2]))
                author = var2.group("auf")
                title = var3.group("ti")
                t = (str(title),str(author))
                return t
                        
if __name__ == "__main__":
    convertToAttrib()
    g = getGenres()
    #print g
    bn = "Visual Studio 7: A Comprehensive Guide"
    aut = getAuthorOf(bn)
    #print aut
    t = ()
    bookID = "bk112"
    t = getBookInfo(bookID)
    #print t
