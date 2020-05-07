import numpy as np
from scipy.stats import truncnorm
from Neuron import *
from Synapse import *
import math as mm


class NeuralNetwork(object):
    LearnRate = 0
    Momentum = 0
    InputLayer = []
    HiddenLayers = []
    OutputLayer = []
    d = 0
    done = 0

    arrSyn = []

    def __init__(self):
        self.Momentum = 0
        self.LearnRate = 0
        self.HiddenLayers = []
        self.InputLayer =  []
        self.OutputLayer = []



    def __init__(self, learnRate, momentum):
        self.LearnRate = learnRate
        self.momentum = momentum
        self.HiddenLayers = []
        self.InputLayer =  []
        self.OutputLayer = []

        """
        for x in range(inputSize):
            self.InputLayer.append(Neurone())
            
           

        for x in range(len(hiddenSizes)):
            self.HiddenLayers.append([])
            for y in range(hiddenSizes[x]):
                n = Neurone()
                self.HiddenLayers[x].append(n)

        for x in range(outputSize):
            self.OutputLayer.append(Neurone())
        """







        """

        if(len(self.HiddenLayers) > 1):
            for x in range(len(self.InputLayer)):
                for y in range(len(self.HiddenLayers[0])):
                    sy = Synapse()
                    sy.addINn(self.InputLayer[x])
                    sy.addOUTn(self.HiddenLayers[0][y])

                    self.HiddenLayers[0][y].InputSynapses.append(sy)
                    self.InputLayer[x].OutputSynapses.append(sy)
                
                    del sy
            trac  = 0
            x  = 0
            y =  0
            z = 0
            for t in range(10000):
                sy = Synapse()
                sy.addINn(self.HiddenLayers[x][y])
                sy.addOUTn(self.HiddenLayers[x + 1][z])
            

                self.HiddenLayers[x][y].OutputSynapses.append(sy)

                self.HiddenLayers[x + 1][z].InputSynapses.append(sy)
                del sy



                z = z + 1
                if (z == len(self.HiddenLayers[trac + 1])):
                    z = 0
                    y = y + 1
                    if(y  == len(self.HiddenLayers[trac])):
                        y = 0
                        z = 0
                        x = x + 1
                        trac = trac + 1
                        if(x == len(self.HiddenLayers) - 1):
                            x = 0
                            y = 0
                            z = 0
                            break

            for x in range(len(self.OutputLayer)):
                for y in range(len(self.HiddenLayers[len(self.HiddenLayers) - 1])):
                    sy = Synapse()
                    sy.addINn(self.HiddenLayers[len(self.HiddenLayers) - 1][y])
                    sy.addOUTn(self.OutputLayer[x])

                    self.HiddenLayers[len(self.HiddenLayers) - 1][y].OutputSynapses.append(sy)
                    self.OutputLayer[x].InputSynapses.append(sy)
                
                    del sy


        else:
            for x in range(len(self.InputLayer)):
                for y in range(len(self.HiddenLayers[0])):
                    sy = Synapse()
                    sy.addINn(self.InputLayer[x])
                    sy.addOUTn(self.HiddenLayers[0][y])

                    self.HiddenLayers[0][y].InputSynapses.append(sy)
                    self.InputLayer[x].OutputSynapses.append(sy)
                
                    del sy



            for x in range(len(self.OutputLayer)):
                for y in range(len(self.HiddenLayers[0])):
                    sy = Synapse()
                    sy.addINn(self.HiddenLayers[0][y])
                    sy.addOUTn(self.OutputLayer[x])

                    self.HiddenLayers[0][y].OutputSynapses.append(sy)
                    self.OutputLayer[x].InputSynapses.append(sy)
                
                    del sy

        """












    def addinN(self, x, s):
        for z in range(x):
            n = Neurone(s)
        


  
            for y in range(len(self.HiddenLayers[0])):
                sy = Synapse()

                sy.addINn(n)
                sy.addOUTn(self.HiddenLayers[0][y])
                n.OutputSynapses.append(sy)
                self.HiddenLayers[0][y].InputSynapses.append(sy)
            
                
                del sy

            self.InputLayer.append(n)

    def addoutN(self, x, s):
        for z in range(x):
            n = Neurone(s)
        


  
            for y in range(len(self.HiddenLayers[-1])):
                sy = Synapse()

                sy.addINn(self.HiddenLayers[-1][y])
                sy.addOUTn(n)
                n.InputSynapses.append(sy)
                self.HiddenLayers[-1][y].OutputSynapses.append(sy)
            
                
                del sy
            self.OutputLayer.append(n)



    def addHL(self, n, s):
        self.HiddenLayers.append([])
        
        for x in range(n):
            nnn = Neurone(s)
            self.HiddenLayers[-1].append(nnn)
            del nnn
                


        if(len(self.HiddenLayers) > 1):
            x = 0
            y = 0
            z = 0
            trac = 0
            while(True):
                sy = Synapse()
                sy.addINn(self.HiddenLayers[self.done + x][y])
                sy.addOUTn(self.HiddenLayers[self.done + x + 1][z])
            

                self.HiddenLayers[self.done + x][y].OutputSynapses.append(sy)

                self.HiddenLayers[self.done + x + 1][z].InputSynapses.append(sy)
                del sy



                z = z + 1
                if (z == len(self.HiddenLayers[self.done + trac + 1])):
                    z = 0
                    y = y + 1
                    if(y  == len(self.HiddenLayers[self.done + trac])):
                        y = 0
                        z = 0
                        x = x + 1
                        trac = trac + 1
                        if(self.done + x == len(self.HiddenLayers) - 1):
                            x = 0
                            y = 0
                            z = 0
                            self.done += 1
                            break




    def BackPropagate(self, targets):

        try:
            for x in range(len(self.OutputLayer)):
                
                if(len(self.OutputLayer) == 1):
                    self.OutputLayer[x].CalculateGradient(targets)
                else:
                    self.OutputLayer[x].CalculateGradient(targets[x])
                

           



            for x in range(1, len(self.HiddenLayers) + 1):
                for y in range(len(self.HiddenLayers[-x])):
                    self.HiddenLayers[-x][y].CalculateGradient()
           



            for x in range(1, len(self.HiddenLayers) + 1):
                for y in range(len(self.HiddenLayers[-x])):
                    self.HiddenLayers[-x][y].UpdateWeights(self.LearnRate, self.Momentum)




            for x in range(len(self.OutputLayer)):
                self.OutputLayer[x].UpdateWeights(self.LearnRate, self.Momentum)
                

        except:
            pass





        




    def ForwardPropagate(self, inputs):
        
       
        
        for x in range(len(self.InputLayer)):
            try:
                if(len(self.InputLayer) != 1):
                    self.InputLayer[x].Value = inputs[x]
                else:
                    self.InputLayer[x].Value = inputs
            except:
                self.InputLayer[x].Value = 0
            
        for x in range(len(self.HiddenLayers)):
            for y in range(len(self.HiddenLayers[x])):
                self.HiddenLayers[x][y].CalculateValue()

        for x in range(len(self.OutputLayer)):
            self.OutputLayer[x].CalculateValue()
        return self.OutputLayer


    def Compute(inputs):
        ForwardPropagate(inputs)
        z = []
        for x in range(len(self.OutputLayer)):
            z.append(self.OutputLayer[x].Value)
        return z




    def CalculateError(self, targets):
       
        self.s = 0
        for z in range(len(self.OutputLayer)):
            self.s = self.s + mm.fabs(self.OutputLayer[z].CalculateError(targets[z])) 
        return self.s



    



    def Train(self, dataSets, targetset, howmanytimes):
        
        for g in range(howmanytimes):
            #print(g)
          
            for x in range(len(dataSets)):
                self.ForwardPropagate(dataSets[x])
                self.BackPropagate(targetset[x])
                
            

    def set_D(self, a):
        self.d = a








    def synToarr(self):
        outsyns = []

        for x in range(len(self.InputLayer)):
            for y in range(len(self.InputLayer[x].OutputSynapses)):
                outsyns.append(self.InputLayer[x].OutputSynapses[y].Weight)


        for x in range(len(self.HiddenLayers)):
            for y in range(len(self.HiddenLayers[x])):
                for z in range(len(self.HiddenLayers[x][y].OutputSynapses)):
                    outsyns.append(self.HiddenLayers[x][y].OutputSynapses[z].Weight)

        self.arrSyn = outsyns
        return outsyns




    def arrTosyn(self, arr):
        
        ct = 0
        for x in range(len(self.InputLayer)):
            for y in range(len(self.InputLayer[x].OutputSynapses)):
                self.InputLayer[x].OutputSynapses[y].Weight = arr[ct]
                ct += 1


        for x in range(len(self.HiddenLayers)):
            for y in range(len(self.HiddenLayers[x])):
                for z in range(len(self.HiddenLayers[x][y].OutputSynapses)):
                    self.HiddenLayers[x][y].OutputSynapses[z].Weight = arr[ct]
                    ct += 1




    def NToarr(self):
        outsyns = []

        for x in range(len(self.InputLayer)):
            outsyns.append(self.InputLayer[x])


        for x in range(len(self.HiddenLayers)):
            for y in range(len(self.HiddenLayers[x])):
                outsyns.append(self.HiddenLayers[x][y])

        for x in range(len(self.OutputLayer)):
            outsyns.append(self.OutputLayer[x])

        self.arrSyn = outsyns
        return outsyns


    def arrToN(self, a):
        ct = 0

        for x in range(len(self.InputLayer)):
            self.InputLayer[x] = a[ct]
            ct += 1


        for x in range(len(self.HiddenLayers)):
            for y in range(len(self.HiddenLayers[x])):
                self.HiddenLayers[x][y] = a[ct]
                ct += 1

        for x in range(len(self.OutputLayer)):
            self.OutputLayer[x] = a[ct]
            ct += 1







    def ARRToBias(self, a):
        ct = 0
        """
        for x in range(len(self.InputLayer)):
            self.InputLayer[x].Bias = a[ct]
            ct += 1
        """

        for x in range(len(self.HiddenLayers)):
            for y in range(len(self.HiddenLayers[x])):
                self.HiddenLayers[x][y].Bias = a[ct]
                ct += 1

        for x in range(len(self.OutputLayer)):
            self.OutputLayer[x].Bias = a[ct]
            ct += 1


    def biasToARR(self):
        ct = 0
        arr = []
        for x in range(len(self.HiddenLayers)):
            for y in range(len(self.HiddenLayers[x])):
                arr.append(self.HiddenLayers[x][y].Bias)
            

        for x in range(len(self.OutputLayer)):
            arr.append(self.OutputLayer[x].Bias)
        return arr