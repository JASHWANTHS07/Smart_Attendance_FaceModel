import cv2
import numpy as np
from imutils import face_utils
import dlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("Dat_files/shape_predictor_68_face_landmarks.dat")

image = cv2.imread("images/Prajwal.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = detector(gray, 0)
for face in faces:
    shape = predictor(gray, face)
    shape = face_utils.shape_to_np(shape)

    nose = shape[30]
    left_eye = shape[36:42].mean(axis=0)
    right_eye = shape[42:48].mean(axis=0)

    eye_center = ((left_eye[0] + right_eye[0]) // 2, (left_eye[1] + right_eye[1]) // 2)
    nose_3d = np.array([nose[0], nose[1], 0])
    left_eye_3d = np.array([left_eye[0], left_eye[1], 0])
    right_eye_3d = np.array([right_eye[0], right_eye[1], 0])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(nose_3d[0], nose_3d[1], nose_3d[2], c='r', marker='o', label='Nose')
    ax.scatter(left_eye_3d[0], left_eye_3d[1], left_eye_3d[2], c='b', marker='o', label='Left Eye')
    ax.scatter(right_eye_3d[0], right_eye_3d[1], right_eye_3d[2], c='g', marker='o', label='Right Eye')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Face Model')
    ax.legend()

    plt.show()
