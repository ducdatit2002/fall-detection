import streamlit as st
import torch
import cv2
import numpy as np
from PIL import Image
import tempfile
import os

# Load the model from local path
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')

def detect_fall(image):
    results = model(image)
    return results

def main():
    st.title("Fall Detection Application")

    option = st.sidebar.selectbox("Choose input type", ("Upload Image/Video", "Use Camera"))

    if option == "Upload Image/Video":
        uploaded_file = st.file_uploader("Upload Image or Video", type=['jpg', 'jpeg', 'png', 'mp4', 'avi', 'mov'])
        if uploaded_file is not None:
            if uploaded_file.type.startswith('image'):
                file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
                image = cv2.imdecode(file_bytes, 1)
                st.image(image, caption='Uploaded Image.', use_column_width=True)
                results = detect_fall(image)
                st.image(np.squeeze(results.render()), caption='Processed Image.', use_column_width=True)
            elif uploaded_file.type.startswith('video'):
                tfile = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
                tfile.write(uploaded_file.read())
                tfile.close()
                st.write(f'Temporary file path: {tfile.name}')
                vidcap = cv2.VideoCapture(tfile.name)
                stframe = st.empty()
                
                while vidcap.isOpened():
                    success, frame = vidcap.read()
                    if not success:
                        break
                    results = detect_fall(frame)
                    processed_frame = np.squeeze(results.render())
                    stframe.image(processed_frame, channels="BGR")
                vidcap.release()
                os.remove(tfile.name)

    elif option == "Use Camera":
        stframe = st.empty()
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            results = detect_fall(frame)
            processed_frame = np.squeeze(results.render())
            stframe.image(processed_frame, channels="BGR")
        cap.release()

if __name__ == '__main__':
    main()
