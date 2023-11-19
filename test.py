import cv2
import numpy as np

class BordaSobel:
    def __init__(self, threshold):
        self.threshold = threshold

    def executar(self, imagem):
        imagem_origem = np.copy(imagem)
        altura, largura = imagem.shape
        gx_kernel = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
        gy_kernel = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

        for y in range(1, altura - 1):
            for x in range(1, largura - 1):
                gx = np.sum(imagem_origem[y - 1:y + 2, x - 1:x + 2] * gx_kernel)
                gy = np.sum(imagem_origem[y - 1:y + 2, x - 1:x + 2] * gy_kernel)
                g = np.sqrt(gx**2 + gy**2)
                pixel = 0 if g <= self.threshold else 255
                imagem[y, x] = pixel

        return imagem

# Exemplo de uso:
# Substitua 'caminho_da_imagem' pelo caminho da sua imagem
caminho_da_imagem = 'C:/Users/Pedro/Documents/Feevale-PDI-Interface-V1/attachment/Lena.png'
imagem = cv2.imread(caminho_da_imagem, cv2.IMREAD_GRAYSCALE)

# Instancie a classe BordaSobel com um valor de limiar (threshold)
metodo_borda = BordaSobel(threshold=100)

# Aplique o método de detecção de bordas Sobel na imagem
imagem_resultante = metodo_borda.executar(imagem)

# Exiba a imagem resultante
cv2.imshow('Imagem Resultante', imagem_resultante)
cv2.waitKey(0)
cv2.destroyAllWindows()
