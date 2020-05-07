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

from NN import *






"""





data = [0,2,4,6,8,10]
out = [0,4,16,36,64,100]


#data = [[0,0],[0,1],[1,0],[1,1]]
#out = [1,0,0,1]


n = NeuralNetwork(0.6,0.1)

n.addHL(10,'sig')
n.addHL(10,'sig')

n.addHL(10,'sig')




n.addinN(1,'sig')

n.addoutN(1,'sig')


out = [ a/100 for a in out]
n.Train(data,out,10000)





for x in range(len(data)):
    print(x * 2, n.ForwardPropagate(data[x])[0].Value*100)




print("")



data = [1,3,5,7,9]
out = [1,9,25,49,81]


nm = NeuralNetwork(0.6,0.01)

nm.addHL(10,'sig')
nm.addHL(10,'sig')
nm.addHL(10,'sig')

nm.addinN(1,'sig')

nm.addoutN(1,'lin')


out = [ a/100 for a in out]

nm.Train(data,out,10000)





for x in range(len(data)):
    print(nm.ForwardPropagate(data[x])[0].Value*100)





print("")
syn = n.synToarr()
synm = nm.synToarr()
bian = n.biasToARR()
biam = nm.biasToARR()
v = []
for z in range(len(syn)):
    v.append((syn[z] + synm[z])/2)

w = []
for z in range(len(bian)):
    w.append((bian[z] + biam[z])/2)



tn = NeuralNetwork(0.6,0.01)

tn.addHL(10,'sig')
tn.addHL(10,'sig')
tn.addHL(10,'sig')

tn.addinN(1,'sig')

tn.addoutN(1,'lin')



tn.arrTosyn(v)
tn.ARRToBias(w)

datas = [0,1,2,3,4,5,6,7,8,9,10]

for x in range(len(datas)):
    print(tn.ForwardPropagate(datas[x])[0].Value * 100)








"""


























ga = gaa.GeneticAlgorithm([1,4,1], 50,100,0.4,0.3, True, True)

def fitness(individual, foodloc):
    return np.abs(individual.bulletlocx - foodloc)
    #return np.abs(individual.bulletlocx - foodloc)  / 501.63003585510256


def mutation(offspring, mrr):
    #@ mutate some 'bias' information of the offspring neurons
    b = []
    w = []
    for  i in range(len(offspring.neuralarray) - 1):
        b.append(mutate(offspring.neuralarray[i].Bias, mrr))




    #// mutate some 'weights' information of the offspring connections
    for  i in range(len(offspring.synarray)):
        w.append(mutate(offspring.synarray[i], mrr))
    offspring.dna.mutation(mrr)
    return b, w




def mutate(gene, mr):
    if (np.random.random() < mr):
        #mutateFactor = 1 + ((np.random.random() - 0.5) * 3 + (np.random.random() - 0.5))
        #gene *= mutateFactor
        
        gene += 2 * np.random.random() - 1
        return gene
    else:
        return gene
    

def selecstion(pop):
    q = np.random.randint(0, 5)
    return pop[q]
    



def crossver(parentA, parentB):
    cutPoint = np.random.randint(0, len(parentA.neuralarray)-1)


    for i in range(len(parentA.neuralarray) - 1):
        if i < cutPoint:
            #biasFromParentA = parentA.neuralarray[i].Bias
            #parentA.neuralarray[i].Bias = parentB.neuralarray[i].Bias
            #parentB.neuralarray[i].Bias = biasFromParentA
            parentA.neuralarray[i].Bias = parentB.neuralarray[i].Bias
            
            
        else:
            #biasFromParentA = parentA.neuralarray[i].Bias
            #parentA.neuralarray[i].Bias = parentB.neuralarray[i].Bias
            #parentB.neuralarray[i].Bias = biasFromParentA
            parentB.neuralarray[i].Bias = parentA.neuralarray[i].Bias



    cutPoint = np.random.randint(0, len(parentA.synarray)-1)
    for i in range(len(parentA.synarray) - 1):
        #biasFromParentA = parentA.synarray[i]
        #parentA.synarray[i] = parentB.synarray[i]
        #parentB.synarray[i] = biasFromParentA
        if i < cutPoint:
            parentA.synarray[i] = parentB.synarray[i]
        else:
            parentB.synarray[i] = parentA.synarray[i]





    parentA.dna.crossover(0.2)
    parentB.dna.crossover(0.2)
    if np.random.randint(0, 2) == 1:
        return parentA
    else:
        return parentB
      




ga.mutate_function = mutation
ga.fitness_function = fitness
ga.selection_function = selecstion
ga.crossover_function = crossver

ga.run()






crtr = ga.current_generation[0]
t = 0.01
bloc = 1

while True:

       print(bloc, crtr.update(bloc))
       bloc += 20
       if bloc > 500:
           break

