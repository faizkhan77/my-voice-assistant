import pyautogui as gui
import time
import pywhatkit

message = input("Enter the message: ")
num_value = input("Enter num of times: ")

time.sleep(5)

def test():
    for i in range(int(num_value)):
        gui.typewrite(message)  
        gui.press('Enter')

pywhatkit.sendwhatmsg(test(), message, 17, 57)