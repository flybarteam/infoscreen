#import coordinates_Solundir
#from selenium import webdriver
import time
import pyautogui
import testrange


# Please specify where the .txt files for inner and outer circle should be

innerCircleFilePath = "F:\\Infoscreen\\innerCircle.txt"
outerCircleFilePath = "F:\\Infoscreen\\outerCircle.txt"
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

LAT = testrange.SolundirLAT
LON = testrange.SolundirLON



if  testrange.isMjomnaOuterring() == 1 and outerCircle == 0:
    time.sleep(5)
    #pyautogui.keyDown('ctrlleft')
    #pyautogui.press('tab')

    outerCircle = open(outerCircleFilePath, 'w')
    outerCircle.write('1')
    outerCircle.close()

    print('Solundir er innenfor ytre sirkel')


if testrange.isMjomnaInnerring() == 1 and innerCircle == 0:
    time.sleep(5)
    #pyautogui.keyDown('ctrlleft')
    #pyautogui.press('tab')

    innerCircle = open(innerCircleFilePath, 'w')
    innerCircle.write('1')
    innerCircle.close()



    print('Solundir er innenfor indre sirkel')

if testrange.isMjomnaOuterring() == 0 and innerCircle == 1:
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

print(testrange.isMjomnaOuterring())