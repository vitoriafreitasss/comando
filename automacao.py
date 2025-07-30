import mouseinfo, pyautogui, time

#mouseinfo.mouseInfo()

pyautogui.moveTo(1275,1052, duration=2)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(644,376, duration=2)
pyautogui.click()
pyautogui.write("imagens de bolo")
