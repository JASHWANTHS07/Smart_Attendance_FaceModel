# Smart Face Attendance Using Face Model

## Project Overview

The Smart Face Attendance system leverages computer vision and facial recognition technology to automatically mark the attendance of students. It consists of three main scripts:

1. `main.py`: Captures video frames from a webcam, detects faces, recognizes known faces, and updates an attendance record accordingly.
2. `Generator.py`: Generates face descriptors from images and saves them for later use in face recognition.
3. `Test.py`: A simple script to load and print a face descriptor for testing purposes.

## Requirements

### Software

- Python 3.x
- OpenCV
- dlib
- numpy
- pandas
- openpyxl

### Hardware

- A computer with a webcam

### Pre-trained Models

- `shape_predictor_68_face_landmarks.dat`
- `dlib_face_recognition_resnet_model_v1.dat`

These pre-trained models are necessary for facial landmark detection and face recognition. They can be downloaded from the official dlib website or other trusted sources.

## Directory Structure

```
project_folder/
│
├── Dat_files/
│   ├── shape_predictor_68_face_landmarks.dat
│   └── dlib_face_recognition_resnet_model_v1.dat
│
├── face_descriptors/
│   ├── person1/
│   │   ├── descriptor1.npy
│   │   ├── descriptor2.npy
│   ├── person2/
│   │   ├── descriptor1.npy
│   │   ├── descriptor2.npy
│
├── single_image_folder/
│   ├── person1/
│   │   ├── image1.jpg
│   │   ├── image2.png
│   ├── person2/
│   │   ├── image1.jpg
│   │   ├── image2.png
│
├── student_list.xlsx
├── main.py
├── Generator.py
├── Test.py
└── README.md
```

- `Dat_files/` contains the pre-trained models.
- `face_descriptors/` contains numpy files for face descriptors of known persons.
- `single_image_folder/` contains images of individuals to generate face descriptors.
- `student_list.xlsx` is an Excel file containing the list of students.

## Setup and Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/JASHWANTHS07/Smart_Attendance_FaceModel.git
   cd Smart_Attendance_FaceModel
   ```

2. **Install the required packages:**

   ```sh
   pip install opencv-python dlib numpy pandas openpyxl
   ```

3. **Download the pre-trained models:**

   - Place `shape_predictor_68_face_landmarks.dat` and `dlib_face_recognition_resnet_model_v1.dat` in the `Dat_files/` directory.

4. **Prepare face descriptors:**

   - Place the face descriptor files of known individuals in the respective subfolders within the `face_descriptors/` directory.

5. **Prepare student list:**

   - Create or update `student_list.xlsx` with the names of students in a column named 'Name'.

## Usage

### 1. Generating Face Descriptors

Before running the attendance system, you need to generate face descriptors for known individuals.

1. **Place images in `single_image_folder/` subdirectories**:

   - Create a folder for each person in `single_image_folder/`.
   - Add images of the person in their respective folders.

2. **Run `Generator.py`**:

   ```sh
   python Generator.py
   ```

   This script will read the images, detect faces, and save the face descriptors in the `face_descriptors/` folder.

### 2. Running the Attendance System

1. **Run `main.py`**:

   ```sh
   python main.py
   ```

2. The system will access the webcam and start recognizing faces. Detected faces will be marked as 'Present' in the attendance record.

3. **Save Attendance:**

   - The attendance record will be saved automatically in the `Attendance` directory, structured by year and month. The filename will be the current date in the format `dd-mm-yyyy_attendance.xlsx`.

### 3. Testing Face Descriptors

1. **Run `Test.py`**:

   ```sh
   python Test.py
   ```

2. This script will load and print a face descriptor for a specific person.

## Functions

### `main.py`

- `mark_attendance(name)`: Marks a student as present in the attendance DataFrame.
- `recognize_faces(frame)`: Detects and recognizes faces in a given video frame. Updates the attendance record if a known face is recognized.
- `save_attendance_to_file(attendance_df)`: Saves the attendance DataFrame to an Excel file in a structured directory format.

### `Generator.py`

- `save_face_descriptors(input_folder, output_folder)`: Reads images from the input folder, detects faces, and saves face descriptors in the output folder.
- `main()`: Main function to call `save_face_descriptors`.

### `Test.py`

- Loads and prints a face descriptor from a file.

## Notes

- Ensure the lighting conditions are adequate for the webcam to capture clear images.
- Face recognition accuracy depends on the quality of the face descriptor files and the pre-trained models used.
- Update the `student_list.xlsx` and face descriptor files regularly to maintain accurate attendance records.

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

---
