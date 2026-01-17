# 🏠 Bangalore House Price Prediction

A Machine Learning web application that predicts house prices in Bangalore based on location and property features.  
The model is deployed using **Streamlit Cloud** for real-time predictions.

---

## 🚀 Live Demo
👉 **Streamlit App:**  
https://bangalorehousepriceprediction-prasadshetty.streamlit.app/

---

## 📌 Project Overview
This project uses a trained regression model to estimate house prices in Bangalore.  
Users can input property details such as:

- Location  
- Total square feet  
- Number of bathrooms  
- Number of balconies  
- BHK configuration  

The application then predicts the **estimated price in Lakhs (₹)**.

---

## 🛠️ Tech Stack
- Python  
- NumPy  
- Pandas  
- Scikit-learn  
- Streamlit  

---

## 📂 Project Structure
```
Bangalore-House-Price-Prediction/
│
├── app.py
├── requirements.txt
├── banglore_home_prices_model.pickle
├── columns.json
├── README.md
│
├── dataset/
│   └── BHP.csv
│
└── notebook/
    └── House_Pricing_Predictions.ipynb
```

---

## 📊 Dataset
**Bangalore Housing Prices Dataset**  
Source: Kaggle  
🔗 https://www.kaggle.com/datasets/aryanfelix/bangalore-housing-prices

---

## ▶️ How to Run Locally

1️⃣ Clone the repository
```bash
git clone https://github.com/shettyprasad-git/Bangalore-House-Price-Prediction.git
```

2️⃣ Navigate to the project folder
```bash
cd Bangalore-House-Price-Prediction
```

3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

4️⃣ Run the Streamlit app
```bash
streamlit run app.py
```

---

## 📈 Output
The app displays the **estimated house price (₹ in Lakhs)** based on user inputs and trained ML model predictions.

---

## 💡 Key Learnings
- Data preprocessing and feature engineering
- Model training and serialization using Pickle
- Deploying ML models using Streamlit Cloud
- Building an end-to-end ML application

---

## 👤 Author
**Durga Prasad**  
🔗 GitHub: https://github.com/shettyprasad-git  
🔗 LinkedIn: https://www.linkedin.com/in/durgaprasadshetty

---

⭐ If you found this project useful, feel free to star the repository!
