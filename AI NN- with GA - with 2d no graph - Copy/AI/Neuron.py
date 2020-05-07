from random import *
from Synapse import *
from FUNCTION import *
import numpy as np
from Draw import *

class Neurone():
	InputSynapses = []
	OutputSynapses = []
	Bias = 0
	BiasDelta = 0
	Gradient = 0
	Value = 0
	ccc = 0

	FunName = ''

	def __init__(self):
		self.InputSynapses = [] 
		self.OutputSynapses = [] 
		self.Bias = np.random.uniform(-1.0, 1.0)
		self.BiasDelta = np.random.uniform(-1.0, 1.0)

	def __init__(self, bb):
		self.FunName = bb
		self.InputSynapses = [] 
		self.OutputSynapses = [] 
		self.Bias = np.random.uniform(-1.0, 1.0)
		self.BiasDelta = np.random.uniform(-1.0, 1.0)



		

	def CalculateValue(self):
		self.sum = 0
		for x in range(len(self.InputSynapses)):
			self.sum = self.sum + self.InputSynapses[x].Weight * self.InputSynapses[x].INn.Value
		self.sum += self.Bias
		self.Value = FUNCTION.choose(self.FunName, self.sum)
	
		
		


		return self.Value


	def CalculateError(self, targettt):
		#print(self.Value, targettt)
		return  targettt - self.Value



	def CalculateGradient(self, targ = 'a'):
		if(targ == 'a'):
			self.sum = 0
			for x in range(len(self.OutputSynapses)):
				self.sum = self.sum + self.OutputSynapses[x].OUTn.Gradient * self.OutputSynapses[x].Weight


			self.Gradient = self.sum * FUNCTION.choose('d_' + self.FunName, self.Value)
			return self.Gradient


		self.Gradient = self.CalculateError(targ) * FUNCTION.choose('d_' + self.FunName, self.Value)
		
		return self.Gradient






	def UpdateWeights(self, LR, M):

		self.prevDelta = self.BiasDelta;
		self.BiasDelta = LR * self.Gradient;
		self.Bias += self.BiasDelta + M * self.prevDelta;

		for x in range(len(self.InputSynapses)):
			self.prevDelta = self.InputSynapses[x].WeightDelta
			self.InputSynapses[x].WeightDelta = LR * self.Gradient * self.InputSynapses[x].INn.Value
			self.InputSynapses[x].Weight += self.InputSynapses[x].WeightDelta + M * self.prevDelta;
			#print(self.InputSynapses[x].Weight)

			