import numpy as np
from PIL import Image
from classes.File import File


class GeometricTransformations:
    originalImage: File
    changedImage: File

    def __init__(self, originalImage, changedImage):
        self.originalImage = originalImage
        self.changedImage = changedImage
        self.changedImage.setFile(self.originalImage.getFile())

    def translateImage(self, translateX, translateY):
        self.changedImage.image = Image.new('RGB', (self.originalImage.getHeight(), self.originalImage.getWidth()), (0, 0, 0))

        for y in range(self.originalImage.getHeight()):
            for x in range(self.originalImage.getWidth()):
                novo_x = x - translateX
                novo_y = y - translateY

                if 0 <= novo_x < self.originalImage.getHeight() and 0 <= novo_y < self.originalImage.getWidth():
                    pixel = self.originalImage.image.getpixel((novo_x, novo_y))
                    self.changedImage.image.putpixel((x, y), pixel)

        self.changedImage.image.save("attachment/translate." + self.originalImage.getExtencial(),
                                     format=self.originalImage.image.format)
        self.changedImage.setFile("attachment/translate." + self.originalImage.getExtencial())
        return self.changedImage