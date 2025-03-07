import cv2


# 動画を読み込む
# cap = cv2.VideoCapture("images/kuma.mp4")
cap = cv2.VideoCapture(0)

# 動画ファイル保存用の設定
fps = int(cap.get(cv2.CAP_PROP_FPS))  # カメラのFPSを取得
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # カメラの横幅を取得
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # カメラの縦幅を取得
fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")  # 動画保存時のfourcc設定（mp4用）
video = cv2.VideoWriter(
    "images/video.mp4", fourcc, fps, (w, h)
)  # 動画の仕様（ファイル名、fourcc, FPS, サイズ）


while True:
    ret, frame = cap.read()
    # print(ret, frame)
    if ret is False:
        break
    cv2.imshow("Image", frame)
    video.write(frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()


# cv2.imshow("Image", frame)
# cv2.waitKey(0)
cv2.destroyAllWindows()
