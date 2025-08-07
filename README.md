# 🩺 Predictive Pulse: Blood Pressure Classification & PDF Report

**Predictive Pulse** is a Flask-based machine learning web app that predicts an individual's blood pressure stage based on health inputs and generates a clinical-style PDF report. Built for simplicity, accessibility, and accuracy.

---

## 🔍 Overview

This tool helps users understand their BP condition—Normal, Elevated, Hypertension, or Crisis—based on clinical data and symptoms. It provides medical advice and a downloadable PDF summary.

---

## ✅ Features

- 🔬 ML model predicts blood pressure stage
- 📄 PDF report generation with user inputs and results
- 🧠 Uses a trained **Gaussian Naive Bayes model**
- 🎯 Clean and responsive **user interface**
- 📊 Real-time classification with interpretation
- 📂 Built with Flask, ready for local or cloud deployment

---

## 🧠 How It Works

1. User enters medical details via a form
2. Inputs are preprocessed and encoded
3. A trained ML model makes the prediction
4. Result is shown with medical interpretation
5. User can download a PDF report

---

## 🧰 Tech Stack

| Layer      | Tech Used                           |
|------------|-------------------------------------|
| Frontend   | HTML, CSS (Bootstrap), JavaScript   |
| Backend    | Python (Flask)                      |
| ML Model   | scikit-learn (Gaussian Naive Bayes) |
| PDF Engine | reportlab                           |
| Others     | numpy, pandas, gunicorn             |

---

### 🏠 Home Page
<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/c73a5cae-7264-45ae-b327-7d1325392345" />
<img width="1365" height="690" alt="image" src="https://github.com/user-attachments/assets/bf08a235-796c-406c-a1a6-844e402d28cc" />

---

### 📝 Patient Input Form
<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/fdabd575-bf56-413f-8009-352d0174373e" />
<img width="1365" height="688" alt="image" src="https://github.com/user-attachments/assets/2c7c88b4-3033-4b95-b367-68dcf1dbd260" />
<img width="1365" height="692" alt="image" src="https://github.com/user-attachments/assets/5a76c45a-f035-4be4-9f2a-dd85683a34f6" />

---

### 📊 Prediction Result
<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/81ec2e45-c3c5-4597-836b-5865822b52ef" />
<img width="1361" height="692" alt="image" src="https://github.com/user-attachments/assets/f8d70004-b290-4d46-8ac1-67de279b2471" />

---

### 📄 Generated PDF Report
<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/0ececdb8-6eba-4627-b8a6-7e1db21382e3" />

---

## ⚙️ Installation Guide

```bash
# 1. Clone the repository
git clone https://github.com/paarthsarthibeast/Predictive-Pulse.git
cd Predictive-Pulse

# 2. (Optional) Set up a virtual environment
python -m venv venv
# Activate: 
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
