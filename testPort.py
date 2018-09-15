#import coordinates_Solundir
from selenium import webdriver
import time
import pyautogui

outerCircle = open('C:\\Users\\Automasjon\\PycharmProjects\\infoscreen\\outerCircle.txt', 'r')
outerCircle = int(outerCircle.read())

innerCircle = open('C:\\Users\\Automasjon\\PycharmProjects\\infoscreen\\innerCircle.txt', 'r')
innerCircle = int(innerCircle.read())

#LAT = float(coordinates_Solundir.getLat())
#LON = float(coordinates_Solundir.getLon())

LAT = 60.1
LON = 6



if LAT > 59.92 and LAT < 61.98 and LON > 4.80 and LON < 5.1 and outerCircle == 0:
    time.sleep(5)
    pyautogui.keyDown('ctrlleft')
    pyautogui.press('tab')

    outerCircle = open('C:\\Users\\Automasjon\\PycharmProjects\\infoscreen\\outerCircle.txt', 'w')
    outerCircle.write('1')
    outerCircle.close()

    print('Solundir er innenfor ytre sirkel')


if LAT > 60.0 and LAT < 60.2 and LON > 4.9 and LON < 5.1 and innerCircle == 0:
    time.sleep(5)
    pyautogui.keyDown('ctrlleft')
    pyautogui.press('tab')

    innerCircle = open('C:\\Users\\Automasjon\\PycharmProjects\\infoscreen\\innerCircle.txt', 'w')
    innerCircle.write('1')
    innerCircle.close()



    print('Solundir er innenfor indre sirkel')

if LAT < 59.92 or LAT > 61.98 or LON < 4.80 or LON > 5.1 and outerCircle == 1 and innerCircle == 1:
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
