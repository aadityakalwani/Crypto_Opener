# ciao
# may the coding begin

import webbrowser
import time
import pyautogui


def open_crypto():
    pyautogui.keyDown("command")
    pyautogui.keyDown("space")
    time.sleep(0.25)
    pyautogui.keyUp("space")
    pyautogui.keyUp("command")
    time.sleep(0.25)
    pyautogui.write("chrome", interval=0.25)
    time.sleep(0.25)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.keyDown("command")
    pyautogui.keyDown("n")
    time.sleep(0.25)
    pyautogui.keyUp("n")
    pyautogui.keyUp("command")
    time.sleep(1)

    webbrowser.open_new("https://alpha.multifarm.fi/assets")
    time.sleep(0.5)
    webbrowser.open_new("https://dailydefi.org/tools/impermanent-loss-calculator/")
    time.sleep(0.5)
    webbrowser.open_new("https://pancakeswap.finance/")
    time.sleep(0.5)
    webbrowser.open_new("https://apeswap.finance/")
    time.sleep(0.5)
    webbrowser.open_new("https://app.barbecueswap.finance/")
    time.sleep(0.5)
    webbrowser.open_new("https://bear.honeyfarm.finance/")
    time.sleep(0.5)
    webbrowser.open_new("https://cobraswap.finance/")

    print("done")


open_crypto()
