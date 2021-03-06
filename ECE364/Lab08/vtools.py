#! /usr/bin/env python3.4
#
# $Author: ee364c10 $:
# $Date: 2015-03-24 15:29:26 -0400 (Tue, 24 Mar 2015) $:
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364c10/Lab08/vtools.py $:
import os
import math
import sys
import re

def is_valid_name(identifier):
    if re.search(r"^([\w]+)$", identifier):
        #print('Valid identifier')
        return True
    else:
        #print('Invalid Identifier')
        return False
#is_valid_name("part1")
#is_valid_name("hyp-hen")
def parse_pin_assignment(assignment):
     m = re.search(r"^\.(?P<wire>[\w]+)\((?P<pin>[\w]+)\)$", assignment)
     if m:
         tup = ()
         if (is_valid_name(m.group('wire')) and is_valid_name(m.group('pin'))):
             tup = (m.group('wire'), m.group('pin'))
         else:
             raise ValueError(assignment)
         return tup
     else:
         raise ValueError(assignment)
#tup = parse_pin_assignment("E(n30)")
#print(tup)
def parse_net(line):
     '''
     m_tmp = re.search(r"^(?P<comp_name>[\w]+)[ ]+(?P<inst_name>[\w]+)[ ]*\([ ]*(?P<asgnmt_tmp>[.*])[ ]*\)$", line)
     
     if m_tmp is not None:
         print(m_tmp.group('asgnmt_tmp'))
         as_tmp = m_tmp.group('asgnmt_tmp')
         print(as_tmp)
         if as_tmp is not None:
             lst_t = as_tmp.split(',')
             tot_assignments_t = len(lst_t)
             tup_lst_t = []
             for i in range(0, tot_assignments_t):
                 lst_t[i] = lst_t[i].strip(' ')
                 tup_lst_t.append(parse_pin_assignment(lst[i]))
     '''
     m = re.search(r"^(?P<comp_name>[\w]+)[ ]+(?P<inst_name>[\w]+)[ ]*\([ ]*(?P<asgnmt>[\w,.\(\) ]+)[ ]*\)$", line)
     if not m:
         #print('correct')
         raise ValueError(line)
     else:
         #print('correct')
         assignments = m.group('asgnmt')
         #print(assignments)
         lst = assignments.split(',')
         tot_assignments = len(lst)
         tup_lst = []
         for i in range(0, tot_assignments):
             lst[i] = lst[i].strip(' ')
             tup_lst.append(parse_pin_assignment(lst[i]))
             #print(lst[i] + ' passed')
         tup = tuple(tup_lst)
         #print(tup)
         l_f = []
         l_f.append(m.group('comp_name'))
         l_f.append(m.group('inst_name'))
         l_f.append(tup)
         #print(l_f)
         fin_tup = tuple(l_f)
         #print(fin_tup)
         return fin_tup

#line = "DFFSR present_val_reg ( .D(n30), .CLK(clk), .R(n33), .S(1), .Q(stop_bit) )"
#line="DFFSR Q_int1_reg ( .D(serial_in), .CLK(clk), .R(1), .S(n5), .Q(Q_int1) )"
#line="OAI22X1     U11(.A(n32),.B(n5),.C(n3),.D(n6),.Y(n25))"
#line="BAD(.A(n32),.B(n5),.C(n3),.D(n6),.Y(n25))"
#line=".A(n32),.B(n5),.C(n3),.D(n6),.Y(n25)"
#line="TEST TEST((.A(n32),.B(n5),.C(n3),.D(n6),.Y(n25)))"
#line="TEST $TEST(.A(n32),.B(n5),.C(n3),.D(n6),.Y(n25))"
#line="TEST TEST(.A(n32),.B(n5),.C(n3),.D(n6),.Y(n25)))"
#line="TEST TEST(.A(n32),.B(n5),.C(n3),.D(n6),.Y(n25)"
#tup_net = parse_net(line)
#print(tup_net)
