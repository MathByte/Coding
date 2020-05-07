import numpy as np
import imp
import sys as os
from GA.DNA import *
import importlib.util
from GA.Crtr import *


class Population(object):
    creaturs = []
    popsize = 0
    matingpool = []
  

    def __init__(self, popsize, net):
        self.popsize = popsize
        self.creaturs = []
        self.matingpool = []
   

        for i in range(popsize):
            self.creaturs.append(Crtr(net))
    
  

    def evaluate(self):
        avgfit = 0
        maxfit = 0
        for creatur in self.creaturs:
            creatur.calcFitness();
            if (creatur.fitness > maxfit):
                maxfit = creatur.fitness;
      
            avgfit += creatur.fitness
    
        avgfit /= len(self.creaturs)

        for creatur in self.creaturs:
            creatur.fitness /= maxfit
    

        self.matingpool = []

        for creatur in self.creaturs:
            n = int(creatur.fitness * 100)
            for x in range(5):
                self.matingpool.append(creatur)
      
    

        return avgfit
  

    def radom(self, c):
        r = (int)(np.random.random() * (len(c)))
        return c[r]
  

    def selection(self, vv):
        newcreaturs = []
        for i in range(len(self.creaturs)):
            parentA = self.radom(self.matingpool).dna
            parentB = self.radom(self.matingpool).dna
            child = parentA.crossover(parentB)
            child.mutation()
            Crtr = vv.Crtr
            newcreaturs.append(Crtr(child))
        self.creaturs.clear
        self.creaturs = newcreaturs
       
  

    def run(self):
        for creatur in self.creaturs:
            creatur.update()
            creatur.show()



    def importfile(self, modname):
        
        from os.path import dirname, abspath, join
        import sys

        # Find code directory relative to our directory
        THIS_DIR = dirname(__file__)
        CODE_DIR = abspath(THIS_DIR)
        sys.path.append(CODE_DIR)
        z = importlib.import_module(modname)
       
        return z
        
     