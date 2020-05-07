


import numpy as np


class DNA(object):

    lifespan = 400
    genesS = []
    genesB = []

   

    def __init__(self, s, n):
        self.genesS = s
        self.genesB = n
    

  
    def mutation(self, rate):
        for i in range(len(self.genesS)):
            if (np.random.random() < rate):
                self.genesS[i] *= np.random.random()
                #gene.setMag(maxforce);    
                #self.genes[i] = gene
        for i in range(len(self.genesB)):
            if (np.random.random() < rate):            
                #gene.setMag(maxforce);    
                self.genesB[i].Bias *= np.random.random()
                


    def crossover(self, rate):
        


        
        for i in range(len(self.genesS)):
            if (np.random.random() < rate):
                mid1 = np.random.randint(len(self.genesS))
                mid2 = np.random.randint(len(self.genesS))
                if(mid1 != mid2):
                    z = self.genesS[mid2]
                    self.genesS[mid2] = self.genesS[mid1]
                    self.genesS[mid1] = z


        for i in range(len(self.genesB)):
            if (np.random.random() < rate):
                mid1 = np.random.randint(len(self.genesB))
                mid2 = np.random.randint(len(self.genesB))
                if(mid1 != mid2):
                    z = self.genesB[mid2]
                    self.genesB[mid2] = self.genesB[mid1]
                    self.genesB[mid1] = z
     
        #return DNA(newgenes)
        
    










