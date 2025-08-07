# 🚑 Predictive Pulse – Hypertension Prediction App

Predictive Pulse is a web-based application that uses machine learning to predict a patient's hypertension stage based on medical input. It generates a downloadable PDF report styled like a clinical summary.

![App Banner](screenshots/banner.png)

---

## 🩺 Features

- 🧠 Predicts hypertension stage using a Gaussian Naive Bayes classifier.
- 📄 Generates a clean, clinical-style **PDF report**.
- 🖥️ Interactive web interface to input patient details.
- 🔍 Displays prediction results and advice.
- 🌐 Built using Flask + HTML/CSS.

---

## 📷 Screenshots

### Home Page
![Home Page](screenshots/home.png)

### Enter Patient Details
![Form](screenshots/form.png)

### Prediction Result
![Result Page](screenshots/result.png)

### Downloadable PDF Report
![PDF](screenshots/pdf_report.png)

---

## 🧪 How It Works

1. User fills out a form with medical info.
2. App encodes inputs based on pre-trained LabelEncoders.
3. A trained Gaussian Naive Bayes model predicts the hypertension stage.
4. Results are displayed and included in a downloadable PDF report.

---

## 📁 Project Structure

