# Fall Detection Project

## Project Overview
This project aims to develop a fall detection system using YOLOv5 for real-time monitoring. The system can detect if a person falls and trigger an alert, providing crucial support for elderly care and personal safety.

## Contributors
- **Phạm Đức Đạt**
- **Lê Thiên Doanh**
- **Dương Thị Quỳnh Như**
- **Nguyễn Khánh Hà**
- **Nguyễn Hoàng Luân**

## Deployment
The project is deployed on Hugging Face Spaces and can be accessed via the following link:  
[Fall Detection on Hugging Face](https://huggingface.co/spaces/ducdatit2002/fall-detection)

## Installation and Setup

1. **Clone the Repository**  
   Clone the project repository to your local machine:
   ```bash
   git clone https://github.com/your-repo/fall-detection.git
   cd fall-detection
   ```

2. **Install Dependencies**  
   Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**  
   Start the Streamlit app to begin detecting falls in real-time:
   ```bash
   streamlit run app.py
   ```

## Model and Methodology
The fall detection system uses the YOLOv5 model, a state-of-the-art object detection algorithm, to identify and classify fall events. The model is trained to recognize various postures and motions, ensuring accurate detection in different scenarios.

## How to Use

1. **Upload a Video or Stream**  
   Upload a video or start a live stream to begin detecting falls. The application will process the input and display the detection results in real-time.

2. **View Detection Results**  
   The system will display bounding boxes around detected individuals and label any fall events detected in the video feed.

3. **Trigger Alerts**  
   If a fall is detected, the system will automatically trigger an alert, notifying the necessary parties for immediate response.

## Future Development
- **Enhance Model Accuracy**: Further improve the model by training with a more extensive dataset.
- **Integration with IoT Devices**: Integrate with smart devices for automatic alerts and emergency response.

## License
This project is licensed under the MIT License.

## Contact
For any questions or suggestions, please reach out to the contributors via email or through the repository's issue tracker.

We hope this project contributes to a safer environment and provides valuable support for those in need. Thank you for using our Fall Detection system!
