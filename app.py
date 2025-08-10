from flask import Flask, render_template, request, send_file
import pickle
import numpy as np
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

# Load model and encoders
model = pickle.load(open("models/random_forest_model.pkl", "rb")) # For Best Accuracy.

app = Flask(__name__)

label_to_encoded = {
    'C': {'Female': 1, 'Male': 0},
    'Age': {'18-34': 0, '35-50': 1, '51-64': 2, '65+': 3},
    'History': {'No': 1, 'Yes': 0},
    'Patient': {'No': 0, 'Yes': 1},
    'TakeMedication': {'No': 0, 'Yes': 1},
    'Severity': {'Mild': 0, 'Moderate': 2, 'Severe': 1},
    'BreathShortness': {'No': 0, 'Yes': 1},
    'VisualChanges': {'No': 0, 'Yes': 1},
    'NoseBleeding': {'No': 0, 'Yes': 1},
    'Whendiagnoused': {'<1 Year': 0, '1 - 5 Years': 1, '>5 Years': 2},
    'Systolic': {'100+': 1, '111 - 120': 2, '121 - 130': 3, '130+': 0},
    'Diastolic': {'70 - 80': 0, '81 - 90': 1, '91 - 100': 2, '100+': 3, '130+': 4},
    'ControlledDiet': {'No': 0, 'Yes': 1},
}


stage_map = {
    0: 'Normal',
    1: 'Elevated',
    2: 'Stage 1',
    3: 'Stage 2',
    4: 'Hypertensive Crisis',
    5: 'Hypotension'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/details')
def details():
    return render_template('details.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        name = request.form.get('name', '')  # for PDF only

        model_features = list(label_to_encoded.keys())
        raw_inputs = {}
        for feature in model_features:
            value = request.form.get(feature)
            if value is None:
                return render_template(
                    'prediction.html',
                    prediction_text=f"Missing input for {feature}."
                )
            raw_inputs[feature] = value

        # Encode features using label_to_encoded mapping
        try:
            encoded_features = [
                label_to_encoded[feature][raw_inputs[feature]] for feature in model_features
            ]
        except KeyError as e:
            return render_template(
                'prediction.html',
                prediction_text=f"Invalid value for {e.args[0]}. Please check your input."
            )

        final_features = np.array([encoded_features])
        print(final_features)
        prediction = model.predict(final_features)
        print(prediction)

       
        output = stage_map.get(prediction[0], f"Unknown Stage ({prediction[0]})")

        return render_template(
            'prediction.html',
            name=name,
            systolic=raw_inputs['Systolic'],
            diastolic=raw_inputs['Diastolic'],
            result=output
        )

    except Exception as e:
        return render_template(
            'prediction.html',
            prediction_text=f"Prediction error: {str(e)}"
        )

@app.route('/download-report', methods=['POST'])
def download_report():
    name = request.form.get('name', '')
    systolic = request.form.get('systolic', '')
    diastolic = request.form.get('diastolic', '')
    result = request.form.get('result', '')

    # Define stage-specific medical advice
    advice_map = {
        "Normal": "Maintain a healthy lifestyle. Keep monitoring your BP regularly.",
        "Elevated": "Reduce salt intake and exercise regularly. Monitor your BP closely.",
        "Stage 1": "Consult your doctor. Lifestyle changes and medication might be required.",
        "Stage 2": "Seek medical attention. Medication and lifestyle changes are necessary.",
        "Hypertensive Crisis": "Immediate medical attention is required. Go to the emergency room.",
        "Hypotension": "Increase fluid intake and consult a healthcare provider."
    }

    # Get advice based on result
    advice = advice_map.get(result, "Monitor your BP regularly and reduce salt intake.")

    timestamp = datetime.now().strftime("%d/%m/%Y, %I:%M:%S %p")

    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2, height - 80, "Predictive Pulse – BP Report")

    # Horizontal line under title
    c.setLineWidth(1)
    c.line(50, height - 90, width - 50, height - 90)

    # Patient Info Section
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 130, "Patient Information")
    c.setFont("Helvetica", 12)
    c.drawString(70, height - 150, f"Name: {name}")
    c.drawString(70, height - 170, f"Date: {timestamp}")

    # Horizontal line
    c.line(50, height - 185, width - 50, height - 185)

    # BP Readings Section
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 210, "Blood Pressure Readings")

    # Color-coded BP values
    from reportlab.lib import colors
    try:
        systolic_val = int(systolic)
        diastolic_val = int(diastolic)
    except ValueError:
        systolic_val = diastolic_val = 0  # fallback if not integers

    if systolic_val > 180 or diastolic_val > 110:
        bp_color = colors.red
    elif systolic_val >= 140 or diastolic_val >= 90:
        bp_color = colors.orange
    elif systolic_val >= 120 or diastolic_val >= 80:
        bp_color = colors.darkgoldenrod
    else:
        bp_color = colors.green

    c.setFont("Helvetica", 12)
    c.setFillColor(bp_color)
    c.drawString(70, height - 230, f"Systolic BP: {systolic} mmHg")
    c.drawString(70, height - 250, f"Diastolic BP: {diastolic} mmHg")
    c.setFillColor(colors.black)

    # Prediction Section
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 280, "Predicted Hypertension Stage")
    c.setFont("Helvetica", 12)
    c.drawString(70, height - 300, f"Result: {result}")

    # Advice Section
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 330, "Medical Advice")
    c.setFont("Helvetica", 12)
    c.drawString(70, height - 350, advice)

    # Footer Disclaimer
    c.setFont("Helvetica-Oblique", 9)
    c.setFillColor(colors.grey)
    c.drawCentredString(width / 2, 40, "This report is auto-generated and not a substitute for professional medical advice.")
    c.setFillColor(colors.black)

    c.showPage()
    c.save()
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="bp_report.pdf",
        mimetype='application/pdf'
    )


if __name__ == '__main__':
    app.run(debug=True)