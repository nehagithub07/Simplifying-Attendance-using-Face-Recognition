# Simplifying Attendance using Face Recognition

## Overview

This project utilizes face recognition technology to automate attendance tracking. The system captures images from a webcam, recognizes faces, and records attendance in a formatted table. An email is sent with the attendance report.

## Features

- Real-time face detection and recognition using a webcam.
- Automatic attendance marking based on recognized faces.
- Email report with the attendance list in HTML format.
- Simple and user-friendly interface.

## Dependencies

- `opencv-python` for image processing and webcam access.
- `face_recognition` for face detection and recognition.
- `numpy` for numerical operations.
- `prettytable` for formatting the attendance table.
- `smtplib` and `ssl` for sending emails.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/nehagithub07/Simplifying-Attendance-using-Face-Recognition.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Simplifying-Attendance-using-Face-Recognition
    ```

3. Install the required Python packages:

    ```bash
    pip install opencv-python face_recognition numpy prettytable
    ```

## Configuration

1. Ensure you have a directory named `Data/Images` containing the images of individuals to be recognized.
2. Update the `sendmail.py` file with your email credentials:

    ```python
    sender_email = "your_email@gmail.com"
    receiver_email = "receiver_email@gmail.com"
    password = "your_password"
    ```

## Usage

1. Run the main script:

    ```bash
    python main.py
    ```

2. The webcam window will open, and the system will start recognizing faces and marking attendance.
3. Press 'q' to stop the webcam feed and send the attendance report via email.

## Project Structure

- `main.py`: The main script that performs face recognition and attendance marking.
- `sendmail.py`: The module responsible for sending the attendance report via email.
- `Data/Images/`: Directory containing images of individuals for recognition.
- `__pycache__/`: Python cache files.
- `dlib-19.24.1-cp311-cp311-win_amd64.whl`: Dlib wheel file for face recognition.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements. 

## Contact

For any queries, you can contact:

- **Author**: Neha
- **Email**: [nehasaniya465@gmail.com](mailto:nehasaniya465@gmail.com)
