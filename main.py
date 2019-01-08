#import coordinates_Solundir
#from selenium import webdriver
import time
#import pyautogui
import rangePorts
import getcoordinates
import popup

# Please specify where the .txt files for inner and outer circle should be

innerCircleFilePath = "/home/pi/Infoscreen/innerCircle.txt"
outerCircleFilePath = "/home/pi/Infoscreen/outerCircle.txt"
try:
    outerCircle = open(outerCircleFilePath, 'r')    #Tries to open .txt file if it exists
except FileNotFoundError:
    outerCircle = open(outerCircleFilePath, 'w')    #Makes a new .txt file if it doesnt exists
    outerCircle.write('0')
    outerCircle.close()
    outerCircle = open(outerCircleFilePath, 'r')    #Opens the newly made txt file
outerCircle = int(outerCircle.read())

try:
    innerCircle = open(innerCircleFilePath, 'r')    #Tries to open .txt file if it exists
except FileNotFoundError:
    innerCircle = open(innerCircleFilePath, 'w')    #Makes a new .txt file if it doesnt exists
    innerCircle.write('0')
    innerCircle.close()
    innerCircle = open(innerCircleFilePath, 'r')    #Opens the newly made txt file
innerCircle = int(innerCircle.read())

#LAT = float(coordinates_Solundir.getLat())
#LON = float(coordinates_Solundir.getLon())

#LAT = rangePorts.SolundirLAT
#LON = rangePorts.SolundirLON

LON = getcoordinates.longitude
LAT = getcoordinates.latitude


###############################################################
if  rangePorts.isMjomnaOuterring() == 1 and outerCircle == 0:
    time.sleep(5)
    #pyautogui.keyDown('ctrlleft')
    #pyautogui.press('tab')

    outerCircle = open(outerCircleFilePath, 'w')
    outerCircle.write('1')
    outerCircle.close()
    print('Solundir er innenfor ytre ring')



if rangePorts.isMjomnaInnerring() == 1 and innerCircle == 0:
    time.sleep(5)
    #pyautogui.keyDown('ctrlleft')
    #pyautogui.press('tab')

    innerCircle = open(innerCircleFilePath, 'w')
    innerCircle.write('1')
    innerCircle.close()
    print('Solundir er innenfor indre ring')



if rangePorts.isMjomnaOuterring() == 0 and innerCircle == 1:
    time.sleep(5)
    #pyautogui.keyDown('ctrlleft')
   #pyautogui.press('tab')

    innerCircle = open(innerCircleFilePath, 'w')
    innerCircle.write('0')
    innerCircle.close()

    outerCircle = open(outerCircleFilePath, 'w')
    outerCircle.write('0')
    outerCircle.close()

    print('Solundir er utenfor igjen.')
##########################################################
if  rangePorts.isBergenOuterring() == 1 and outerCircle == 0:
    time.sleep(5)
    #pyautogui.keyDown('ctrlleft')
    #pyautogui.press('tab')

    outerCircle = open(outerCircleFilePath, 'w')
    outerCircle.write('1')
    outerCircle.close()
    print('Solundir er innenfor ytre ring')


if rangePorts.isBergenInnerring() == 1 and innerCircle == 0:
    time.sleep(5)
    #pyautogui.keyDown('ctrlleft')
    #pyautogui.press('tab')

    innerCircle = open(innerCircleFilePath, 'w')
    innerCircle.write('1')
    innerCircle.close()
    print('Solundir er innenfor indre ring')
    popup.Bergen()




if rangePorts.isBergenOuterring() == 0 and innerCircle == 1:
    time.sleep(5)
    #pyautogui.keyDown('ctrlleft')
   #pyautogui.press('tab')

    innerCircle = open(innerCircleFilePath, 'w')
    innerCircle.write('0')
    innerCircle.close()

    outerCircle = open(outerCircleFilePath, 'w')
    outerCircle.write('0')
    outerCircle.close()

    print('Solundir er utenfor igjen.')
