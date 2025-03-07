# while True:
#     print("あなたの名前は？")
#     name = input(">>")
#     if name == "bye":
#         break
#     print(name)

import pyautogui


arr = [[1439, 1042, 1], [847, 633, 1], [747, 620, 1]]

for row in arr:
    pyautogui.moveTo(row[0], row[1], row[2])
    pyautogui.click()
# pyautogui.moveTo(1439, 1042, 1)
# pyautogui.click()

# pyautogui.moveTo(847, 633, 1)
# pyautogui.click()

# pyautogui.moveTo(747, 620, 1)
# pyautogui.click()
