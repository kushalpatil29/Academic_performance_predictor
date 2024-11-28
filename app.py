from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

model_path = "student_performance.pkl"
try:
    model = joblib.load(model_path)
    print("Model loaded successfully.")
except FileNotFoundError:
    print(f"Error: Model file not found at {model_path}. Ensure the file exists.")
    exit()

input_columns = ['Sem-1', 'Sem-2', 'Sem-3', 'Sem-4', 'Sem-5', 'Sem-6', 
                 'AttendanceRate', 'StudyHoursPerWeek', 'ExtracurricularActivities']

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        missing_columns = [col for col in input_columns if col not in data]
        if missing_columns:
            return jsonify({
                "error": f"Missing required fields: {missing_columns}"
            }), 400

        input_data = pd.DataFrame([{
            "Sem-1": data["Sem-1"],
            "Sem-2": data["Sem-2"],
            "Sem-3": data["Sem-3"],
            "Sem-4": data["Sem-4"],
            "Sem-5": data["Sem-5"],
            "Sem-6": data["Sem-6"],
            "AttendanceRate": data["AttendanceRate"],
            "StudyHoursPerWeek": data["StudyHoursPerWeek"],
            "ExtracurricularActivities": data["ExtracurricularActivities"]
        }])

        prediction = model.predict(input_data)
        return jsonify({
            "Sem-7 Prediction": round(prediction[0], 2)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
