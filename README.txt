
Project Title: Dynamic Fare Prediction in Ride-Hailing Apps
------------------------------------------------------------

This project deploys a machine learning model using Streamlit to predict ride-hailing fare prices based on trip distance, start hour, and day of the week. The model used is Histogram-Based Gradient Boosting (HGB), trained and saved as a .pkl file.

Authors: Gagan Venkatesh, Vineeth Jutur

------------------------------------------------------------
HOW TO RUN THE STREAMLIT APP
------------------------------------------------------------

Step 1: Clone or download the project folder containing:
- app.py (Streamlit app script)
- fare_prediction_model.pkl (trained ML model)

Step 2: Install Python dependencies

Make sure you have Python 3.8 or higher installed.

### For Windows (Command Prompt or Anaconda Prompt):
pip install streamlit scikit-learn pandas numpy

### For Mac (Terminal):
pip3 install streamlit scikit-learn pandas numpy

Step 3: Run the Streamlit app

### Windows:
streamlit run app.py

### Mac:
streamlit run app.py

Your default browser will open with the app at:
http://localhost:8501

------------------------------------------------------------
DATASET LINKS (hosted on Google Drive)
------------------------------------------------------------

Please download the following datasets before running model training or reloading data:

1. Original Dataset (Full Uber rides data):
https://drive.google.com/file/d/1ZmHOG_1K8cM3R0Y6YZ9Js8r7JUntIo1W/view

2. X_data (Feature matrix used for training/testing):
https://drive.google.com/file/d/1uJVWCnmpKhi45vsop0Zi4G33DnU6gMh3/view

3. Y_data (Target variable – Fare values):
https://drive.google.com/file/d/1383bxL9Q1ANPPUfgOGPGJTXAPTU-mkIi/view

------------------------------------------------------------
NOTES
------------------------------------------------------------

- The current app takes inputs for trip miles, start hour, and day of week, and uses the pre-trained model to predict fare.
- You can extend the app by integrating weather or traffic data for better accuracy.
- If you run into port conflicts, change the port by:
streamlit run app.py --server.port 8502

- **Demo screen recording of the deployed app usage is attached for reference.**


