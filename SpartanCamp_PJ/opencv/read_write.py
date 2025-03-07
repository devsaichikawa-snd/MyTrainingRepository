import cv2


# 画像ファイルの読込
# img = cv2.imread("images/cat.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.imread("images/cat.jpg")
print(img.shape)
resize_img = cv2.resize(img, dsize=(768 // 2, 432 // 2))
cv2.imwrite("images/resize_cat.jpg", resize_img)
# 画像に文字を描画する
cv2.putText(
    img,
    text="CAT !!!",
    org=(100, 200),
    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=5,
    color=(255, 255, 0),
    thickness=3,
)
# 画像を表示
# cv2.imshow("Image", img)

# 待ち時間(キー操作を待つ)
# cv2.waitKey(5000)  # 5000=5秒

# 画像ファイルの書込(保存)
# cv2.imwrite("images/new_cat.jpg", img)
