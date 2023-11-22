import copy
from PIL import Image
from classes.File import File

class MathematicalMorphology:
    originalImage: File
    changedImage: File

    def __init__(self, originalImage, changedImage):
        self.originalImage = originalImage
        self.changedImage = changedImage
        self.changedImage.setFile(self.originalImage.getFile())

    def dilation(self):
        changedImageMap = self.changedImage.convertImageToMap()

        for y in range(1, self.changedImage.getHeight()-2):
            for x in range(1, self.changedImage.getWidth()-2):

                red = 0
                greem = 0
                blue = 0

                for i in range(3):
                    for j in range(3):
                        r, g, b, p = self.originalImage.image.getpixel((x+(i-1),  y+(j-1)))
                        
                        if (r > red):
                            red = r
                            greem = g
                            blue = b
                
                if ((red+greem+blue)/3 > 128):

                    if(red+10 < 255): red = red + 10 
                    else: red = 255
                    if(greem+10 < 255): greem = greem + 10 
                    else: greem = 255
                    if(blue+10 < 255): blue = blue + 10 
                    else: blue = 255

                    for i in range(3):
                        for j in range(3):
                            changedImageMap[x+(i-1), y+(j-1)] = red, greem, blue
        
        self.changedImage.image.save("attachment/dilation." + self.changedImage.getExtencial(),
                                     format=self.originalImage.image.format)
        self.changedImage.setFile("attachment/dilation." + self.changedImage.getExtencial())
        return self.changedImage
    
    def erosion(self):
        changedImageMap = self.changedImage.convertImageToMap()

        for y in range(1, self.changedImage.getHeight()-2):
            for x in range(1, self.changedImage.getWidth()-2):

                red = 0
                greem = 0
                blue = 0

                for i in range(3):
                    for j in range(3):
                        r, g, b, p = self.originalImage.image.getpixel((x+(i-1),  y+(j-1)))
                        
                        if (r < red):
                            red = r
                            greem = g
                            blue = b

                r, g, b, p = self.originalImage.image.getpixel((x,  y))
                if r < 128:
                    if(red-10 > 0): red = red - 10 
                    else: red = 0
                    if(greem-10 > 0): greem = greem - 10 
                    else: greem = 0
                    if(blue-10 > 0): blue = blue - 10 
                    else: blue = 0


                    for i in range(3):
                        for j in range(3):
                            changedImageMap[x+(i-1), y+(j-1)] = red, greem, blue
        
        self.changedImage.image.save("attachment/erosion." + self.changedImage.getExtencial(),
                                     format=self.originalImage.image.format)
        self.changedImage.setFile("attachment/erosion." + self.changedImage.getExtencial())
        return self.changedImage

    def opening(self):
        erosionImage = self.erosion()
        changedImage = File(erosionImage.getFile())
        changedImageMap = changedImage.convertImageToMap()

        for y in range(1, self.changedImage.getHeight()-2):
            for x in range(1, self.changedImage.getWidth()-2):

                red = 0
                greem = 0
                blue = 0

                for i in range(3):
                    for j in range(3):
                        r, g, b, p = erosionImage.image.getpixel((x+(i-1),  y+(j-1)))
                        
                        if (r < red):
                            red = r
                            greem = g
                            blue = b

                r, g, b, p = erosionImage.image.getpixel((x,  y))
                if r < 128:
                    if(red-10 > 0): red = red - 10 
                    else: red = 0
                    if(greem-10 > 0): greem = greem - 10 
                    else: greem = 0
                    if(blue-10 > 0): blue = blue - 10 
                    else: blue = 0


                    for i in range(3):
                        for j in range(3):
                            changedImageMap[x+(i-1), y+(j-1)] = red, greem, blue
        
        changedImage.image.save("attachment/opening." + self.changedImage.getExtencial(),
                                    format=self.originalImage.image.format)
        changedImage.setFile("attachment/opening." + self.changedImage.getExtencial())
        return changedImage
    
    def closure(self):
        dilationImage = self.erosion()
        changedImage = File(dilationImage.getFile())
        changedImageMap = changedImage.convertImageToMap()

        for y in range(1, self.changedImage.getHeight()-3):
            for x in range(1, self.changedImage.getWidth()-3):

                red = 0
                greem = 0
                blue = 0

                for i in range(3):
                    for j in range(3):
                        r, g, b, p = dilationImage.image.getpixel((x+(i-1),  y+(j-1)))
                        
                        if (r > red):
                            red = r
                            greem = g
                            blue = b
                
                if ((red+greem+blue)/3 > 128):

                    if(red+10 < 255): red = red + 10 
                    else: red = 255
                    if(greem+10 < 255): greem = greem + 10 
                    else: greem = 255
                    if(blue+10 < 255): blue = blue + 10 
                    else: blue = 255

                    for i in range(3):
                        for j in range(3):
                            changedImageMap[x+(i-1), y+(j-1)] = red, greem, blue
        
        changedImage.image.save("attachment/dilation." + self.changedImage.getExtencial(),
                                     format=self.originalImage.image.format)
        changedImage.setFile("attachment/dilation." + self.changedImage.getExtencial())
        return changedImage