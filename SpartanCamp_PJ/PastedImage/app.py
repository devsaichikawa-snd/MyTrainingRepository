"""要件
顔画像の両目を識別し、そこに目の画像をリサイズして貼り付ける
(目の識別は公式からカスケードファイル(haarcascade_eye.xml)をダウンロードしてきて使用すること)
貼り付けた目の画像の透過処理を行う
"""
import cv2
import face_recognition
import numpy as np
from PIL import Image


# 使用する画像を格納する
original_woman_image = "images/face_img.png"
eye_image = "images/eye_img.png"


def show_img(face_img):
    """画像を表示する
    Param: 読み込みたい画像
    """
    cv2.imshow("face", face_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def find_face():
    """顔を検出する関数
    カスケード分類器とは、、、
    物体検出を行うためには検出したい物体がどんな特徴を持っているのか、
    該当する物体を含む画像と含まない画像（＝学習用画像）を用意し、検出したい物体の特徴を抽出します。
    この特徴を「特徴量」と呼びますが、学習用画像すべての「特徴量」をまとめたデータのことを
    「カスケード分類器」と呼びます。
    """
    # カスケードファイルを指定して、分類機を作成
    cascade_file = "haarcascade_eye.xml"
    cascade = cv2.CascadeClassifier(cascade_file)
    # 画像を読み込み、グレイスケール(白黒)に変換
    img = cv2.imread(original_woman_image)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 顔検出
    face_list = cascade.detectMultiScale(img_gray)

    return face_list


def find_face_part(face_part_name):
    """顔の各パーツの座標を取得する
    Param: 指定する顔のパーツの物理名称
    Return: 取得したパーツの座標
    """
    # Face Recognitionで顔画像を読み込む
    face_image = face_recognition.load_image_file(original_woman_image)
    # 顔画像から顔の各部位の座標を検出する
    face_landmarks_list = face_recognition.face_landmarks(face_image)
    # face_part_nameで指定した顔の部位の座標を検出する
    face_part_name_landmarks = face_landmarks_list[0][face_part_name]

    return face_part_name_landmarks


def eye_pasteing(face_list):
    """対象画像に指定した画像をResizeして貼り付ける
    Param: 顔のパーツの座標が格納されたList
    """
    # pillowで対象の画像を開く
    face_img = Image.open(original_woman_image)
    eye_img = Image.open(eye_image)

    # 右目
    right_eye_x = face_list[2][0]  # X座標
    right_eye_y = face_list[2][1]  # Y座標
    right_eye_w = face_list[2][2]  # 横幅
    right_eye_h = face_list[2][3]  # 縦幅

    # Resizeと保存
    resize_right_eye_img = eye_img.resize((right_eye_w, right_eye_h))
    resize_right_eye_img.save("images/resized_r_eye_img.png")
    # 貼付
    face_img.paste(
        resize_right_eye_img,
        (right_eye_x, right_eye_y),
        resize_right_eye_img.split()[3],
    )

    # 左目
    left_eye_x = face_list[1][0]  # X座標
    left_eye_y = face_list[1][1]  # Y座標
    left_eye_w = face_list[1][2]  # 横幅
    left_eye_h = face_list[1][3]  # 縦幅

    # Resizeと保存
    resize_left_eye_img = eye_img.resize((left_eye_w, left_eye_h))
    resize_left_eye_img.save("images/resized_l_eye_img.png")
    # 貼付
    face_img.paste(
        resize_left_eye_img, (left_eye_x, left_eye_y), resize_left_eye_img.split()[3]
    )

    # 出来上がった合体画像を保存
    face_img.save("images/pasted_face_img.png")


def main():
    face_list = find_face()
    face_img = eye_pasteing(face_list)
    show_img(face_img)


if __name__ == "__main__":
    main()


# def paint_face_part(face_part_name_landmarks, face_img):
#     # numpy.ndarray型で座標を指定
#     points = np.array(face_part_name_landmarks)
#     # 取り出した顔のパーツの座標同士を繋ぎ、その間を黒色で塗りつぶす
#     cv2.fillConvexPoly(face_img, points, color=(0, 0, 0))
#     return face_img

# OpenCVで画像の読み込み
# face_img = cv2.imread(original_woman_image)
# face_part_name = "right_eye"
# face_part_name = "left_eye"
# face_part_name_landmarks = find_face_part(face_part_name)
# face_img = paint_face_part(face_part_name_landmarks, face_img)

# 座標にマーカーをつける
# for face_part_name_landmark in face_part_name_landmarks:
#     cv2.drawMarker(
#         face_img,
#         face_part_name_landmark,
#         color=(255, 0, 0),
#         markerType=cv2.MARKER_CROSS,
#         thickness=1,
#     )
# show_img(face_img)
