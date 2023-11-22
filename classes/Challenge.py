from PIL import Image
from classes.File import File

class Challenge:
    originalImage: File
    changedImage: File

    def __init__(self, originalImage, changedImage):
        self.originalImage = originalImage
        self.changedImage = changedImage
        self.changedImage.setFile(self.originalImage.getFile())

        self.object1 = Image.new('RGB', (self.originalImage.getWidth(), self.originalImage.getHeight()))
        self.object2 = Image.new('RGB', (self.originalImage.getWidth(), self.originalImage.getHeight()))
        self.object2 = Image.new('RGB', (self.originalImage.getWidth(), self.originalImage.getHeight()))

    def identifyObject(self):
        originalImageMap = self.changedImage.convertImageToMap()

        object1 = Image.new('RGB', (self.originalImage.getWidth(), self.originalImage.getHeight()))
        object1Map = object1.load()

        object1X = []
        object1Y = []

        for x in range(self.originalImage.getWidth()):
            for y in range(self.originalImage.getHeight()):
                r, g, b, p = originalImageMap[x, y]

                if r > 150:
                    object1Map[x, y] = 0, 0, 0
                    object1X.append(x)
                    object1Y.append(y)

        self.object1.save("attachment/objeto1." + self.originalImage.getExtencial(),
                                     format=self.originalImage.image.format)
        return self.object1