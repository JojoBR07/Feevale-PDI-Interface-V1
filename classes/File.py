from PIL import Image
import os

class File:

    def __init__(self, path):
        self.path = path
        self.image = Image.open(path)
        self.width = self.image.width
        self.height = self.image.height
        self.extencial = path.split(".")[-1]
        self.name = path.split("/")[-1]

    def __str__(self):
        print("Path: " + self.path)
        print("Size: (%d x %d)" % (self.width, self.height))
        print("Extencial: " + self.extencial)
        return "Name: " + self.name

    # Retrieves instance variable
    def saveFile(self, path):
        self.image.save(path + "/" + self.getName(), format=self.image.format)

    def setFile(self, path):
        self.path = path
        self.image = Image.open(self.path)
        self.width = self.image.width
        self.height = self.image.height
        self.extencial = self.path.split(".")[-1]
        self.name = self.path.split("/")[-1]

    def getFile(self):
        return self.path

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getExtencial(self):
        return self.extencial

    def getName(self):
        return self.name

    def convertImageToMap(self):
        return self.image.load()
    
    def converter_jpeg_para_png(self, jpeg_path):
        try:
            # Abre a imagem JPEG
            imagem = Image.open(jpeg_path)
            nome_base = os.path.basename(imagem.fileneame.split("/")[-1])  # Obtém o nome do arquivo com extensão
            nome_sem_extensao, _ = os.path.splitext(nome_base) 

            # Salva a imagem como PNG
            imagem.save(imagem.filename, 'PNG')

            print(f"Conversão concluída: {jpeg_path} para {imagem.filename}")

            return imagem.filename

        except Exception as e:
            print(f"Erro ao converter a imagem: {e}")

        return None
