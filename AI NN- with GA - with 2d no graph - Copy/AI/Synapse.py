import Neuron
from random import *
import numpy as np

class Synapse():
    Weight = 0
    OUTn = 0
    INn = 0
    WeightDelta = 0


    def __init__(self):
        self.INn = 0
        self.OUTn = 0
        self.Weight = np.random.uniform(-1.0, 1.0)
        self.WeightDelta = np.random.uniform(-1.0, 1.0)
        
    def addINn(self, inn):
        self.INn = inn


    def addOUTn(self, outt):
        self.OUTn = outt