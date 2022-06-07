import os
import zipfile
from datetime import datetime,timedelta
import ctypes
import PySimpleGUI as sg
import pyautogui

layout = [
    [sg.Text("Escolha",enable_events = True,key = "-TEXT1-"),sg.InputCombo(["Casa","Carro"])],
    [sg.Text("Imagem",enable_events = True,key = "-TEXT2-"),sg.Image("imagem_a_ser_procurada.png",expand_x=True)],
    [sg.Text("Entrada",enable_events = True,key = "-TEXT3-"),sg.Input()],
    [sg.Text("",enable_events = True,key = "-TEXT4-",justification="center",expand_x=True)],
    [sg.Button("Confirmar", key = "Bconfirma"),sg.Button("Sair",size=(7,1), key = "Bsair"),sg.Button("Achar",size=(7,1), key = "Bachar")]
]

window = sg.Window("Escreve e Acha",layout)

while True:
    event, values = window.read()

    #Sair do programa
    if event == sg.WIN_CLOSED or event == "Bsair":
        break
    #Para escrever o texto
    if event == "Bconfirma":
        retorno = sg.Window("Modelo",[[sg.Input(),sg.Button("OK"),sg.Button("Cancelar")]])
        window["-TEXT4-"].update(values[0]+":"+values[2]+" "+str(retorno.read()[1][0]))
        retorno.close()
    #Achar uma imagem
    if event == "Bachar":
        achou = 0
        while achou == 0:
            if pyautogui.locateOnScreen('imagem_a_ser_procurada.png') != None:
                lx, ly, x2, y2 = pyautogui.locateOnScreen('imagem_a_ser_procurada.png')
                pyautogui.leftClick(x=lx,y=ly)
                achou = 1

window.close()
