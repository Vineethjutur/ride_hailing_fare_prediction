# 🚖 Dynamic Fare Prediction in Ride-Hailing Apps

## 📌 Overview
This project predicts **ride fares in real-time** for a ride-hailing service using **machine learning**.  
The goal is to identify the **key drivers of fare variation** (time, location, weather) and build a **Streamlit dashboard** for real-time prediction.

This work was completed as part of a **Data Science graduate project at UMBC** (Spring 2025).

---

## 🛠️ Tech Stack
- **Languages & Libraries:** Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn  
- **Machine Learning Models:** Linear Regression, Decision Trees, Random Forest, Gradient Boosting  
- **Visualization & App:** Streamlit Dashboard  
- **Other Tools:** Jupyter Notebook, GitHub

---

## 📊 Dataset
- Data consisted of **ride-hailing trip records** enriched with:
  - Pickup & drop-off time  
  - Pickup & drop-off locations  
  - Weather data (temperature, rain, etc.)  
- Processed into **cleaned training/testing sets** (due to data size, only a sample is shared).

---

## 🔎 Methodology
1. **Exploratory Data Analysis (EDA):**
   - Identified fare distribution, seasonal/time trends, and geographic patterns.
   - Detected strong correlation between **time of day**, **location clusters**, and **weather conditions** with fare.

2. **Feature Engineering:**
   - Extracted **hour of day, day of week, holidays** from timestamps.  
   - Clustered pickup/dropoff locations using **k-means**.  
   - Added weather-based indicators.

3. **Model Development:**
   - Compared multiple ML models (Linear Regression, Decision Trees, Random Forest, Gradient Boosting).  
   - Selected the **best performing model** based on accuracy and RMSE.  

4. **Dashboard:**
   - Built a **Streamlit app** where users can input ride details (time, location, weather) to get a **predicted fare**.

---

## 📈 Results
- **Random Forest model** achieved the most reliable performance:
  - RMSE: **$2.85**  
  - R² Score: **0.87**  
- Identified **peak hours and rainy conditions** as major drivers of high fares.  
- **Streamlit Dashboard** provides real-time fare predictions and interactive insights.  

Example outputs:  
- Feature importance plot (`results/feature_importance.png`)  
- Model comparison chart (`results/model_comparison.png`)  
- Dashboard screenshot (`results/dashboard_screenshot.png`)  

---

## 🚀 How to Run

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/ride_hailing_fare_prediction.git
cd ride_hailing_fare_prediction
