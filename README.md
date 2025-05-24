# Facial Expression Recognition System - Sure Trust 😊

![Facial Expression Recognition](https://img.shields.io/badge/Facial%20Expression%20Recognition-Open%20Source-brightgreen)

Welcome to the **Facial Expression Recognition System** repository! This project harnesses the power of YOLOv9 and Flask to detect emotions in images and live camera feeds. It identifies five emotions: Angry, Happy, Natural, Sad, and Surprised, achieving a mean Average Precision (mAP50) of 0.731. The system features a user-friendly web interface that supports file uploads, real-time processing, and emoji feedback.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Demo](#demo)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Releases](#releases)

## Project Overview

Facial expressions are a vital part of human communication. This project aims to develop a system that can recognize and interpret these expressions. Using deep learning techniques, we built a model that can classify emotions from facial images. This technology has applications in Human-Computer Interaction (HCI), emotion analysis, and more.

## Features

- **Emotion Detection**: Accurately detects five emotions from images and live video feeds.
- **Web Interface**: Easy-to-use interface for uploading images and viewing results.
- **Real-Time Processing**: Analyze live camera input for immediate feedback.
- **Emoji Feedback**: Provides emoji suggestions based on detected emotions.
- **Open Source**: Contribute to the project and improve the system.

## Technologies Used

This project utilizes the following technologies:

- **Python**: The primary programming language for the application.
- **OpenCV**: For image processing and computer vision tasks.
- **Flask**: A lightweight web framework for creating the web interface.
- **HTML/CSS/JS**: For building the front end of the application.
- **YOLOv9**: A state-of-the-art object detection model used for emotion recognition.
- **TensorFlow**: For deep learning tasks and model training.
- **Roboflow Dataset**: A dataset used for training the emotion detection model.

## Installation

To get started with this project, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Bananacat123-hue/Facial_Expression_Recognition-Sure_Trust-.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd Facial_Expression_Recognition-Sure_Trust-
   ```

3. **Install Required Packages**:

   Make sure you have Python installed. Then, install the required packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:

   Start the Flask server:

   ```bash
   python app.py
   ```

5. **Access the Web Interface**:

   Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## Usage

Once the application is running, you can use it in the following ways:

1. **Upload an Image**: Click on the upload button to select an image file from your device. The system will analyze the image and display the detected emotion.

2. **Use the Live Camera**: Allow the application to access your camera. It will process the video feed in real-time and show the detected emotions as you move.

3. **View Emoji Feedback**: Based on the detected emotion, the application will display an appropriate emoji for quick feedback.

## Demo

Here’s a brief demonstration of how the application works:

![Demo](https://img.shields.io/badge/Demo-Click%20Here-brightblue)

You can find the latest releases and updates [here](https://github.com/Bananacat123-hue/Facial_Expression_Recognition-Sure_Trust-/releases).

## Contributing

We welcome contributions to improve this project. Here’s how you can help:

1. **Fork the Repository**: Click on the fork button to create a copy of the repository in your account.

2. **Create a New Branch**: Use a descriptive name for your branch.

   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **Make Your Changes**: Implement your feature or fix a bug.

4. **Commit Your Changes**: Write a clear commit message.

   ```bash
   git commit -m "Add your message here"
   ```

5. **Push to Your Branch**:

   ```bash
   git push origin feature/YourFeatureName
   ```

6. **Create a Pull Request**: Go to the original repository and submit a pull request.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute this software.

## Contact

For questions or feedback, you can reach out to the project maintainer:

- **Email**: your-email@example.com
- **GitHub**: [Bananacat123-hue](https://github.com/Bananacat123-hue)

## Releases

For the latest updates and downloadable files, visit the [Releases section](https://github.com/Bananacat123-hue/Facial_Expression_Recognition-Sure_Trust-/releases). 

Thank you for your interest in the Facial Expression Recognition System! We hope you find it useful for your projects and research. Your contributions and feedback are always welcome.