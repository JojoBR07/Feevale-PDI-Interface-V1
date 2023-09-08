from PIL import Image

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
    def saveFile(self):
        return self.test
    
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