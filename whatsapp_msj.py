import pyautogui as pg, webbrowser as web, time as tn,numpy as np
import pandas as pd
from pynput.keyboard import Controller
import time 


keyboard = Controller()



#!/usr/bin/python
# -*- coding: latin-1 -*-


prueba=pd.read_excel('base_gestionar.xlsx')
numeros_gestionados=[]


print(prueba.columns)
dato=int(prueba['TEL1'][0])
print(dato)

for i in range(len(prueba)):
    dato=int(prueba['TEL1'][i])
    dato=str(dato)
    deuda=prueba['DEUDA_VDA'][i]
    nombre=str(prueba['NOMBRE'][i]).upper()
    asesor=prueba['ASESOR'][i]


    
    chrome_path='C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    
    
    
    web.get(chrome_path).open(f"https://web.whatsapp.com/send?phone=+57{dato}")
    
   
    
    tn.sleep(7.5)
       

    #keyboard.type(f"Buen día señor(a) {nombre}, *IMPERDIBLE*,  *Creditek* lanza la campaña  por el mes de febrero con descuentos hasta del 50 % ! Comunícate por este medio o al teléfono 3336025026.")
    keyboard.type(f'Buen día señor(a) {nombre}, ¿cómo se encuentra?')

    tn.sleep(3)
    pg.press('enter')
    tn.sleep(0.5)
    pg.hotkey('ctrl','w')
    numeros_gestionados.append(dato)
    print('mensaje enviado: ',dato)
    


numeros_gestionados=pd.DataFrame(numeros_gestionados)

numeros_gestionados.to_excel('numeros_gestionados.xlsx')
