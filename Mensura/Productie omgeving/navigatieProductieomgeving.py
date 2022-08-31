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
import OCRproductie

#Deze functie opent H@W en navigeert naar de verkennende bedrijfsbezoeken.
#Datums moeten manueel ingegeven worden, hier wordt momenteel 20 seconden voor gegeven.
def openhw():
    py.click(x=1917, y=1047) #Minimaliseert alle open windows -> enkel bruikbaar in echte omgeving.
    time.sleep(1)

    #Openen H@W
    py.click(x=41, y=229, clicks=2) #Openen h@W applicatie (Echte omgeving)
    #py.click(x=115, y=349, clicks=2) #Openen h@w applicatie (Test omgeving)

    #Genoeg tijd geven tot de H@W applicatie geopend is (heeft soms lang nodig in de productieomgeving).
    time.sleep(30) 

    #Navigeren naar het venster met bedrijfsbezoeken.
    py.click(x=1411, y=145) #Zet H@W in full screen
    time.sleep(1)
    py.click(x=77, y=129) #Klikt op het input veld van de verkenner.
    py.typewrite("Bedrijfsbezoek")
    py.press("enter") #Navigeren naar bedrijfsbezoeken.
    time.sleep(2)
    py.click(x=124, y=387) #Klikt op "beheer bedrijfsbezoek"
    time.sleep(2)

    py.click(x=1037, y=187) #Klikt op het input veld om de datums in te geven.
    time.sleep(20) #Tijd geven om de datums in te geven.

    #Type bedrijfsbezoek selecteren
    py.click(x=838, y=212) #Klikt op het input veld "Bezoek"
    py.typewrite("v") #Enkel "v" intypen is genoeg om "verkennend bedrijfsbezoek" te verkrijgen.
    py.press("enter")

    #Tijd geven om manueel de bedrijfsbezoeken te sorteren indien dit gewenst is.
    time.sleep(10)

#Deze functie gaat bij de bewaarde documenten na of er een verslag van het bedrijfsbezoek aanwezig is en opent deze, indien dat zo is. Anders wordt het venster gesloten.
def openVerslag(Y, i, aantalRecords):
    #Checken als we aan de laatste record zitten.
    if (i == aantalRecords+1) and (i >= 39):
        time.sleep(1)
        py.click(x=534, y=988, clicks=2) #Klik op de laatste record.
        time.sleep(2)
    else: py.click(x=533, y=Y, clicks=2) #Open het gevraagde bedrijfsbezoek
    time.sleep(3)
    
    #Nagaan of er al een gevarenlijst aanwezig is in "Checklist".
    #Indien er al een gevarenlijst aanwezig is moet er geen tweede gemaakt woren en mag het venster gesloten worden.
    py.click(x=76, y=226, clicks=2) #Klikt op "Checklist"
    time.sleep(8) #Relatief veel tijd geven, als er veel checklijsten instaan kan het lang duren om te openen.
    py.click(x=90, y=770) #Klikt ergens anders zodat de checklijst van de bedrijfsgevaren niet in het blauw wordt gemarkeerd, anders maakt OCR fouten.
    time.sleep(1)
    if OCRproductie.checkAanwezigheidGevarenlijst() == True:
        time.sleep(1)
        py.click(x=326, y=104) #Sluit het venster.
        return False

    time.sleep(2)
    py.click(x=91, y=293) #Open "bewaarde documenten".
    time.sleep(5)

    #De omschrijvingen sorteren van Z-A: kans groter dat het verslag bovenaan komt te staan.
    py.click(x=333, y=186, clicks=2, interval=1)
    py.moveTo(x=86, y=609) #Zorgt ervoor dat de muis niet voor de screenshot komt te staan.
    time.sleep(1)

    #Checken of een verslag van het bedrijfsbezoek aanwezig is in "bewaarde documenten".
    if OCRproductie.checkAanwezigheidVerslag() == True:
        #Open het verslag (Word document).
        py.click(x=599, y=208, clicks=2)
        return True
    else:
        #De bedrijfsbezoeken die geen verslag verkennend bedrijfsbezoek hebben bijgehouden in "Bedrijfsbezoeken.txt" noteren
        bedrijfsbezoekNoteren()
        py.click(x=326, y=104) #Sluit het venster.
        return False

#Maakt nieuwe gevarenlijst aan bij "checklist".
def openNieuweLijst():
    time.sleep(0.5)
    py.click(x=90, y=223) #Open "Checklist"
    time.sleep(2)
    py.click(x=182, y=159) #Druk op de "+" knop
    time.sleep(5) #Tijdelijk hoger om tijd te geven om het manueel te doen.
    py.press("down", presses=12, interval=0.1) #IN DE TESTOMGEVING MANUEEL DOEN
    time.sleep(1)
    py.click(x=747, y=576) #Klik op de save knop
    time.sleep(2)

#De bedrijfsbezoeken die geen verslag verkennend bedrijfsbezoek hebben bijgehouden in "Bedrijfsbezoeken.txt" noteren
def bedrijfsbezoekNoteren():
    py.click(x=77, y=185) #Navigeren naar "Algemeen".
    time.sleep(2)
    fileBedrijfsbezoeken = open("Bedrijfsbezoeken.txt", "a") #Open de .txt file.
    bedrijfsbezoek = OCRproductie.retrieveBedrijfsbezoek() #Referentie van het bedrijfsbezoek extraheren uit H@W.
    fileBedrijfsbezoeken.write("{}\n".format(bedrijfsbezoek)) #Bedrijfsbezoek noteren die niet in orde is in de "Bedrijfsbezoeken.txt" file.
    fileBedrijfsbezoeken.close()
