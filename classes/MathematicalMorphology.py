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
        originalImageMap = self.changedImage.convertImageToMap()

        for y in range(1, self.changedImage.getWidth()-1):
            for x in range(1, self.changedImage.getHeight()-1):
                i, j = 0, 0

                r, g, b, p = self.changedImage.image.getpixel((y,  x))

                if(r+10 < 255): r = r + 10 
                else: r = 255
                if(g+10 < 255): g = g + 10 
                else: g = 255
                if(b+10 < 255): b = b + 10 
                else: b = 255

                for i in range(3):
                    for j in range(3):
                        originalImageMap[y+(i-1), x+(j-1)] = (r, g, b)

        self.changedImage.image.save("attachment/dilation." + self.originalImage.getExtencial(),
                                format=self.originalImage.image.format)
        self.changedImage.setFile("attachment/dilation." + self.originalImage.getExtencial())
        return self.changedImage

                        
