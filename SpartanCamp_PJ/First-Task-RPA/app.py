""" 要件
1. googleの新しいタブを立ち上げ、そこに自動で平泉町 観光と入力し、検索
2. 開いたページのスクリーンショットを撮って、保存
※ ブラウザの立ち上げはwebbrowserを使うこと
※ writeメソッドだと日本語入力ができないので、自身で調べて、日本語入力をすること
※ クリックとクリックの間は少し時間を空ける方が確実なのでtimeモジュールを使用して工夫をすること
"""
import pyautogui
import pyperclip
import time
import webbrowser


# while True:
#     x, y = pyautogui.position()
#     positionStr = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
#     print(positionStr, end="")
#     print("\b" * len(positionStr), end="", flush=True)


# Prepare GoogleURL
url = "https://www.google.com/"


def webbrowserOpen():
    """Open webbrowser"""
    webbrowser.open(url)


def search():
    """search"""
    # Move searchBox
    pyautogui.moveTo(800, 470, 1)

    # Move searchBox
    pyautogui.click()

    # Write Word
    pyperclip.copy("平泉町 観光")
    pyautogui.hotkey("ctrl", "v")

    # conduct enter command
    pyautogui.press("enter")


def screenShot():
    """Conduct screenShot
    Take a image after 3s
    """
    time.sleep(3)
    pyautogui.screenshot("Images/rpa_result.png")


# Conduct browseropen and screenShot
if __name__ == "__main__":
    webbrowserOpen()
    search()
    screenShot()
