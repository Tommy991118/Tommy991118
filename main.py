from turtle import width
import pyautogui as py
import time 
from PIL import Image
import cv2
import pytesseract
import re
import os
import OCRproductie, checklistGevarenProductie, navigatieProductieomgeving #Andere python files.

#Hoofdfunctie die het script doet starten.
def start():
    time.sleep(5)
    #Open Health@Work en navigeer naar de gewenste bedrijfsbezoeken (datums manueel ingeven).
    navigatieProductieomgeving.openhw()

    #Lange pauze om safe te zijn zodat de foto van het aantal records niet wordt genomen wanneer het nog aan het laden is (als er veel records worden opgevraagd).
    time.sleep(25)

    #Extraheren hoeveel records er zijn opgevraagd ten gevolge van de ingegeven datums.
    aantalRecords = OCRproductie.retrieveAantalRecords()

    """
    Afstandsverschil berekenen tussen de posities van de bedrijfsbezoeken.
    Point(x=520, y=395) - Eerste record
    Point(x=521, y=412) - Tweede record
    y = 412 - 396 = 16 = deltaY
    """

    Y = 395 #Y coördinaat van het eerste bedrijfsbezoek binnen "Overzicht bedrijfsbezoeken".

    #Loopen door de records
    for i in range(1, aantalRecords+2):
        #Er zijn 39 bedrijfsbezoeken per frame van de lijst van bedrijfsbezoeken.
        #Vanaf de 39e bedrijfsbezoek moet de meegegeven Y coördinaat niet meer gewijzigd worden, omdat de bedrijfsbezoeken automatisch verschuiven.
        if i < 39: deltaY = 16
        else: deltaY = 0

        #Navigeer naar de bewaarde documenten.
        #Is True als er een verslag aanwezig is & false indien niet.
        if navigatieProductieomgeving.openVerslag(Y, i, aantalRecords) == True:
            #Wachten tot het Word document wordt geopend.
            time.sleep(10) 

            #Extraheer de GRIM codes van het Word document.
            codes = OCRproductie.wordOCR()

            time.sleep(15) #Tijdelijk zo lang om een Word document ervoor te houden.
            
            #Noteert de bedrijfsbezoeken waarvan het verslag niet in orde was.
            if codes == "NietInOrde":
                navigatieProductieomgeving.bedrijfsbezoekNoteren()

            #Als het geen ABC+ is verder gaan met het opstellen van de gevarenlijst.
            elif codes != "ABC+":
                #Navigeren om een nieuwe gevarenlijst aan te maken.
                navigatieProductieomgeving.openNieuweLijst()
                time.sleep(5)

                #Codes meegeven aan een functie die de bijbehorende gevaren gaat aanvinken.
                checklistGevarenProductie.gevarenAanvinken(codes) #Coördinaten die overeenkomen met de productie omgeving.
                #checklistGevarenTestomgeving.gevarenAanvinken(codes) #Coördinaten die overeenkomen met de test omgeving.
                time.sleep(1)

                #Sluit het venster van het bedrijfsbezoek
                py.click(x=325, y=103)
                time.sleep(2)
            
            #Indien het een ABC+ is, sluit het venster.
            else:
                py.click(x=324, y=103)

        #Nieuwe Y waarde berekenen om het volgende bedrijfsbezoek te selecteren in de volgende iteratie.
        #Zorgt ervoor dat het volgende bedrijfsbezoek wordt geklikt in de volgende iteratie.
        Y = Y + deltaY
        time.sleep(2)