from GA.DNA import *
from NN import *
import numpy as np

class Crtr():
    nuralnet = 0
    
    fitness = 0
    dna = []
    outt = []
    xloc ,yloc = 0, 0
    bulletlocx = 0
    bulletlocy = 0

    neuralarray = []
    synarray = []





    def __init__(self, dn, w):
       
       
       if(str(type(dn)) == "<class 'int'>"):
           self.nuralnet = NeuralNetwork(0.6,  0.01)
        
           self.yloc = 0
           self.xloc = 0
           self.bulletlocx = 0
           self.bulletlocy = 0
           for q in range(len(w) - 2):           
               self.nuralnet.addHL(w[q + 1], 'sig')

           self.nuralnet.addinN(w[0], 'sig')

        
           self.nuralnet.addoutN(w[len(w) - 1], 'sig')
        
           
           q = self.nuralnet.synToarr()
           self.synarray = q
           ww = self.nuralnet.NToarr()
           self.neuralarray = ww
           self.dna = DNA(q, ww)

       else:
           self.nuralnet = NeuralNetwork(0.6,  0.01)
           self.dna = dn
           self.yloc = 0
           self.xloc = 0
           self.bulletlocx = 0
           self.bulletlocy = 0
           
           for q in range(len(w) - 2):
               self.nuralnet.addHL(w[q + 1], 'sig')

           self.nuralnet.addinN(w[0], 'sig')
           self.nuralnet.addoutN(w[len(w) - 1], 'sig')

           
           self.nuralnet.arrTosyn(self.dna.genesS)

           self.synarray = self.dna.genesS
           self.neuralarray = self.nuralnet.NToarr()
   

    def calcFitness(self):
        pass


    
    def update(self,xx):
        t = 0.0
        maxV = 70.1
        
        #w1 = self.outt[0].Value
        #w2 = self.outt[1].Value
        w1 = self.think(xx)[0].Value
        #print(w1 , w2 )
        while(True):
            dx = w1 * maxV * np.cos((np.pi / 4)) * t 
            

            dy = 0.5 * (-9.8) * t * t  + t * np.sin(w1 * (np.pi / 4)) * maxV * w1
            t += 0.01
            
            if(t > 0):
                if(dy < self.bulletlocy):
                    self.bulletlocx = dx    
                    self.outt.clear
                    break
        return self.bulletlocx
        #print(self.bulletlocx)


    def think(self, xx):
        
        return (self.nuralnet.ForwardPropagate(xx / 501.63003585510256))