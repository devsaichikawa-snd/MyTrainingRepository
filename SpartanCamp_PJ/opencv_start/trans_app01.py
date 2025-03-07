import cv2
from PIL import Image


# 使用する画像を格納する
original_face_img = "images/man.png"
original_mask_img = "images/otahuku.png"


def find_face():
    # 顔検出の分類器を用意
    cascade_file = "haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(cascade_file)
    img = cv2.imread(original_face_img)
    face_list = cascade.detectMultiScale(img)

    return face_list


face_list = find_face()
# def paste_img(face_list):
x = face_list[0][0]  # X座標
y = face_list[0][1]  # Y座標
w = face_list[0][2]  # 横幅
h = face_list[0][3]  # 縦幅

# Pillowで画像を開く
face_img = Image.open(original_face_img)
mask_img = Image.open(original_mask_img)
# face_img = cv2.imread(original_face_img)
# mask_img = cv2.imread(original_mask_img)

# 顔に合ったサイズに画像をリサイズしてフォルダに保存
# resized_mask_img = cv2.resize(mask_img, dsize=(w, h))
resized_mask_img = mask_img.resize(w, h)
# cv2.imwrite("images/resize_otahuku.png", resized_mask_img)

# マスク画像を顔に貼り付けるのと、背景透過のためのsplit()
# 画像の貼り付けはPillowを使用した方がシンプルで簡単なのでこちらを使用します
# face_img[y : h + y, x : w + x] = cv2.imread("images/resize_otahuku.png")
face_img.paste(resized_mask_img, (x, y), resized_mask_img)
# フォルダの中に保存される
face_img.save("images/hensin_pillow.png")
# cv2.imwrite("images/hensin.png", face_img)


# def show_img():
#     # 画像を表示させる
#     cv2.imshow('face', face_img)
#     # waitKey(0)で画像上で何かしらのキーを押せば閉じられるようにする
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


# def main():
#     face_list = find_face()
#     paste_img(face_list)
#     face_img = cv2.imread("images/hensin.png")
# show_img(face_img)


# if __name__ == "__main__":
#     main()
