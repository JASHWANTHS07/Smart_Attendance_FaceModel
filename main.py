import cv2
import pandas as pd
import os
import dlib
import numpy as np
from datetime import datetime
import calendar


face_descriptors_folder = 'face_descriptors'


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("Dat_files/shape_predictor_68_face_landmarks.dat")
face_recognizer = dlib.face_recognition_model_v1("Dat_files/dlib_face_recognition_resnet_model_v1.dat")


face_descriptors = []
names = []
for person_name in os.listdir(face_descriptors_folder):
    person_folder = os.path.join(face_descriptors_folder, person_name)
    if os.path.isdir(person_folder):
        for filename in os.listdir(person_folder):
            descriptor_path = os.path.join(person_folder, filename)
            face_descriptor = np.load(descriptor_path, allow_pickle=True)
            face_descriptors.append(face_descriptor)
            names.append(person_name)


face_descriptors = np.array(face_descriptors)
names = np.array(names)


student_list_file = 'student_list.xlsx'
student_df = pd.read_excel(student_list_file)

all_students = student_df['Name'].tolist()


attendance_df = pd.DataFrame({'Name': all_students, 'Attendance': ['Absent'] * len(all_students), 'Date': [''] * len(all_students), 'Time': [''] * len(all_students)})


def mark_attendance(name):
    global attendance_df
    time_now = datetime.now()
    date = time_now.strftime("%Y-%m-%d")
    time = time_now.strftime("%I:%M %p")  # Hour:Minute AM/PM format
    attendance_df.loc[attendance_df['Name'].str.split().str[0] == name, ['Attendance', 'Date', 'Time']] = ['Present', date, time]



def recognize_faces(frame):
    global attendance_df
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        x1, y1, x2, y2 = face.left(), face.top(), face.right(), face.bottom()

        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)


        shape = predictor(gray, face)


        face_chip = dlib.get_face_chip(frame, shape, size=150)


        face_rgb = cv2.cvtColor(face_chip, cv2.COLOR_BGR2RGB)


        face_descriptor = face_recognizer.compute_face_descriptor(face_rgb)

        if face_descriptors.size > 0:
            face_distances = [np.linalg.norm(face_descriptor - descriptor) for descriptor in face_descriptors]
            min_distance_index = np.argmin(face_distances)
            min_distance = face_distances[min_distance_index]

            if min_distance < 0.6:
                student_name = names[min_distance_index]
                mark_attendance(student_name)

                cv2.putText(frame, f"{student_name} - Present", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
            else:
                cv2.putText(frame, "Unknown", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
        else:
            cv2.putText(frame, "Found faces", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

    return frame


def main():
    global attendance_df
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = recognize_faces(frame)
        cv2.imshow('Attendance System', frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    def save_attendance_to_file(attendance_df):

        today_date = datetime.now()

        # Create the folder structure for year, month, and day
        year_folder = os.path.join("Attendance", str(today_date.year))
        month_folder = os.path.join(year_folder, str(today_date.month))
        day_folder = os.path.join(month_folder, str(today_date.day))


        if not os.path.exists(year_folder):
            os.makedirs(year_folder)


        if not os.path.exists(month_folder):
            os.makedirs(month_folder)


        if not os.path.exists(day_folder):
            os.makedirs(day_folder)


        attendance_file_name = today_date.strftime("%d-%m-%Y") + "_attendance.xlsx"


        attendance_file_path = os.path.join(day_folder, attendance_file_name)


        attendance_df.to_excel(attendance_file_path, index=False)

def save_attendance_to_file(attendance_df):

    today_date = datetime.now()


    year_folder = os.path.join("Attendance", str(today_date.year))
    month_name = calendar.month_name[today_date.month]
    month_folder = os.path.join(year_folder, month_name)


    if not os.path.exists(year_folder):
        os.makedirs(year_folder)


    if not os.path.exists(month_folder):
        os.makedirs(month_folder)


    attendance_file_name = today_date.strftime("%d-%m-%Y") + "_attendance.xlsx"


    attendance_file_path = os.path.join(month_folder, attendance_file_name)


    attendance_df.to_excel(attendance_file_path, index=False)




if __name__ == "__main__":
    main()
    save_attendance_to_file(attendance_df)
