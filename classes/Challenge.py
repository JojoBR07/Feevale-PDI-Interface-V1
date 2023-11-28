from PIL import Image
from classes.File import File

class Challenge:
    originalImage: File
    changedImage: File

    def __init__(self, originalImage, changedImage):
        self.originalImage = originalImage
        self.changedImage = changedImage
        self.changedImage.setFile(self.originalImage.getFile())

        self.object1 = Image.new('RGB', (self.changedImage.getWidth(), self.changedImage.getHeight()))
        self.object2 = Image.new('RGB', (self.changedImage.getWidth(), self.changedImage.getHeight()))
        self.object2 = Image.new('RGB', (self.changedImage.getWidth(), self.changedImage.getHeight()))

        self.object1X = []
        self.object1Y = []

        self.object2X = []
        self.object2Y = []

        self.object3X = []
        self.object3Y = []

        self.numbers = [30852, 12832, 23995, 21943, 21141, 22270, 26710, 18629, 29387, 29606]
        self.operators = [1670932, 1261689, 2919020, 1540880]

    def updateImages(self, newImage, object):
        self.originalImage = File(newImage)

        if object == 1:
            self.object1 = Image.new('RGB', (self.originalImage.getWidth(), self.originalImage.getHeight()))
            self.object1X = []
            self.object1Y = []
        elif object == 2:
            self.object2 = Image.new('RGB', (self.originalImage.getWidth(), self.originalImage.getHeight()))
            self.object2X = []
            self.object2Y = []
        else:
            self.object3 = Image.new('RGB', (self.originalImage.getWidth(), self.originalImage.getHeight()))
            self.object3X = []
            self.object3Y = []

    def identifyObjectNumber(self, image):
        self.updateImages(image, 1)

        originalImageMap = self.originalImage.convertImageToMap()
        object1Map = self.object1.load()

        for x in range(self.originalImage.getWidth()):
            for y in range(self.originalImage.getHeight()):
                try:
                    r, g, b, p = originalImageMap[x, y]
                except Exception as e:
                    r, g, b = originalImageMap[x, y]

                if r < 50:
                    object1Map[x, y] = 255, 255, 255
                    self.object1X.append(x)
                    self.object1Y.append(y)

        print("Pixels: ", len(self.object2X))
        print("Pixels em Centrímetros: ", round((2.646 * len(self.object1X))/10, 3))
        print("Número: ", self.findSimilarObject(len(self.object1X), "numbers"))

        self.object1.save("attachment/objeto." + self.originalImage.getExtencial(),
                                     format=self.originalImage.image.format)
        return self.object1
    
    def identifyObjectNumber2(self, image):
        self.updateImages(image, 3)

        originalImageMap = self.originalImage.convertImageToMap()
        object1Map = self.object3.load()

        for x in range(self.originalImage.getWidth()):
            for y in range(self.originalImage.getHeight()):
                try:
                    r, g, b, p = originalImageMap[x, y]
                except Exception as e:
                    r, g, b = originalImageMap[x, y]

                if r < 50:
                    object1Map[x, y] = 255, 255, 255
                    self.object3X.append(x)
                    self.object3Y.append(y)

        
        print("Pixels: ", len(self.object3X))
        print("Pixels em Centrímetros: ", round((2.646 * len(self.object3X))/10, 3))
        print("Número: ", self.findSimilarObject(len(self.object3X), "numbers"))

        self.object1.save("attachment/objeto." + self.originalImage.getExtencial(),
                                     format=self.originalImage.image.format)
        return self.object1
    
    def identifyObjectOperation(self, image):
        self.updateImages(image, 2)

        originalImageMap = self.originalImage.convertImageToMap()
        object1Map = self.object2.load()

        for x in range(self.originalImage.getWidth()):
            for y in range(self.originalImage.getHeight()):

                try:
                    r, g, b, p = originalImageMap[x, y]
                except Exception as e:
                    r, g, b = originalImageMap[x, y]

                if r < 50:
                    object1Map[x, y] = 255, 255, 255
                    self.object2X.append(x)
                    self.object2Y.append(y)

        
        print("Pixels: ", len(self.object1X))
        print("Pixels em Centrímetros: ", round((2.646 * len(self.object1X))/10, 3))
        print("Número: ", self.findSimilarObject(len(self.object2X), "operators"))

        self.object1.save("attachment/objeto." + self.originalImage.getExtencial(),
                                     format=self.originalImage.image.format)
        return self.object1
    
    def findSimilarObject(self, valor, type):
        melhor_posicao = None
        melhor_diferenca = float('inf')

        lista = self.numbers if type == "numbers" else self.operators 

        for i, elemento in enumerate(lista):
            diferenca_percentual = abs(elemento - valor) / max(elemento, valor) * 100

            if diferenca_percentual <= 90 and diferenca_percentual < melhor_diferenca:
                melhor_posicao = i
                melhor_diferenca = diferenca_percentual

        return melhor_posicao
    
    def calculator (self):

        value1 = self.findSimilarObject(len(self.object1X), "numbers");
        value2 = self.findSimilarObject(len(self.object2X), "operators");
        value3 = self.findSimilarObject(len(self.object3X), "numbers");

        if value2 == 0:
            result = value1 + value3
            operator = "+"
        elif value2 == 1:
            result = value1 / value3
            operator = "/"
        elif value2 == 2:
            result = value1 * value3
            operator = "*"
        else:
            result = value1 - value3
            operator = "-"
        
        return (f"{value1} {operator} {value3} = {result}")