import math
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

        for x in range(self.originalImage.getHeight()):
            for y in range(self.originalImage.getWidth()):
                novo_x = x - translateX
                novo_y = y - translateY

                if 0 <= novo_x < self.originalImage.getHeight() and 0 <= novo_y < self.originalImage.getWidth():
                    pixel = self.originalImage.image.getpixel((novo_x, novo_y))
                    self.changedImage.image.putpixel((x, y), pixel)

        self.changedImage.image.save("attachment/translate." + self.originalImage.getExtencial(),
                                     format=self.originalImage.image.format)
        self.changedImage.setFile("attachment/translate." + self.originalImage.getExtencial())
        return self.changedImage
    
    def scaleImage (self, scale):        
        self.changedImage.image = Image.new('RGB', (int(self.originalImage.getHeight() * scale), int(self.originalImage.getWidth() * scale)), (0, 0, 0))
        self.changedImage.image.save("attachment/grayscale." + self.originalImage.getExtencial(), format=self.originalImage.image.format)
        self.changedImage.setFile("attachment/grayscale." + self.originalImage.getExtencial())

        for y in range(self.changedImage.getHeight()):
            for x in range(self.changedImage.getWidth()):
                pixel = self.originalImage.image.getpixel((int(x/scale), int(y/scale)))
                self.changedImage.image.putpixel((x, y), pixel)

        self.changedImage.image.save("attachment/enlarge." + self.originalImage.getExtencial(),
                                     format=self.originalImage.image.format)
        self.changedImage.setFile("attachment/enlarge." + self.originalImage.getExtencial())
        return self.changedImage
    
    def horizontalMirroringImage (self):
        for y in range(1, self.changedImage.getHeight()):
            for x in range(1, self.changedImage.getWidth()):
                if y < self.originalImage.getHeight() and x < self.originalImage.getWidth():
                    pixel = self.originalImage.image.getpixel((x, y))
                    self.changedImage.image.putpixel((self.changedImage.getHeight() - x, y), pixel)

        self.changedImage.image.save("attachment/mirroring." + self.originalImage.getExtencial(),
                                     format=self.originalImage.image.format)
        self.changedImage.setFile("attachment/mirroring." + self.originalImage.getExtencial())
        return self.changedImage
    
    def verticalMirroringImage (self):
        for y in range(1, self.changedImage.getHeight()):
            for x in range(1, self.changedImage.getWidth()):
                if y < self.originalImage.getHeight() and x < self.originalImage.getWidth():
                    pixel = self.originalImage.image.getpixel((x, y))
                    self.changedImage.image.putpixel((x, self.originalImage.getWidth() - y), pixel)

        self.changedImage.image.save("attachment/mirroring." + self.originalImage.getExtencial(),
                                     format=self.originalImage.image.format)
        self.changedImage.setFile("attachment/mirroring." + self.originalImage.getExtencial())
        return self.changedImage
    
    def rotationingImage (self, rotation):
        self.changedImage.image = self.originalImage.image.rotate(rotation)
        self.changedImage.image = Image.new('RGB', (self.changedImage.getHeight(), self.changedImage.getWidth()))

        angulo_rad = math.radians(rotation)
        seno = math.sin(angulo_rad)
        cosseno = math.cos(angulo_rad)

        for x in range(self.changedImage.getHeight()):
            for y in range(self.changedImage.getWidth()):
                novo_x = int(x * cosseno - y * seno)
                novo_y = int(x * seno + y * cosseno)
                if 0 <= novo_x < self.changedImage.getHeight() and 0 <= novo_y < self.changedImage.getWidth():
                    pixel = self.originalImage.image.getpixel((novo_x, novo_y))
                    self.changedImage.image.putpixel((x, y), pixel)

        self.changedImage.image.save("attachment/rotation." + self.originalImage.getExtencial(),
                                     format=self.originalImage.image.format)
        self.changedImage.setFile("attachment/rotation." + self.originalImage.getExtencial())
        return self.changedImage
