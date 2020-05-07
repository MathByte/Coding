import math
import numpy as np



class  FUNCTION():



    sd = 8


    def __init__(self):
        pass
    
  




    def Sigmoid(x):
        if(x < -45.0):
            return 0.0
        if(x > 45.0):
            return 1.0
        return 1.0 / (1.0 + math.exp(-x))

       
    def DERSigmoid(x):
        return x * (1 - x)








    def TNG(x):
        return np.math.tanh(x)

    def DERTNG(x):
        return 1 - TNG(x) * TNG(x)






    def BinaryStep(x):
        if(x < 0):
            return 0
        else:
            return 1

    def DERBinaryStep(x):
        return 0
            
        







    def Lineaar(a, x):
        return a * x

    def DERLineaar(a, x):
        return a







    
    def ReLU(x):
        if(x > 0):
            return 0.1*x
        else:
            return 0


    def DERReLU(x):
        if(x > 0):
            return 1
        else:
            return 0.01








    def choose(x, v):
      if(x == "sig"):
          g = FUNCTION.Sigmoid(v)
          return g

      if(x == "d_sig"):
          g = FUNCTION.DERSigmoid(v)
          return g




      if(x == "bin"):
          g = FUNCTION.BinaryStep(v)
          return g

      if(x == "d_bin"):
          g = FUNCTION.DERBinaryStep(v)
          return g





      if(x == "lin"):
          g = FUNCTION.Lineaar(1, v)
          return g

      if(x == "d_lin"):
          g = FUNCTION.DERLineaar(1, v)
          return g






      if(x == "rul"):
          g = FUNCTION.ReLU(v)
          return g
      if(x == "d_rul"):
         g = FUNCTION.DERReLU(v)
         return g



      if(x == "tng"):
         g = FUNCTION.TNG(v)
         return g
      if(x == "d_tng"):
         g = FUNCTION.DERTNG(v)
         return g