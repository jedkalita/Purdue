#! /usr/local/bin/python3.4
#
# $Author: ee364c10 $:
# $Date: 2015-03-04 11:25:10 -0500 (Wed, 04 Mar 2015) $:
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364c10/Lab07/Laboratory.py $:

import os
import math
import sys
import re

class Experiment:
    def __init__(self, experimentNumber,experimentDate,virusName,unitCount,unitCost):
        self.experimentNumber = int(experimentNumber)
        self.experimentDate = experimentDate
        self.virusName = virusName
        self.unitCount = int(unitCount)
        self.unitCost = float(unitCost)
        self.totalCost = float(self.unitCount * self.unitCost)
    def __str__(self):
        e_num = "{0:03d}".format(self.experimentNumber)
        tot_cst = "{0:06.2f}".format(self.totalCost)
        ret_str = e_num + ", " + self.experimentDate + ", $" + tot_cst + ": " + self.virusName
        return ret_str

class Technician:
    def __init__(self, techName, techID):
        self.techName = techName
        self.techID = techID
        self.experiments = {}
    def addExperiment(self, experiment):
        if experiment.experimentNumber in self.experiments:
            self.experiments[experiment.experimentNumber] = experiment
        else:
            self.experiments.update({experiment.experimentNumber:experiment})
    def __str__(self):
        tot_expt = 0
        for key in self.experiments:
            tot_expt = tot_expt+1
        num = "{0:02d}".format(tot_expt)
        ret_str = self.techID + ", " + self.techName + ": " + str(num) + " Experiments"
        return ret_str
    def generateTechActivity(self):
        ret_str = self.techID + ", " + self.techName + "\n"
        #experiments_sorted = sorted(self.experiments)
        #print(experiment_sorted)ted(self
        sorted(self.experiments)
        for keys in self.experiments:
            string = str(self.experiments[keys])
            ret_str = ret_str + string + "\n"
        return ret_str
    def loadExperimentsFromFile(self, fileName):
        f = open(fileName, 'r')
        c = 0
        for lines in f:
            if c == 0 or c==1:
                c = c+1
                continue
            else:
                cnt = lines.split()
                e_num = cnt[0]
                e_date = cnt[1]
                vir = cnt[2]
                ucnt = cnt[3]
                ucst = cnt[4].split('$')[1]
                new_expt = Experiment(e_num,e_date,vir,ucnt,ucst)
                self.addExperiment(new_expt)

class Laboratory:
    def __init__(self, labName):
        self.labName = labName
        self.technicians = {}
    def addTechnician(self, technician):
        if technician.techName in self.technicians:
            self.technicians[technician.techName] = technician
        else:
            self.technicians.update({technician.techName:technician})
    def __str__(self):
        tot_tech = 0
        for keys in self.technicians:
            tot_tech = tot_tech + 1
        num = "{0:02d}".format(tot_tech)
        ret_str = self.labName + ": " + num + " Technicians"+"\n"
        for keys in self.technicians:
            string = str(self.technicians[keys])
            ret_str = ret_str + string + "\n"
        return ret_str
    def generateLabActivity(self):
        ret_str = ''
        #technician_sorted = sorted(self.technicians)
        sorted(self.technicians)
        for keys in self.technicians:
            string = self.technicians[keys].generateTechActivity()
            ret_str = ret_str + string
        return ret_str
'''
e1 = Experiment(31,'04/01/2015','xxx',4,25.79)
#print(str(e1))
e2 = Experiment(33,'03/01/2015','xuyx',17,76.79)
t1 = Technician('Pranjit Kalita', '69069-29232')
t1.addExperiment(e1)
t2 = Technician('JP McEnroe', '69089-29532')
t2.addExperiment(e2)
t3 = Technician('Audrey Land', '63689-20532')
#t.addExperiment(e2)
t1.loadExperimentsFromFile('report 69069-29232.txt')
t2.loadExperimentsFromFile('report 55926-36619.txt')
t3.loadExperimentsFromFile('report 75471-28954.txt')
#print(t1.generateTechActivity())
#print(str(t1))
#print(t2.generateTechActivity())
#print(str(t2))
l1 = Laboratory('RD Research')
l1.addTechnician(t1)
l1.addTechnician(t2)
l1.addTechnician(t3)
print(str(l1))
print(l1.generateLabActivity())
'''

        
    
