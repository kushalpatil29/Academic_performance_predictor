#Student_Performance

Project Overview:- This project predicts a student's Sem-7 marks based on their previous semester marks, attendance, study hours, and extracurricular activities. The system uses a machine learning model trained on merged datasets and provides a simple Flask-based API for making predictions.

Approach Data Gathering: Two raw datasets were gathered from Kaggle: 
Dataset 1 -> https://www.kaggle.com/datasets/erqizhou/students-data-analysis 
Dataset 2 -> https://www.kaggle.com/datasets/haseebindata/student-performance-predictions?select=student_performance.csv

Dataset 2 originally contained only 10 entries. Dummy values were added using NumPy to extend it to 105 records.

Feature Selection and Dataset Merging: 
-> Features were selected based on requirements. 
-> The datasets were merged to form a new dataset.

Feature Engineering: 
-> Added an avg_marks column for better feature representation. 
-> Performed encoding on categorical data to convert them into numerical values for preprocessing.

Model Selection: 
Random Forest Regressor was chosen for the following reasons: 
1) Handles Multi-Feature Datasets: 
    ->Works with both continuous (e.g., marks, attendance) and discrete features (e.g., extracurricular activity levels). 
2) Ease of Use: 
    ->Minimal parameter tuning required compared to complex models like XGBoost. 
3) Dataset Compatibility: 
    ->Random Forest works well with medium-sized datasets like the one used in this project. 
4)Model Training and Evaluation: 
    ->The model was trained using the Random Forest Regressor. 
    ->Performance was evaluated using metrics such as: 
        Mean Absolute Error (MAE). 
        Mean Squared Error (MSE). 
        Root Mean Squared Error (RMSE). 
        R-squared (R²). 
The feature importance scores were computed to identify the most influential features for prediction.

----------------------------------------------------- INSTRUCTIONS FOR TESTING API (FLASK) -----------------------------------------------------------------

Run the Flask Application 
-> Open a terminal or command prompt. 
-> Navigate to the directory where your Flask app (app.py) is located. 
-> Run the Flask app (cmd:- python app.py) 
-> The app will start and provide a URL

Open Postman:

Create a New Request:

Click "New Request" in Postman.

Set Request Type: Change the request type to POST. Enter the API URL: Use the URL where your Flask app is running (e.g., http://127.0.0.1:5000/predict).

Add JSON Input to the Body: 
-> Select the Body tab. 
-> Choose the raw option and set the format to JSON (from the dropdown). 
->Enter the required JSON input with the 9 fields Example input data
{ "Sem-1": 75, "Sem-2": 80, "Sem-3": 78, "Sem-4": 85, "Sem-5": 88, "Sem-6": 90, "AttendanceRate": 95, "StudyHoursPerWeek": 15, "ExtracurricularActivities": 3 }

Send the Request: 
-> Click the Send button.

View the Response: 
->The API will return the predicted Sem-7 marks in JSON format. 
->Example: { "Sem-7 Prediction": 89.45 }