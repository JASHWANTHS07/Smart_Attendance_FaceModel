# Smart Face Attendance Using Face Model

## Project Overview

The Smart Face Attendance system leverages computer vision and facial recognition technology to automatically mark the attendance of students. It captures video frames from a webcam, detects faces, recognizes known faces, and updates an attendance record accordingly. The attendance record is saved in an organized manner, creating folders based on the year and month, and saving the attendance file with the current date.

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
├── student_list.xlsx
├── attendance_system.py
└── README.md
```

- `Dat_files/` contains the pre-trained models.
- `face_descriptors/` contains numpy files for face descriptors of known persons.
- `student_list.xlsx` is an Excel file containing the list of students.

## Setup and Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/smart-face-attendance.git
   cd smart-face-attendance
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

1. **Run the attendance system:**

   ```sh
   python attendance_system.py
   ```

2. The system will access the webcam and start recognizing faces. Detected faces will be marked as 'Present' in the attendance record.

3. **Save Attendance:**

   - The attendance record will be saved automatically in the `Attendance` directory, structured by year and month. The filename will be the current date in the format `dd-mm-yyyy_attendance.xlsx`.

## Functions

### `mark_attendance(name)`

Marks a student as present in the attendance DataFrame.

### `recognize_faces(frame)`

Detects and recognizes faces in a given video frame. Updates the attendance record if a known face is recognized.

### `save_attendance_to_file(attendance_df)`

Saves the attendance DataFrame to an Excel file in a structured directory format.

## Notes

- Ensure the lighting conditions are adequate for the webcam to capture clear images.
- Face recognition accuracy depends on the quality of the face descriptor files and the pre-trained models used.
- Update the `student_list.xlsx` and face descriptor files regularly to maintain accurate attendance records.

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

---

This README file provides a comprehensive guide to setting up and running the Smart Face Attendance system. If you have any questions or encounter issues, please refer to the project's GitHub repository or open an issue for support.