from turtle import width
import numpy as np
import pandas as pd
import pyautogui as py
import time
from PIL import Image
import cv2
import pytesseract
import re

#Indien deze functie niet werkt en daardoor het script stops, probeer een andere tijdsperiode te nemen: langer of korter.
#Extraheren hoeveel records er zijn voor de ingegeven datums.
#Nodig voor de for loop.
def retrieveAantalRecords():
    #Coördinaten op basis waarvan de screenshot wordt genomen van het aantal records. 
    left = 373
    top = 1012
    width = 36
    height = 17

    #OCR toepassen om het aantal records op te vragen.
    #Andere psm hier omdat het één getal is, dan werkt psm 8 beter.
    path_to_tesseract = r"C:\Users\xtmsls\AppData\Local\Tesseract-OCR\tesseract.exe"
    myconfig = r"--psm 8 --oem 3"
    pytesseract.pytesseract.tesseract_cmd = path_to_tesseract
    im = py.screenshot("AantalRecords.png", region=(left, top, width, height))
    records = pytesseract.image_to_string(im, config=myconfig)
    aantalRecords = re.sub("\D", "", records)
    aantalRecords = re.sub(r" ", "", aantalRecords)
    print(aantalRecords)
    return int(aantalRecords) #Geeft aantal records weer die zijn opgevraagd door de gegeven datums.

#Extraheert de GRIM codes van het verslag (Word document)
def wordOCR():
    time.sleep(10)

    #Hier nagaan of het een NL, FR of ABC+ document is, op basis daarvan de gepaste py.write doorgeven.
    if checkTaalVerslag() == "NL":
        py.hotkey("ctrl", "f")
        time.sleep(3)
        py.write("Overzicht van de aanwezige gevaren", interval=0.02)
    elif checkTaalVerslag() == "FR":
        py.hotkey("ctrl", "f")
        time.sleep(3)
        py.write("Cartographie de dangers", interval=0.02)
    else:
        #Anders is het een ABC+
        py.hotkey("alt", "f4") #Sluit het verslag, kunnen hier geen gevarenlijst voor opstellen.
        time.sleep(2)
        return "ABC+"

    time.sleep(5)

    #Coördinaten om een screenschot te nemen van de opgelijste gevaren.
    left = 580
    top = 161
    width = 1030
    height = 856

    #Scrollen om de volledige eerste pagina te krijgen.
    py.scroll(-650)
    time.sleep(1)

    #OCR toepassen
    #Pytesseract configureren
    path_to_tesseract = r"C:\Users\xtmsls\AppData\Local\Tesseract-OCR\tesseract.exe"
    myconfig = r"--psm 11 --oem 3"
    pytesseract.pytesseract.tesseract_cmd = path_to_tesseract

    #Eerste screenshot nemen.
    im1 = py.screenshot("my_screenshot1.png", region=(left, top, width, height))
    text1 = pytesseract.image_to_string(im1, config=myconfig)
    time.sleep(1)

    #Naar de tweede pagina scrollen waar mogelijk nog gevaren staan.
    py.scroll(-1850)
    time.sleep(2)

    #Tweede screenshot nemen.
    im2 = py.screenshot("my_screenshot2.png", region=(left, top, width, height))
    text2 = pytesseract.image_to_string(im2, config=myconfig)
    time.sleep(2)

    #Sluit het verslag.
    py.hotkey("alt", "f4") #Tijdelijk af om in de testomgeving te werken.

    #Alle gevaren combineren in één string.
    text = text1 + text2

    #Nieuwe variabele om na te gaan of het gevaar "Bedelving, verdrinking en pletgevaar" voorkomt.
    pletgevaar = ""

    #"Bedelving, verdrinking en pletgevaar" heeft dezelfde GRIM code als "Nood- en vluchtwegen"
    #Daarom wordt deze veranderd naar een andere code zodat dat alle gevaren unieke codes hebben.
    if ("pletgevaar" in text) or ("noyade" in text): pletgevaar = "1000021"

    #Tekst preprocessen om alleen cijfers over te houden. 
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r" ", "", (text))
    codes = re.findall("\d+.", text)
    #Zelfgemaakte unieke code voor pletgevaar toevoegen aan de lijst van GRIM codes van het document.
    if pletgevaar == "1000021": 
        codes.append(pletgevaar)
        #Werkelijke code van pletgevaar verwijderen, anders wordt "Nood- en vluchtwegen" ook aangeduid.
        codes.remove("1000020")
    
    #Alle grim codes van de gevaren.
    grimCodes = ['3030001', '3030002', '3030209', '3030003', '3030004', '3030005', '3030006', '3013300', '3010001', '3010002', '3010705', '3010003', '3010004', '3010005', '3013600', '3020100', '3020600', '3020700', '3020705', '3020703', '3020706', '3020707', '3020903', '3020901', '3020902', '3020800', '3020300', '7000013', '3040200', '3040301', '3040302', '3040303',
'3040304', '3040100', '3050001', '3050207', '3050208', '7000001', '7000002', '7000003', '7000004', '7000005', '7000006', '7000007', '7000008', '7000009', '7000010', '7000011', '7000012', '1000006', '1000012', '1000013', '1000014', '1000015', '1000016', '1000017', '1000018', '1000019', '1000020', '3020500', '1000020', '1000011', '3050308']

    #Nakijken of er wel GRIM codes aanwezig waren in het Word document. Indien dat niet zo is, is dit document niet in orde. 
    #Check geeft True of False als er een code van het Word document voorkomt in de lijst van grimCodes.
    check = any(item in codes for item in grimCodes)

    if check == True: return codes
    else: return "NietInOrde"

#Nagaan of het NL, FR of ABC+ is.
def checkTaalVerslag():
    """
    Point(x=731, y=178) Linksboven
    Point(x=1523, y=619) Rechtsonder
    """
    #Coördinaten om een screenshot te nemen van de eerste pagina van het Word document.
    #Op basis daarvan nagaan of het NL of FR is.
    left = 731
    top = 178
    width = 792
    height = 441

    #OCR toepassen om na te gaan of er een verslag aanwezig is.
    path_to_tesseract = r"C:\Users\xtmsls\AppData\Local\Tesseract-OCR\tesseract.exe"
    myconfig = r"--psm 11 --oem 3"
    pytesseract.pytesseract.tesseract_cmd = path_to_tesseract
    im = py.screenshot("verslagWord.png", region=(left, top, width, height))
    verslag = pytesseract.image_to_string(im, config=myconfig)
    
    if ("reconnaissance" in verslag):
        return "FR"
    elif ("verkennend" in verslag):
        return "NL"
    else:
        return "ABC+"

#Nakijken of er al een checklist van de bedrijfsgevaren aanwezig is.
def checkAanwezigheidGevarenlijst():
    """
    Point(x=196, y=200) Linksboven
    Point(x=398, y=266) Rechtsonder
    """
    #Coördinaten die gebruikt worden om een screenshot te nemen van de checklijsten in "Checklist".
    """ Productieomgeving
    left = 196
    top = 200
    width = 202
    height = 66
    """
    
    left = 291
    top = 199
    width = 391-291
    height = 265-199
    
    #OCR toepassen om na te gaan of er een verslag aanwezig is.
    path_to_tesseract = r"C:\Users\xtmsls\AppData\Local\Tesseract-OCR\tesseract.exe"
    myconfig = r"--psm 11 --oem 3"
    pytesseract.pytesseract.tesseract_cmd = path_to_tesseract
    im = py.screenshot("gevarenlijst.png", region=(left, top, width, height))
    checklijsten = pytesseract.image_to_string(im, config=myconfig)
    #Checken als er al een gevarenlijst in staat of als er al een ABC+ verslag staat.
    if ("gevaren" in checklijsten) or ("Screening" in checklijsten): return True
    else: return False

#Nagaan of er een verslag van het bedrijfsbezoek aanwezig is bij de bewaarde documenten.
#Indien deze functie "Verslag" of "Rapport" niet zou herkennen kunnen de coördinaten best gewijzigd worden zodanig dat er een kleinere screenshot wordt genomen.
#Dan is de kans veel groter dat Pytesseract het woord "Verslag" of "Rapport" accurater kan omzetten in een string. 
def checkAanwezigheidVerslag():
    """
    Point(x=294, y=199) Linksboven
    Point(x=393, y=214) Rechtsonder
    """
    #Coördinaten om een screenshot te nemen van de documenten in "bewaarde documenten".
    left = 294
    top = 199
    width = 99
    height = 16

    #OCR toepassen om na te gaan of er een verslag aanwezig is.
    path_to_tesseract = r"C:\Users\xtmsls\AppData\Local\Tesseract-OCR\tesseract.exe"
    myconfig = r"--psm 11 --oem 3"
    pytesseract.pytesseract.tesseract_cmd = path_to_tesseract
    im = py.screenshot("verslagHW.png", region=(left, top, width, height))
    verslag = pytesseract.image_to_string(im, config=myconfig)

    #"Versilag" in test omgeving gebruiken en "Verslag" in productie omgeving.
    # if ("Rapport" in verslag) or ("Versilag" in verslag): return True 
    # else: return False
    if ("Rapport" in verslag) or ("Versilag" in verslag): return True 
    else: return False



def retrieveBedrijfsbezoek():
    left = 298
    top = 181
    width = 337
    height = 17

    #OCR toepassen om na te gaan of er een verslag aanwezig is.
    path_to_tesseract = r"C:\Users\xtmsls\AppData\Local\Tesseract-OCR\tesseract.exe"
    myconfig = r"--psm 11 --oem 3"
    pytesseract.pytesseract.tesseract_cmd = path_to_tesseract
    im = py.screenshot("bedrijfsbezoek.png", region=(left, top, width, height))
    bedrijfsbezoek = pytesseract.image_to_string(im, config=myconfig)

    #Tekst preprocessen: alleen cijfers overhouden. 
    bedrijfsbezoek = re.sub(r"[^\w\s]", "", bedrijfsbezoek)
    bedrijfsbezoek = re.sub(r" ", "", (bedrijfsbezoek))
    bedrijfsbezoek = re.findall("\d+.", bedrijfsbezoek)

    return bedrijfsbezoek