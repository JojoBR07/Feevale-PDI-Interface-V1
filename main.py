from classes.File import File
import PySimpleGUI as sg

sg.theme('BluePurple')
originalImage = File("C:/Users/Pedro/Documents/Feevale-PDI-Interface-V1/attachment/Lena.png")
changedImage = File("C:/Users/Pedro/Documents/Feevale-PDI-Interface-V1/attachment/Lena.png")

original = [
    [sg.Text(text='Imagem Original', font=('Arial Bold', 16), size=20, expand_x=True, justification='center')],
    [sg.Image(filename='C:/Users/Pedro/Documents/Feevale-PDI-Interface-V1/attachment/Lena.png')]
]

changed = [
	[sg.Text(text='Imagem Modificada', font=('Arial Bold', 16), size=20, expand_x=True, justification='center')],
    [sg.Image(filename="C:/Users/Pedro/Documents/Feevale-PDI-Interface-V1/attachment/Lena.png")]
]

menu_def = [
   ['&Arquivo', ['Abrir imagem', '&Salvar imagem::savekey', '---', '!&Sobre', '&Sair',]],
   ['Transformações Geométricas', ['Transladar', 'Rotacionar', 'Espelhar', 'Aumentar', 'Diminuir']],
   ['Filtros', ['Grayscale', 'Passa Baixa','Passa Alta', 'Threshold']],
   ['Morfologia Matemática', ['Dilatação', 'Erosão', 'Abertura', 'Fechamento']],
   ['Extração de Caracteristicas', ['---', '!&DESAFIO', '---']]
]

layout = [
    [
	    sg.Menu(menu_def),
        sg.Column(original, justification='center'),
        sg.VSeperator(),
        sg.Column(changed, justification='center'),
    ]
]

window = sg.Window('Processamento Digital de Imagens', layout, size=(1000, 500))

while True:
	event, values = window.read()
	print(event, values)
	
	if event in (None, 'Sair'):
		break
	elif event in ('Abrir imagem'):
		print(originalImage)
		#sg.popup_get_file('Selecione um arquivo', title="Arquivos")
	
	if event == 'Display':
		# Update the "output" text element
		# to be the value of "input" element
		window['-OUTPUT-'].update(values['-IN-'])

window.close()