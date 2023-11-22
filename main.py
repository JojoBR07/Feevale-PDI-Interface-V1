from classes.Challenge import Challenge
from classes.File import File
from classes.Filter import Filter
from classes.GeometricTransformations import GeometricTransformations
from classes.MathematicalMorphology import MathematicalMorphology
import PySimpleGUI as sg

sg.theme('BluePurple')
originalImage = File("C:/Users/Pedro/Documents/Feevale-PDI-Interface-V1/attachment/Lena.png")
changedImage = File("C:/Users/Pedro/Documents/Feevale-PDI-Interface-V1/attachment/Lena.png")
filters = Filter(originalImage, changedImage)
transformations = GeometricTransformations(originalImage, changedImage)
morphology = MathematicalMorphology(originalImage, changedImage)
challenge = Challenge(originalImage, changedImage)

original = [
    [sg.Text(text='Imagem Original', font=('Arial Bold', 16), size=20, expand_x=True, justification='center')],
    [sg.Image(filename=originalImage.getFile(), key="-ORIGINAL_IMAGE-")]
]

changed = [
    [sg.Text(text='Imagem Modificada', font=('Arial Bold', 16), size=20, expand_x=True, justification='center')],
    [sg.Image(filename=changedImage.getFile(), key="-CHANGED_IMAGE-")]
]

menu_def = [
    ['&Arquivo', ['Abrir imagem', '&Salvar imagem', '---', '&Sobre', '&Sair', ]],
    ['Filtros', ['Grayscale', 'Passa Baixa', ['Média', 'Mediana', 'Moda', 'Gauss', 'Passa Baixa'], 'Passa Alta', 'Threshold']],
    ['Transformações', ['Brilho', 'Contrate']],
    ['Transformações Geométricas', ['Transladar', 'Rotacionar', ['10°', '45°', '90°'], 'Espelhar', ['Horizontal', 'Vertical'], 'Escala', ['Aumentar', 'Diminuir']]],
    ['Morfologia Matemática', ['Dilatação', 'Erosão', 'Abertura', 'Fechamento']],
    ['Extração de Caracteristicas', ['---', '&Desafio', '---']]
]

buttons = [
    sg.Button('Média', button_color='black', key='-BT_MEDIA-', visible=False),
    sg.Button('Mediana', button_color='black', key='-BT_MEDIANA-', visible=False),
    sg.Button('Moda', button_color='black', key='-BT_MODA-', visible=False),
    sg.Button('Gauss', button_color='black', key='-BT_GAUSS-', visible=False),
]

layout = [
    [
        sg.Menu(menu_def),
        sg.Column(original, justification='center'),
        sg.VSeperator(),
        sg.Column(changed, justification='center'),
        buttons,
    ]
]

window = sg.Window('Processamento Digital de Imagens', layout, size=(1000, 500), element_justification='c')

while True:
    event, values = window.read()
    print(event, values)

    if event in (None, 'Sair'):
        break
    elif event in ('Abrir imagem'):
        originalImage.setFile(sg.popup_get_file('Selecione um arquivo', title="Arquivos"))
        changedImage.setFile(originalImage.getFile())
        window["-ORIGINAL_IMAGE-"].update(originalImage.getFile())
    elif event in ('Salvar imagem'):
        changedImage.saveFile(sg.popup_get_folder('Selecione um diretório', title="Salvar imagem"))
    elif event in ('Sobre'):
        sg.popup('Desenvolvedor: Joilson de Oliveira Telles', 'Versão do Software: 1.8', title="Sobre")
    elif event in ('Grayscale'):
        changedImage = filters.covertImageToGrayscale()
        window["-CHANGED_IMAGE-"].update(changedImage.getFile())
    elif event in ('Passa Alta'):
        changedImage = filters.sobel(200)
        window["-CHANGED_IMAGE-"].update(changedImage.getFile())
    elif event in ('Passa Baixa'):
        window['-BT_MEDIA-'].update(visible=True)
        window['-BT_MEDIANA-'].update(visible=True)
        window['-BT_MODA-'].update(visible=True)
        window['-BT_GAUSS-'].update(visible=True)
    elif event in ('-BT_MEDIA-', 'Média'):
        changedImage = filters.covertImageToMedia()
        window["-CHANGED_IMAGE-"].update(changedImage.getFile())
    elif event in ('-BT_MODA-', 'Moda'):
        changedImage = filters.covertImageToModa()
        window["-CHANGED_IMAGE-"].update(changedImage.getFile())
    elif event in ('-BT_MEDIANA-', 'Mediana'):
        changedImage = filters.covertImageToMediana()
        window["-CHANGED_IMAGE-"].update(changedImage.getFile())
    elif event in ('-BT_GAUSS-', 'Gauss'):
        changedImage = filters.covertImageToGlauss()
        window["-CHANGED_IMAGE-"].update(changedImage.getFile())
    elif event in ('Transladar'):
        x = sg.popup_get_text("Insira o deslocamento HORIZONTAL da imagem: ", title="Traslação")
        y = sg.popup_get_text("Insira o deslocamento VERTICAL da imagem: ", title="Traslação")
        changedImage = transformations.translateImage(int(x), int(y))
        window["-CHANGED_IMAGE-"].update(changedImage.getFile())
    elif event in ('Aumentar'):
        changedImage = transformations.scaleImage(3)
        window["-CHANGED_IMAGE-"].update(changedImage.getFile())
    elif event in ('Diminuir'):
        changedImage = transformations.scaleImage(0.33)
        window["-CHANGED_IMAGE-"].update(changedImage.getFile())
    elif event in ('Horizontal'):
        changedImage = transformations.horizontalMirroringImage()
        window["-CHANGED_IMAGE-"].update(changedImage.getFile())
    elif event in ('Vertical'):
        changedImage = transformations.verticalMirroringImage()
        window["-CHANGED_IMAGE-"].update(changedImage.getFile())
    elif event in ('10°'):
        changedImage = transformations.rotationingImage(10)
        window["-CHANGED_IMAGE-"].update(changedImage.getFile())
    elif event in ('45°'):
        changedImage = transformations.rotationingImage(45)
        window["-CHANGED_IMAGE-"].update(changedImage.getFile())
    elif event in ('90°'):
        changedImage = transformations.rotationingImage(90)
        window["-CHANGED_IMAGE-"].update(changedImage.getFile())
    elif event in ('Brilho'):
        value = sg.popup_get_text("Insira o modificador de brilho: ", title="Brilho")
        changedImage = filters.brightness(float(value))
        window["-CHANGED_IMAGE-"].update(changedImage.getFile())
    elif event in ('Contrate'):
        value = sg.popup_get_text("Insira o modificador de contraste: ", title="Contraste")
        changedImage = filters.contrast(float(value))
        window["-CHANGED_IMAGE-"].update(changedImage.getFile())
    elif event in ('Dilatação'):
        changedImage = morphology.dilation()
        window["-CHANGED_IMAGE-"].update(changedImage.getFile())
    elif event in ('Erosão'):
        changedImage = morphology.erosion()
        window["-CHANGED_IMAGE-"].update(changedImage.getFile())
    elif event in ('Abertura'):
        changedImage = morphology.opening()
        window["-CHANGED_IMAGE-"].update(changedImage.getFile())
    elif event in ('Fechamento'):
        changedImage = morphology.closure()
        window["-CHANGED_IMAGE-"].update(changedImage.getFile())
    elif event in ('Desafio'):
        challenge.identifyObject()
        window["-CHANGED_IMAGE-"].update(changedImage.getFile())
    if event == 'Display':
        # Update the "output" text element
        # to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])

window.close()
