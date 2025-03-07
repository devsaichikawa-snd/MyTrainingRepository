import pyautogui


left, top, width, height = pyautogui.locateOnScreen("screenshot1.png", confidence=0.1)
print(left, top, width, height)

pyautogui.screenshot("mouse_move.png")
# pyautogui.moveTo(400, 500, 1)
# pyautogui.dragTo(600, 500, button="left")
# pyautogui.click()
# pyautogui.write("hello hiraizumi")
# pyautogui.hotkey("ctrl", "a")
# pyautogui.hotkey("ctrl", "c")
# pyautogui.hotkey("ctrl", "v")
