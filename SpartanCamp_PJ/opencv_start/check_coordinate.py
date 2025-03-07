import cv2


def onMouse(event, x, y, flags, params):
    """
    発生したイベントが「左クリック」だったとき、処理を実行する。
    """
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        return x, y


# 画像を読み込む
img = cv2.imread("images/man.png")
# 画像を表示する
cv2.imshow("Face", img)
# 画像でイベントを実行する
cv2.setMouseCallback("Face", onMouse)
cv2.waitKey(0)
