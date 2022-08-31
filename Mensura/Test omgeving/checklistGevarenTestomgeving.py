from turtle import width
import numpy as np
import pandas as pd
import pyautogui as py
import time 
from PIL import Image
import cv2
import pytesseract
import re
import os
                
#Nagaan of een bepaalde gevaar aanwezig is en op basis hiervan de juiste coördinaten klikken.
def gevarenAanvinken(codes):
    biologisch(codes)
    chemisch(codes)
    fysisch(codes)
    ergonomisch(codes)
    psychosociaal(codes)
    arbeidsmiddelen(codes)

    #Scrollen door de checklist om tot de arbeidsomgeving en arbeidsorganisatie te geraken.
    py.click(x=1820, y=206)
    time.sleep(1)
    py.scroll(-50)

    arbeidsomgeving(codes)
    arbeidsorganisatie(codes)

#De functies hieronder kijken per categorie of er gevaren overeenkomen met de GRIM codes van het Word document. 
def biologisch(codes):
    time.sleep(1)
    py.click(x=501, y=458) #Vergroot de cellen
    time.sleep(2)

    if "3030001" in codes:
        py.click(x=501, y=458, clicks=1, interval=1)
        time.sleep(1)
    if "3030002" in codes:
        py.click(x=503, y=508, clicks=2, interval=1)
        time.sleep(1)
    if "3030209" in codes:
        py.click(x=502, y=547, clicks=2, interval=1)
        time.sleep(1)
    if "3030003" in codes:
        py.click(x=506, y=600, clicks=2, interval=1)
        time.sleep(1)
    if "3030004" in codes:
        py.click(x=504, y=644, clicks=2, interval=1)
        time.sleep(1)
    if "3030005" in codes:
        py.click(x=506, y=687, clicks=2, interval=1)
        time.sleep(1)
    if "3030006" in codes:
        py.click(x=506, y=733, clicks=2, interval=1)
        time.sleep(1)
    if "3013300" in codes:
        py.click(x=503, y=781, clicks=2, interval=1)
        time.sleep(1)
    time.sleep(1)
    py.click(x=221, y=367) #Klikken op de opslaan knop.
    time.sleep(1)

def chemisch(codes):
    time.sleep(1)
    py.click(x=1258, y=194) #Navigeer naar "Chemisch"
    time.sleep(2)
    py.click(x=504, y=460) #Vergroot de cellen
    time.sleep(2)
    if "3010001" in codes:
        py.click(x=504, y=460, clicks=1, interval=1)
        time.sleep(1)
    if "3010002" in codes:
        py.click(x=501, y=508, clicks=2, interval=1)
        time.sleep(1)
    if "3010705" in codes:
        py.click(x=501, y=550, clicks=2, interval=1)
        time.sleep(1)
    if "3010003" in codes:
        py.click(x=505, y=608, clicks=2, interval=1)
        time.sleep(1)
    if "3010004" in codes:
        py.click(x=504, y=655, clicks=2, interval=1)
        time.sleep(1)
    if "3010005" in codes:
        py.click(x=501, y=722, clicks=2, interval=1)
        time.sleep(1)
    if "3013600" in codes:
        py.click(x=504, y=781, clicks=2, interval=1)
        time.sleep(1)
    time.sleep(1)
    py.click(x=221, y=367) #Klikken op de opslaan knop.
    time.sleep(1)

def fysisch(codes):
    time.sleep(1)
    py.click(x=1248, y=212) #Navigeer naar "Fysisch"
    time.sleep(2)
    py.click(x=503, y=457) #Vergroot de cellen
    time.sleep(2)
    if "3020000" in codes:
        py.click(x=503, y=457, clicks=1, interval=1)
        time.sleep(1)
    if "3020100" in codes:
        py.click(x=505, y=504, clicks=2, interval=1)
        time.sleep(1)
    if "3020700" in codes:
        py.click(x=504, y=551, clicks=2, interval=1)
        time.sleep(1)
    if "3020600" in codes:
        py.click(x=502, y=608, clicks=2, interval=1)
        time.sleep(1)
    if "3020705" in codes:
        py.click(x=502, y=651, clicks=2, interval=1)
        time.sleep(1)
    if "3020703" in codes:
        py.click(x=502, y=698, clicks=2, interval=1)
        time.sleep(1)
    if "3020706" in codes:
        py.click(x=502, y=756, clicks=2, interval=1)
        time.sleep(1)
    if "3020707" in codes:
        py.click(x=502, y=801, clicks=2, interval=1)
        time.sleep(1)
    if "3020903" in codes:
        py.click(x=505, y=846, clicks=2, interval=1)
        time.sleep(1)
    if "3020901" in codes:
        py.click(x=501, y=891, clicks=2, interval=1)
        time.sleep(1)
    if "3020902" in codes:
        py.click(x=503, y=937, clicks=2, interval=1)
        time.sleep(1)
    py.scroll(-100)
    if "3020800" in codes:
        py.click(x=503, y=833, clicks=2, interval=1)
        time.sleep(1)
    if "3020300" in codes:
        py.click(x=502, y=879, clicks=2, interval=1)
        time.sleep(1)
    if "7000013" in codes:
        py.click(x=503, y=923, clicks=2, interval=1)
        time.sleep(1)
    time.sleep(1)
    py.click(x=221, y=367) #Klikken op de opslaan knop.
    time.sleep(1)

def ergonomisch(codes):
    time.sleep(1)
    py.click(x=1250, y=228) #Navigeer naar "Ergonomisch"
    time.sleep(2)
    py.click(x=504, y=460) #Vergroot de cellen
    time.sleep(2)

    if "3040200" in codes:
        py.click(x=504, y=460, clicks=1, interval=1)
        time.sleep(1)
    if "3040301" in codes:
        py.click(x=502, y=571, clicks=2, interval=1)
        time.sleep(1)
    if "3040302" in codes:
        py.click(x=502, y=616, clicks=2, interval=1)
        time.sleep(1)
    if "3040303" in codes:
        py.click(x=504, y=673, clicks=2, interval=1)
        time.sleep(1)
    if "3040304" in codes:
        py.click(x=502, y=717, clicks=2, interval=1)
        time.sleep(1)
    if "3040100" in codes:
        py.click(x=501, y=762, clicks=2, interval=1)
        time.sleep(1)
    time.sleep(1)
    py.click(x=221, y=367) #Klikken op de opslaan knop.
    time.sleep(1)



def psychosociaal(codes):
    time.sleep(1)
    py.click(x=1258, y=243) #Navigeer naar "Psychosociaal"
    time.sleep(2)
    py.click(x=504, y=461) #Vergroot de cellen
    time.sleep(2)

    if "3050001" in codes:
        py.click(x=504, y=461, clicks=1, interval=1)
        time.sleep(1)
    if "3050207" in codes:
        py.click(x=502, y=504, clicks=2, interval=1)
        time.sleep(1)
    if "3050208" in codes:
        py.click(x=502, y=551, clicks=2, interval=1)
        time.sleep(1)
    time.sleep(1)
    py.click(x=221, y=367) #Klikken op de opslaan knop.
    time.sleep(1)

def arbeidsmiddelen(codes):
    time.sleep(1)
    py.click(x=1250, y=261) #Navigeer naar "Arbeidsmiddelen"
    time.sleep(2)
    py.click(x=504, y=459) #Vergroot de cellen
    time.sleep(2)

    if "7000001" in codes:
        py.click(x=504, y=459, clicks=1, interval=1)
        time.sleep(1)
    if "7000002" in codes:
        py.click(x=502, y=504, clicks=2, interval=1)
        time.sleep(1)
    if "7000003" in codes:
        py.click(x=504, y=552, clicks=2, interval=1)
        time.sleep(1)
    if "7000004" in codes:
        py.click(x=501, y=593, clicks=2, interval=1)
        time.sleep(1)
    if "7000005" in codes:
        py.click(x=506, y=637, clicks=2, interval=1)
        time.sleep(1)
    if "7000006" in codes:
        py.click(x=504, y=682, clicks=2, interval=1)
        time.sleep(1)
    if "7000007" in codes:
        py.click(x=504, y=734, clicks=2, interval=1)
        time.sleep(1)
    if "7000008" in codes:
        py.click(x=502, y=775, clicks=2, interval=1)
        time.sleep(1)
    if "7000009" in codes:
        py.click(x=504, y=821, clicks=2, interval=1)
        time.sleep(1)
    if "7000010" in codes:
        py.click(x=503, y=864, clicks=2, interval=1)
        time.sleep(1)
    if "7000011" in codes:
        py.click(x=504, y=909, clicks=2, interval=1)
        time.sleep(1)
    if "7000012" in codes:
        py.click(x=503, y=954, clicks=2, interval=1)
        time.sleep(1)
    time.sleep(1)
    py.click(x=221, y=367) #Klikken op de opslaan knop.
    time.sleep(1)

def arbeidsomgeving(codes):
    time.sleep(1)
    py.click(x=1292, y=244) #Navigeer naar "Arbeidsomgeving"
    time.sleep(2)
    py.click(x=503, y=460) #Vergroot de cellen
    time.sleep(2)

    if "1000006" in codes:
        py.click(x=503, y=460, clicks=1, interval=1)
        time.sleep(1)
    if "1000012" in codes:
        py.click(x=503, y=505, clicks=2, interval=1)
        time.sleep(1)
    if "1000013" in codes:
        py.click(x=501, y=548, clicks=2, interval=1)
        time.sleep(1)
    if "1000014" in codes:
        py.click(x=502, y=594, clicks=2, interval=1)
        time.sleep(1)
    if "1000015" in codes:
        py.click(x=503, y=641, clicks=2, interval=1)
        time.sleep(1)
    if "1000016" in codes:
        py.click(x=502, y=685, clicks=2, interval=1)
        time.sleep(1)
    if "1000017" in codes:
        py.click(x=502, y=731, clicks=2, interval=1)
        time.sleep(1)
    if "1000018" in codes:
        py.click(x=503, y=773, clicks=2, interval=1)
        time.sleep(1)
    if "1000019" in codes:
        py.click(x=503, y=820, clicks=2, interval=1)
        time.sleep(1)
    if "1000021" in codes:
        py.click(x=505, y=866, clicks=2, interval=1)
        time.sleep(1)
    if "3020500" in codes:
        py.click(x=505, y=908, clicks=2, interval=1)
        time.sleep(1)
    if "1000020" in codes:
        py.click(x=505, y=955, clicks=2, interval=1)
        time.sleep(1)
    time.sleep(1)
    py.click(x=221, y=367) #Klikken op de opslaan knop.
    time.sleep(1)

def arbeidsorganisatie(codes):
    time.sleep(1)
    py.click(x=1278, y=261) #Navigeer naar "Arbeidsorganisatie"
    time.sleep(2)
    py.click(x=504, y=459) #Vergroot de cellen
    time.sleep(2)

    if "1000011" in codes:
        py.click(x=504, y=459, clicks=1, interval=1)
        time.sleep(1)
    if "3050308" in codes:
        py.click(x=503, y=517, clicks=2, interval=1)
        time.sleep(1)
    if "1000000" in codes:
        py.click(x=503, y=564, clicks=2, interval=1)
        time.sleep(1)
    if "3030602" in codes:
        py.click(x=505, y=620, clicks=2, interval=1)
        time.sleep(1)
    time.sleep(1)
    py.click(x=221, y=367) #Klikken op de opslaan knop.
    time.sleep(1)