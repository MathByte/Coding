from NN import * 
import numpy as np
from NN import *
from Draw import *
from threading import Thread
import time
from openpyxl import *
from GA.Population import *
from GA.Crtr import *
from GA.DNA import *
import GA.GeneticA as gaa
import numpy as np







maxV = 70.1

teta = 89


w2 = teta / 90
t = 0.01





datain = []
dataout = []


for xx in range(11):
    w2 = xx * 0.05
    while(True):
    
        dx = maxV * np.cos(w2 * (np.pi / 2)) * t 
        dy = 0.5 * (-9.8) * t * t  + t * np.sin(w2 * (np.pi / 2)) * maxV 
        t += 0.01

        #print(round(dx, 2), round(dy, 2))

        if(dy <= 0):
            datain.append(w2)
            dataout.append(dx / 501.63003585510256)
            break
                    
        
for xx in range(len(datain)):
    print(datain[xx], "  ", dataout[xx])




nn = NeuralNetwork(0.3,  0.01)

nn.addHL(4, 'sig')
nn.addHL(4, 'sig')



nn.addinN(1,'sig')
nn.addoutN(1,'sig')







nn.Train(datain, dataout, 10000)





for x in range(10):
    print(nn.ForwardPropagate(datain[x])[0].Value)