#import coordinates_Solundir
#from selenium import webdriver
import time
import pyautogui
import testrange

outerCircle = open('C:\\Users\\Automasjon\\PycharmProjects\\infoscreen\\outerCircle.txt', 'r')
outerCircle = int(outerCircle.read())
innerCircle = open('C:\\Users\\Automasjon\\PycharmProjects\\infoscreen\\innerCircle.txt', 'r')
innerCircle = int(innerCircle.read())

#LAT = float(coordinates_Solundir.getLat())
#LON = float(coordinates_Solundir.getLon())

LAT = testrange.SolundirLAT
LON = testrange.SolundirLON



if  testrange.isMjomnaOuterring() == 1 and outerCircle == 0:
    time.sleep(5)
    pyautogui.keyDown('ctrlleft')
    pyautogui.press('tab')

    outerCircle = open('C:\\Users\\Automasjon\\PycharmProjects\\infoscreen\\outerCircle.txt', 'w')
    outerCircle.write('1')
    outerCircle.close()

    print('Solundir er innenfor ytre sirkel')


if testrange.isMjomnaInnerring() == 1 and innerCircle == 0:
    time.sleep(5)
    pyautogui.keyDown('ctrlleft')
    pyautogui.press('tab')

    innerCircle = open('C:\\Users\\Automasjon\\PycharmProjects\\infoscreen\\innerCircle.txt', 'w')
    innerCircle.write('1')
    innerCircle.close()



    print('Solundir er innenfor indre sirkel')

if testrange.isMjomnaOuterring() == 0 and innerCircle == 1:
    time.sleep(5)
    pyautogui.keyDown('ctrlleft')
    pyautogui.press('tab')

    innerCircle = open('C:\\Users\\Automasjon\\PycharmProjects\\infoscreen\\innerCircle.txt', 'w')
    innerCircle.write('0')
    innerCircle.close()

    outerCircle = open('C:\\Users\\Automasjon\\PycharmProjects\\infoscreen\\outerCircle.txt', 'w')
    outerCircle.write('0')
    outerCircle.close()

    print('Solundir er utenfor igjen.')

print(testrange.isMjomnaOuterring())