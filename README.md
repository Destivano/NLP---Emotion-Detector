# NLP Emotion Detector

## 📌 Project Overview
This is an **NLP-based Emotion Detector** that analyzes textual input to determine the dominant emotion expressed. The project was developed as part of the **Python for AI & Development** course on **edX**, taught by **IBM**.

## 🛠️ Technologies Used
- **Python**
- **Flask** (for the web application)
- **Natural Language Processing (NLP)**

## 🚀 How It Works
1. The user inputs a text statement.
2. The **emotion detection model** processes the text and identifies the **dominant emotion**.
3. The system returns a response showing the detected emotions along with their intensity scores.

## 📂 Project Structure
```
final_project/
│── EmotionDetection/               # Emotion detection logic
│   ├── __init__.py
│   ├── emotion_detection.py        # Emotion detection implementation
│
│── templates/
│   ├── index.html                  # Web interface for user input
│
│── static/                          # Static assets (CSS, JS, etc.)
│
│── server.py                        # Flask app to serve the API & UI
│── test_emotion_detection.py        # Test cases for emotion detection
│── README.md                        # Project documentation
│── LICENSE                          # License file
│── .gitignore                       # Files to ignore in Git
```

## 🔧 Installation & Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/Destivano/NLP---Emotion-Detector.git
   cd NLP--Emotion-Detector
   ```
2. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Flask App**
   ```bash
   python server.py
   ```
5. Open your browser and go to **`http://127.0.0.1:5000/`**

## 📌 API Endpoint
- **`GET /emotionDetector?textToAnalyze=your_text_here`**
  - Returns JSON with emotion scores and the dominant emotion.

## 📝 Example Usage
**Request:**
```
http://127.0.0.1:5000/emotionDetector?textToAnalyze=I am feeling very happy today!
```

**Response:**
```json
{
    "anger": 0.1,
    "joy": 0.9,
    "sadness": 0.05,
    "dominant_emotion": "joy"
}
```

## 🏆 Conclusion

By completing this project, I have:
- Created an Emotion Detection application using functions from embeddable AI libraries.
- Extracted relevant information from the output received from the function.
- Tested and packaged the application created using the Emotion Detection function.
- Completed web deployment of my application using Flask.
- Incorporated error handling in my application to account for invalid input.
- Written code in perfect compliance with **PEP8 guidelines**, achieving a **10/10 score** in static code analysis.

## 🏆 Credits
- Developed by **Mohamed Amine Arous**
- As part of **IBM’s Python for AI & Development** course on **edX**


## 📜 License
This project is open-source under the **MIT License**.

© IBM Corporation 2023. All rights reserved.

