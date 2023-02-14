import pyautogui as pg, webbrowser as web, time as tn,numpy as np
import pandas as pd
from pynput.keyboard import Controller
from PIL import Image as img

keyboard = Controller()

imagen=img.open('img.png')
imagen.copy


chrome_path='C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    
    #print(type(mensaje))
    
web.get(chrome_path).open(f"https://web.whatsapp.com/send?phone=+573142740860")
    
   
    
tn.sleep(8)
    #keyboard.type(f"Buenos días, ABOGADOS en representación de Creditek, Estimado (a) {nombre} evidenciamos incumplimiento en el pago de su crédito, Realizamos campaña de conciliación PREJURIDICA con fecha límite de pago ENERO 31, acceda a descuento por pago de contado. Genere reporte positivo en Data Crédito y suspensión de cobro jurídico. Comuníquese y no deje vencer esta fecha y evite inconvenientes. Si no tenemos una comunicación con usted asumiremos su desinterés en solucionar y pasara a la etapa Jurídica. WhatsApp 3052787721 - 3165600067 - Teléfono en Bogota (333)6025026")
#keyboard.type(imagen)
#pg.write(imagen)
pg.hotkey('ctrl','v')
tn.sleep(1)
#keyboard.type(f"Buenos Dias, ABOGADOS en representación de Creditek S.A.S., Estimado (a) {nombre} evidenciamos incumplimiento en el pago de su crédito, Realizamos campaña de conciliación PREJURIDICA con fecha limite de pago ENERO 31, acceda a descuento por pago de contado. Genere reporte positivo en Data Credito y suspension de cobro juridico. Comuniquese Abogado {asesor} y no deje vencer esta fecha  y evite inconvenientes. Si no tenemos una comunicacion con usted asumiremos su desinterés en solucionar y pasara a la etapa juridica. Whatsapp 3246258127 - Telefono en Bogota (333)6025026")
    
    #print('ñ')
tn.sleep(3)
pg.press('enter')
tn.sleep(2)
pg.hotkey('ctrl','w')
#numeros_gestionados.append(dato)
print('mensaje enviado: ')
