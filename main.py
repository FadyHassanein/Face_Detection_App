import streamlit as st
import cv2 
import numpy as np
from PIL import Image, ImageEnhance
import os

@st.cache_data
def load_image(image_file):
    img = Image.open(image_file)
    return img

def load_cascade(file_name):
    path = os.path.join('frecog', file_name)
    cascade = cv2.CascadeClassifier(path)
    if cascade.empty():
        st.error(f"Failed to load {file_name}")
    return cascade

face_cascade = load_cascade('haarcascade_frontalface_default.xml')
eye_cascade = load_cascade('haarcascade_eye.xml')
smile_cascade = load_cascade('haarcascade_smile.xml')

def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 3)
    return image, faces

def detect_eyes(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(image, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 3)
    return image, eyes

def detect_smiles(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    smiles = smile_cascade.detectMultiScale(gray, 1.8, 20)
    for (x, y, w, h) in smiles:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 3)
    return image, smiles

def cartonize_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(image, 9, 300, 300)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

def cannize_image(image):
    img = cv2.GaussianBlur(image, (11, 11), 0)
    canny = cv2.Canny(img, 100, 150)
    return canny

def process_images(uploaded_files, feature_choice):
    results = []
    for file in uploaded_files:
        image = Image.open(file)
        image_np = np.array(image.convert('RGB'))

        if feature_choice == 'Faces':
            result_img, result_faces = detect_faces(image_np)
            results.append((file.name, result_img, len(result_faces)))
        elif feature_choice == 'Smiles':
            result_img, result_smiles = detect_smiles(image_np)
            results.append((file.name, result_img, len(result_smiles)))
        elif feature_choice == 'Eyes':
            result_img, result_eyes = detect_eyes(image_np)
            results.append((file.name, result_img, len(result_eyes)))
        elif feature_choice == 'Cartonize':
            result_img = cartonize_image(image_np)
            results.append((file.name, result_img, None))
        elif feature_choice == 'Cannize':
            result_img = cannize_image(image_np)
            results.append((file.name, result_img, None))

    return results

def main():
    st.title("Face Detection App")
    st.text("Built with Streamlit and OpenCV")

    activities = ["Detection", "Real-time Detection", "About"]
    choice = st.sidebar.selectbox("Select Activity", activities)

    if choice == 'Detection':
        st.subheader("Face Detection")
        uploaded_files = st.file_uploader("Upload Image(s)", type=['jpg', 'png', 'jpeg'], accept_multiple_files=True)

        if uploaded_files:
            task = ["Faces", "Smiles", "Eyes", "Cartonize", "Cannize"]
            feature_choice = st.sidebar.selectbox("Find Features", task)

            if st.button("Process"):
                results = process_images(uploaded_files, feature_choice)
                for file_name, result_img, count in results:
                    st.text(f"Processed: {file_name}")
                    st.image(result_img, caption=file_name)
                    if count is not None:
                        st.success(f"Found {count} features in {file_name}")

    elif choice == 'Real-time Detection':
        st.subheader("Real-time Face Detection")
        run = st.checkbox("Run")
        FRAME_WINDOW = st.image([])
        camera = cv2.VideoCapture(0)

        while run:
            _, frame = camera.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result_img, _ = detect_faces(frame)
            FRAME_WINDOW.image(result_img)

        camera.release()

    elif choice == 'About':
        st.subheader("About")
        st.markdown("This application is built using Streamlit and OpenCV. It supports face, eye, and smile detection along with real-time detection and image enhancement features. Enjoy exploring your images!")

if __name__ == '__main__':
    main()
