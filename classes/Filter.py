import numpy as np
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

    def most_frequent(self, vetor):
        unique, counts = np.unique(vetor, return_counts=True)
        index = np.argmax(counts)
        return unique[index]

    def covertImageToGrayscale(self):
        originalImageMap = self.changedImage.convertImageToMap()

        for i in range(self.originalImage.getHeight()):
            for j in range(self.originalImage.getWidth()):
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
        self.changedImage.setFile(self.originalImage.getFile())
        self.changedImage = self.covertImageToGrayscale()
        changedImageMap = self.changedImage.convertImageToMap()

        for x in range(self.changedImage.getWidth()-1):
            for y in range(self.changedImage.getHeight()-1):

                lista = list()
                r, g, b, p = self.changedImage.image.getpixel((y-1, x-1))
                lista.append(r)

                r, g, b, p = self.changedImage.image.getpixel((y - 1, x))
                lista.append(r)

                r, g, b, p = self.changedImage.image.getpixel((y - 1, x + 1))
                lista.append(r)

                r, g, b, p = self.changedImage.image.getpixel((y, x - 1))
                lista.append(r)

                r, g, b, p = self.changedImage.image.getpixel((y, x))
                lista.append(r)

                r, g, b, p = self.changedImage.image.getpixel((y, x + 1))
                lista.append(r)

                r, g, b, p = self.changedImage.image.getpixel((y + 1, x - 1))
                lista.append(r)

                r, g, b, p = self.changedImage.image.getpixel((y + 1, x))
                lista.append(r)

                r, g, b, p = self.changedImage.image.getpixel((y + 1, x + 1))
                lista.append(r)

                changedImageMap[y-1, x-1] = (self.most_frequent(lista), self.most_frequent(lista), self.most_frequent(lista))
                del lista

        self.changedImage.image.save("attachment/moda." + self.originalImage.getExtencial(),
                                     format=self.originalImage.image.format)
        self.changedImage.setFile("attachment/moda." + self.originalImage.getExtencial())
        return self.changedImage

    def covertImageToMediana(self):
        self.changedImage = self.covertImageToGrayscale()
        changedImageMap = self.changedImage.convertImageToMap()

        for y in range(self.changedImage.getWidth()-1):
            for x in range(self.changedImage.getHeight()-1):

                i, j = 1, 1
                lista = list()
                for i in range(3):
                    for j in range(3):
                        r, g, b, p = self.changedImage.image.getpixel((x+(i-1),  y+(j-1)))
                        lista.append(int(r))

                lista.sort()
                changedImageMap[x, y] = (lista[4], lista[4], lista[4])
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

        for y in range(1, self.changedImage.getWidth()-1):
            for x in range(1, self.changedImage.getHeight()-1):

                i, j, z = 0, 0, 0
                for i in range(3):
                    for j in range(3):
                        r, g, b, p = self.changedImage.image.getpixel((x+(i-1),  y+(j-1)))
                        z += r * mask[i][j]

                changedImageMap[x, y] = (int(z/16), int(z/16), int(z/16))

        self.changedImage.image.save("attachment/glauss." + self.originalImage.getExtencial(),
                                     format=self.originalImage.image.format)
        self.changedImage.setFile("attachment/glauss." + self.originalImage.getExtencial())
        return self.changedImage

    def brightness(self, value):
        originalImageMap = self.changedImage.convertImageToMap()

        for i in range(self.originalImage.getWidth()):
            for j in range(self.originalImage.getHeight()):
                r, g, b, p = self.originalImage.image.getpixel((i, j))
                r = 1 * r + value
                g = 1 * g + value
                b = 1 * b + value
                originalImageMap[i, j] = (int(r), int(g), int(b))

        self.changedImage.image.save("attachment/brightness." + self.originalImage.getExtencial(),
                                     format=self.originalImage.image.format)
        self.changedImage.setFile("attachment/brightness." + self.originalImage.getExtencial())
        return self.changedImage
    
    def contrast(self, value):
        originalImageMap = self.changedImage.convertImageToMap()

        for i in range(self.originalImage.getWidth()):
            for j in range(self.originalImage.getHeight()):
                r, g, b, p = self.originalImage.image.getpixel((i, j))
                r = value * (r-128) + 128 # Aumentar e Reduzir 128 para manter o ponto médio (Recomendação chatgpt)
                g = value * (g-128) + 128 # Aumentar e Reduzir 128 para manter o ponto médio (Recomendação chatgpt)
                b = value * (b-128) + 128 # Aumentar e Reduzir 128 para manter o ponto médio (Recomendação chatgpt)
                originalImageMap[i, j] = (int(r), int(g), int(b))

        self.changedImage.image.save("attachment/contrast." + self.originalImage.getExtencial(),
                                     format=self.originalImage.image.format)
        self.changedImage.setFile("attachment/contrast." + self.originalImage.getExtencial())
        return self.changedImage