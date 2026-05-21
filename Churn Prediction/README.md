# 🚀 Customer Churn Prediction System

An end-to-end Machine Learning project that predicts whether a telecom customer is likely to churn using customer demographic and service usage data.

Built with Streamlit and Machine Learning for real-time predictions through an interactive web application.

---

# 📌 Overview

Customer churn is one of the biggest challenges for telecom companies.

This project helps businesses identify customers who are likely to leave their services so they can take proactive retention measures.

The application allows users to:

- Enter customer information
- Process and encode customer data
- Predict customer churn instantly
- Display results in a user-friendly interface

---

# 🧠 Problem Statement

Telecom companies lose significant revenue due to customer churn.

The goal of this project is to build a Machine Learning model capable of predicting customer churn based on customer behavior, subscription details, and billing information.

---

# ✨ Features

- 📊 Real-time churn prediction
- 🎯 User-friendly Streamlit interface
- ⚡ Fast and lightweight ML deployment
- 🧾 Manual categorical feature encoding
- 🤖 Pre-trained Machine Learning model
- 📈 Business-focused predictive analytics

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core Programming |
| Streamlit | Web Application |
| NumPy | Numerical Operations |
| Pandas | Data Processing |
| Scikit-learn | Machine Learning |
| Pickle | Model Serialization |

---

# 📂 Project Structure

```bash
Customer-Churn-Prediction/
│
├── app.py
├── churn_model.pkl
├── Churn-prediction.ipynb
├── WA_Fn-UseC_-Telco-Customer-Churn.csv
└── README.md
```

---

# 📊 Dataset Information

The dataset contains telecom customer information such as:

- Customer demographics
- Account information
- Service subscriptions
- Billing details
- Contract information

### Important Features Used

| Feature | Description |
|---|---|
| gender | Customer gender |
| SeniorCitizen | Senior citizen status |
| tenure | Number of months with company |
| InternetService | Type of internet service |
| Contract | Contract type |
| MonthlyCharges | Monthly bill amount |
| TotalCharges | Total amount charged |
| PaymentMethod | Payment method |

---

# ⚙️ Machine Learning Workflow

## 1️⃣ Data Collection
Customer churn dataset collected from telecom records.

## 2️⃣ Data Preprocessing
- Handling missing values
- Feature selection
- Data cleaning

## 3️⃣ Feature Encoding
Categorical features converted into numerical values manually inside the application.

## 4️⃣ Model Training
Machine Learning classification model trained on processed customer data.

## 5️⃣ Model Serialization
Trained model saved using Pickle.

## 6️⃣ Deployment
Integrated into a Streamlit web application for real-time predictions.

---

# 🖥️ Application Interface

The application collects customer information through interactive UI components like:

- Dropdown menus
- Sliders
- Numeric input fields

Example:

```python
gender = st.selectbox("Gender", ["Female", "Male"])

tenure = st.slider("Tenure", 0, 72)

MonthlyCharges = st.number_input("Monthly Charges")
```

---

# 🔍 Prediction Logic

After collecting user input:

1. Data is manually encoded
2. Converted into NumPy array
3. Passed into trained model
4. Prediction result displayed

Example:

```python
prediction = model.predict(input_data)

if prediction[0] == 1:
    st.error("Customer Will Churn")
else:
    st.success("Customer Will Not Churn")
```

---

# 🚀 Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/customer-churn-prediction.git
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd customer-churn-prediction
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install streamlit numpy pandas scikit-learn
```

---

## 4️⃣ Run the Application

```bash
streamlit run app.py
```

---

# 📈 Sample Output

| Prediction Result |
|---|
| ✅ Customer Will Not Churn |
| ❌ Customer Will Churn |

---

# 🎯 Business Use Cases

This project can help telecom companies:

- Improve customer retention
- Reduce revenue loss
- Identify high-risk customers
- Build targeted marketing campaigns
- Enhance customer satisfaction

---

# 🔮 Future Enhancements

- Add prediction probability score
- Improve UI/UX design
- Deploy on Streamlit Cloud
- Add login authentication
- Integrate database support
- Use Deep Learning models
- Add data visualization dashboard
---
---
# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

## Ujjwal Kumar

Passionate about:
- Data Science
- Machine Learning
- AI Applications
- Predictive Analytics

---

# ⭐ Support

If you found this project useful:

- Star the repository
- Fork the project
- Share with others

---

# 💡 Final Note

This project demonstrates how Machine Learning can be integrated with a modern web framework to solve real-world business problems effectively.
