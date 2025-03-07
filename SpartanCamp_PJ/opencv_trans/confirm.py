import cv2
import face_recognition


original_face_img = "images/man.png"
face_img = face_recognition.load_image_file(original_face_img)
face_landmarks_list = face_recognition.face_landmarks(face_img)

# print(face_landmarks_list)
face_image = cv2.imread(original_face_img)

# chin
print(face_landmarks_list[0]["chin"])
for chin_coordinate in face_landmarks_list[0]["chin"]:
    cv2.drawMarker(
        face_image,
        chin_coordinate,
        color=(255, 0, 0),
        markerType=cv2.MARKER_CROSS,
        thickness=1,
    )

# left_eye
print(face_landmarks_list[0]["left_eye"])
for left_eye_coordinate in face_landmarks_list[0]["left_eye"]:
    cv2.drawMarker(
        face_image,
        left_eye_coordinate,
        color=(255, 0, 0),
        markerType=cv2.MARKER_CROSS,
        thickness=1,
    )


cv2.imshow("Image", face_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
