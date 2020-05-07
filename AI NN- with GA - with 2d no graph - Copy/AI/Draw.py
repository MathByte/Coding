#from graphics import *









class Draw():
    win = 0
    width = 1000
    hight = 500
    NN = 0
    locations = []
    calcloc = []

    def __init__(self, n):
      
        self.NN = n
        self.win = GraphWin('draw',self.width,self.hight)
        self.win.setBackground('black')
        self.locations = []
   
    
    def start_calc(self):
        xoff = 0
        xoff = self.width / (len(self.NN.HiddenLayers) + 2)

        yoff = 0
        yoff = self.hight / (len(self.NN.InputLayer))

        xaxis = 0

        count = 0
        for x in range(len(self.NN.InputLayer)):
            self.locations.append([])
            self.locations[count].append(xoff  - xoff / 2)
            self.locations[count].append(yoff + yoff * x - yoff / 2)
            count += 1

        
        for x in range(len(self.NN.HiddenLayers)):
            xaxis += 1
            for y in range(len(self.NN.HiddenLayers[x])):
                yoff = self.hight / (len(self.NN.HiddenLayers[x]))
                self.locations.append([])
                self.locations[count].append(xoff + xaxis * xoff - xoff / 2)
                self.locations[count].append(yoff + yoff * y - yoff / 2)
                count += 1

        xaxis += 1
        for x in range(len(self.NN.OutputLayer)):
            yoff = self.hight / (len(self.NN.OutputLayer))
            self.locations.append([])
            self.locations[count].append(xoff + xaxis * xoff - xoff / 2)
            self.locations[count].append(yoff + yoff * x - yoff / 2)
            count += 1

    def draw_circuls(self):
        
        r = 0
        g = 0
        rt = []

        for x in range(len(self.NN.InputLayer)):
            rt.append(self.NN.InputLayer[x])
            


        for x in range(len(self.NN.HiddenLayers)):
            for y in range(len(self.NN.HiddenLayers[x])):
                rt.append(self.NN.HiddenLayers[x][y])
               
            
        for x in range(len(self.NN.OutputLayer)):
            rt.append(self.NN.OutputLayer[x])
           




        
        for x in range(len(self.locations)):
            pt = Point(self.locations[x][0], self.locations[x][1])
            cir = Circle(pt, 25)

            t = rt[x].Value * 100
            if(t > 0):

                g = int(t)
                r = 0
                if (g > 255):
                    g = 255
            else:
                r = (-1) * int(t)
                g = 0
                if(r > 255):
                    r = 255
            
            color = color_rgb(0, r, g)
            cir.setFill(color)
            cir.draw(self.win)

        del rt

    def calcLocations(self):

        c = 0
        self.calcloc.append([])

        for y in range(len(self.NN.InputLayer)):
            self.calcloc[0].append([])
            self.calcloc[0][y].append(self.locations[c][0])
            c += 1
                

              
        for z in range(len(self.NN.HiddenLayers)):
            self.calcloc.append([])           
            for x in range(len(self.NN.HiddenLayers[z])):
                self.calcloc[1 + z].append([])
                self.calcloc[1 + z][x].append(self.locations[c][0])
                c += 1

        self.calcloc.append([])  
        for y in range(len(self.NN.OutputLayer)):
            self.calcloc[1 + len(self.NN.HiddenLayers)].append([])
            self.calcloc[1 + len(self.NN.HiddenLayers)][y].append(self.locations[c][0])
            c += 1



        




        c = 0

        for y in range(len(self.NN.InputLayer)):
            self.calcloc[0][y].append(self.locations[c][1])
            c += 1
                

              
        for z in range(len(self.NN.HiddenLayers)):    
            for x in range(len(self.NN.HiddenLayers[z])):
                self.calcloc[1 + z][x].append(self.locations[c][1])
                c += 1


        for y in range(len(self.NN.OutputLayer)):

            self.calcloc[1 + len(self.NN.HiddenLayers)][y].append(self.locations[c][1])
            c += 1




    def draw_Lines(self):
        
        
        t  = 0
        r = 0
        g = 0
        for x in range(len(self.NN.InputLayer)):
            for y in range(len(self.NN.HiddenLayers[0])):
                p1x = self.calcloc[0][x][0]
                p2x = self.calcloc[1][y][0]

                p1y = self.calcloc[0][x][1]
                p2y = self.calcloc[1][y][1]
                t = self.NN.InputLayer[x].OutputSynapses[y].Weight * 100
                if(t > 0):
                    g = int(t)
                    r = 0
                    if (g > 255):
                        g = 255
                else:
                    r = (-1) * int(t)
                    g = 0
                    if(r > 255):
                        r = 255
              
                color = color_rgb(r, g, 0)
                p1 = Point(p1x, p1y)
                p2 = Point(p2x, p2y)
                lin = Line(p1, p2)
                lin.setFill(color)
                lin.setWidth(8)
                lin.draw(self.win)



        if(len(self.NN.HiddenLayers) > 1):
            for z in range(len(self.NN.HiddenLayers) - 1):
                for x in range(len(self.NN.HiddenLayers[z])):
                    for y in range(len(self.NN.HiddenLayers[z + 1])):
                        p1x = self.calcloc[1 + z][x][0]     
                        p2x = self.calcloc[1 + z + 1][y][0]    

                        p1y = self.calcloc[1 + z][x][1]   
                        p2y = self.calcloc[1 + z + 1][y][1]


                        t = self.NN.HiddenLayers[z][x].OutputSynapses[y].Weight * 100
                        if(t > 0):
                            g = int(t)
                            r = 0
                            if (g > 255):
                                g = 255
                        else:
                            r = (-1) * int(t)
                            g = 0
                            if(r > 255):
                                r = 255
                       
                        color = color_rgb(r, g, 0)
                      
                        p1 = Point(p1x, p1y)
                        p2 = Point(p2x, p2y)
                        lin = Line(p1, p2)
                        lin.setFill(color)
                        lin.setWidth(8)
                        lin.draw(self.win)
        






        for y in range(len(self.NN.OutputLayer)):
            for x in range(len(self.NN.HiddenLayers[len(self.NN.HiddenLayers) - 1])):
                p1x = self.calcloc[len(self.NN.HiddenLayers)][x][0]
                p2x = self.calcloc[len(self.NN.HiddenLayers) + 1][y][0]

                p1y = self.calcloc[len(self.NN.HiddenLayers)][x][1]
                p2y = self.calcloc[len(self.NN.HiddenLayers) + 1][y][1]
                t = self.NN.HiddenLayers[-1][x].OutputSynapses[y].Weight * 100
                if(t > 0):
                    g = int(t)
                    r = 0
                    if (g > 255):
                        g = 255
                else:
                    r = (-1) * int(t)
                    g = 0
                    if(r > 255):
                        r = 255
              
                color = color_rgb(r, g, 0)
                p1 = Point(p1x, p1y)
                p2 = Point(p2x, p2y)
                lin = Line(p1, p2)
                lin.setFill(color)
                lin.setWidth(8)
                lin.draw(self.win)