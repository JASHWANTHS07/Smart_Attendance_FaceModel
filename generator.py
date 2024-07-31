import os
import cv2
import numpy as np
import dlib


shape_predictor_path = "Dat_files/shape_predictor_68_face_landmarks.dat"

face_recognition_model_path = "Dat_files/dlib_face_recognition_resnet_model_v1.dat"


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(shape_predictor_path)
face_recognizer = dlib.face_recognition_model_v1(face_recognition_model_path)

def save_face_descriptors(input_folder, output_folder):

    os.makedirs(output_folder, exist_ok=True)

    print("Reading...")
    print()
    for person_name in os.listdir(input_folder):
        print(person_name)
        person_input_folder = os.path.join(input_folder, person_name)
        if os.path.isdir(person_input_folder):  # Check if it's a directory
            person_output_folder = os.path.join(output_folder, person_name)
            os.makedirs(person_output_folder, exist_ok=True)
            print("Iterating...")


            img_files = [f for f in os.listdir(person_input_folder) if f.endswith('.jpg') or f.endswith('.png')]

            if len(img_files) == 0:
                print(f"No image files found in {person_input_folder}. Skipping augmentation for {person_name}.")
                continue

            print("Loading...")
            for img_file in img_files:
                img_path = os.path.join(person_input_folder, img_file)
                if os.path.isfile(img_path):  # Check if it's a file
                    img = cv2.imread(img_path)
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = detector(gray)
                    for face in faces:

                        shape = predictor(gray, face)

                        face_descriptor = face_recognizer.compute_face_descriptor(img, shape, num_jitters=0)

                        np.save(os.path.join(person_output_folder, f"{img_file[:-4]}_descriptor.npy"), face_descriptor)
                        print(f"Saved face descriptor for {person_name} - {img_file}")
                else:
                    print(f"{img_path} is not a file. Skipping.")

        else:
            print(f"{person_input_folder} is not a directory. Skipping.")

def main():
    input_folder = 'single_image_folder'
    output_folder = 'face_descriptors'


    save_face_descriptors(input_folder, output_folder)
    print("Face descriptors saved successfully.")

if __name__ == "__main__":
    main()
