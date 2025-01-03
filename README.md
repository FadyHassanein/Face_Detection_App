# Face Detection and Image Processing App

Welcome to the **Face Detection and Image Processing App**! This project demonstrates the use of Streamlit and OpenCV for detecting features in images such as faces, eyes, and smiles. Additionally, it provides options for real-time detection and creative image transformations like cartoonizing and edge detection.

---

## Features

### 🔍 Image Detection
- **Faces**: Detects human faces in uploaded images.
- **Eyes**: Identifies eyes in uploaded images.
- **Smiles**: Finds smiles in uploaded images.

### 🎨 Image Processing
- **Cartoonize**: Transforms your image into a cartoon-like rendering.
- **Edge Detection (Cannize)**: Applies Canny edge detection for a dramatic effect.

### 📹 Real-Time Detection
- Utilizes your webcam to detect faces in real-time, making the app interactive and engaging.

---

## Tech Stack

### 🛠️ Built With:
- **Python**: The programming language of choice.
- **Streamlit**: For creating the web application.
- **OpenCV**: For powerful computer vision capabilities.
- **Pillow**: For image manipulation and enhancement.

---

## How to Use

### 🚀 Running the App Locally

1. **Clone the Repository**
    ```bash
    git clone https://github.com/FadyHassanein/face-detection-app.git
    cd face-detection-app
    ```

2. **Run the App**
    ```bash
    streamlit run app.py
    ```

3. **Interact with the App**
    Open the URL provided in the terminal (usually `http://localhost:8501`) to explore the app.

### 🌐 Key App Sections
- **Detection**: Upload images and detect features.
- **Real-Time Detection**: Use your webcam to detect faces in real-time.
- **About**: Learn about the app and its features.

---

## File Structure

```plaintext
face-detection-app/
├── app.py               # Main application file
├── frecog/             # Folder containing Haarcascade files
│   ├── haarcascade_frontalface_default.xml
│   ├── haarcascade_eye.xml
│   └── haarcascade_smile.xml
└── README.md           # Documentation (this file)
```

---

## Requirements

Ensure you have the following installed:
- Python 3.7+
- Required Python libraries.

---

## Future Enhancements

- [ ] Add more detection features (e.g., object detection).
- [ ] Improve real-time detection performance.
- [ ] Add more advanced image filters and transformations.

---

## Acknowledgments

- **OpenCV** for the Haar Cascade models.
- **Streamlit** for making interactive app development simple.

---

### Happy Detecting! 😊

