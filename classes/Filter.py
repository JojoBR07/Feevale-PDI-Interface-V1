from PIL import Image
from classes.File import File


class Filter:
    originalImage: File
    changedImage: File

    def __init__(self, originalImage, changedImage):
        self.originalImage = originalImage
        self.changedImage = changedImage
        self.changedImage.setFile(self.originalImage.getFile())

    def getChangedImage(self):
        return 0

    def covertImageToGrayscale(self):
        originalImageMap = self.changedImage.convertImageToMap()

        for i in range(self.originalImage.getWidth()):
            for j in range(self.originalImage.getHeight()):
                r, g, b, p = self.originalImage.image.getpixel((i, j))
                grayscale = (r + g + b) / 3
                originalImageMap[i, j] = (int(grayscale), int(grayscale), int(grayscale))

        self.changedImage.image.save("attachment/grayscale." + self.originalImage.getExtencial(),
                                     format=self.originalImage.image.format)
        self.changedImage.setFile("attachment/grayscale." + self.originalImage.getExtencial())
        return self.changedImage

    def covertImageToMedia(self):
        self.changedImage = self.covertImageToGrayscale()
        changedImageMap = self.changedImage.convertImageToMap()

        mask = [[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]]

        for y in range(self.changedImage.getWidth()-1):
            for x in range(self.changedImage.getHeight()-1):

                i, j, z = 0, 0, 0
                for i in range(3):
                    for j in range(3):
                        r, g, b, p = self.changedImage.image.getpixel((x+(i-1),  y+(j-1)))
                        z = z + r * mask[i][j]

                changedImageMap[x, y] = (int(z/9), int(z/9), int(z/9))

        self.changedImage.image.save("attachment/media." + self.originalImage.getExtencial(),
                                     format=self.originalImage.image.format)
        self.changedImage.setFile("attachment/media." + self.originalImage.getExtencial())
        return self.changedImage

    def covertImageToModa(self):
        self.changedImage = self.covertImageToGrayscale()
        changedImageMap = self.changedImage.convertImageToMap()

        for y in range(self.changedImage.getWidth()-1):
            for x in range(self.changedImage.getHeight()-1):

                i, j, frequente = 0, 0, 0
                moda = list()
                for i in range(3):
                    for j in range(3):
                        r, g, b, p = self.changedImage.image.getpixel((x+(i-1),  y+(j-1)))
                        moda.append(r)
                frequente = max(set(moda), key=moda.count)

                del moda
                changedImageMap[x, y] = (int(frequente), int(frequente), int(frequente))

        self.changedImage.image.save("attachment/moda." + self.originalImage.getExtencial(),
                                     format=self.originalImage.image.format)
        self.changedImage.setFile("attachment/moda." + self.originalImage.getExtencial())
        return self.changedImage

    def covertImageToMediana(self):
        self.changedImage = self.covertImageToGrayscale()
        changedImageMap = self.changedImage.convertImageToMap()

        for y in range(self.changedImage.getWidth()-1):
            for x in range(self.changedImage.getHeight()-1):

                i, j, frequente = 0, 0, 0
                lista = list()
                for i in range(3):
                    for j in range(3):
                        r, g, b, p = self.changedImage.image.getpixel((x+(i-1),  y+(j-1)))
                        lista.append(int(r))

                lista.sort()
                changedImageMap[x, y] = (lista[5], lista[5], lista[5])
                del lista

        self.changedImage.image.save("attachment/mediana." + self.originalImage.getExtencial(),
                                     format=self.originalImage.image.format)
        self.changedImage.setFile("attachment/mediana." + self.originalImage.getExtencial())
        return self.changedImage

    def covertImageToGlauss(self):
        self.changedImage = self.covertImageToGrayscale()
        changedImageMap = self.changedImage.convertImageToMap()

        mask = [[1, 2, 1],
                [2, 4, 2],
                [1, 2, 1]]

        for y in range(self.changedImage.getWidth()-1):
            for x in range(self.changedImage.getHeight()-1):

                i, j, z = 0, 0, 0
                for i in range(3):
                    for j in range(3):
                        r, g, b, p = self.changedImage.image.getpixel((x+(i-1),  y+(j-1)))
                        z = z + r * mask[i][j]

                changedImageMap[x, y] = (int(z/16), int(z/16), int(z/16))

        self.changedImage.image.save("attachment/glauss." + self.originalImage.getExtencial(),
                                     format=self.originalImage.image.format)
        self.changedImage.setFile("attachment/glauss." + self.originalImage.getExtencial())
        return self.changedImage