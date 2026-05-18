Customer Churn Prediction

A Machine Learning web application built with Streamlit to predict whether a telecom customer is likely to churn based on customer details and service usage.

📌 Project Overview

This project uses a trained Machine Learning model to predict customer churn for a telecom company. Users can enter customer information through a simple web interface, and the model predicts whether the customer is likely to leave the service.

The application is developed using:

Python
Streamlit
NumPy
Pickle
Machine Learning Classification Model

The app loads a pre-trained model (churn_model.pkl) and takes customer details as input to generate predictions.

🚀 Features
Interactive web interface using Streamlit
Real-time churn prediction
Customer data input form
Manual categorical data encoding
Fast and lightweight deployment
📂 Project Structure
Customer-Churn-Prediction/
│
├── app.py
├── churn_model.pkl
├── Churn-prediction.ipynb
├── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── README.md
🛠️ Technologies Used
Python 3.x
Streamlit
NumPy
Scikit-learn
Pandas
Pickle
📊 Input Features

The model uses the following customer attributes:

Gender
Senior Citizen
Partner
Dependents
Tenure
Phone Service
Multiple Lines
Internet Service
Online Security
Online Backup
Device Protection
Tech Support
Streaming TV
Streaming Movies
Contract Type
Paperless Billing
Payment Method
Monthly Charges
Total Charges
▶️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/your-username/customer-churn-prediction.git
cd customer-churn-prediction
2️⃣ Install Dependencies
pip install -r requirements.txt

If requirements.txt is not available, install manually:

pip install streamlit numpy scikit-learn pandas
3️⃣ Run the Streamlit App
streamlit run app.py
📌 Prediction Output

The application predicts:

Customer Will Churn
Customer Will Not Churn

based on the entered customer information.

🧠 Machine Learning Workflow
Data Collection
Data Preprocessing
Feature Encoding
Model Training
Model Serialization using Pickle
Deployment with Streamlit
📷 Application Preview
st.title("Customer Churn Prediction")

The app provides an easy-to-use interface for entering customer information and viewing predictions instantly.

🔮 Future Improvements
Add probability score for churn prediction
Improve UI design
Deploy on Streamlit Cloud
Add model performance metrics
Use advanced ML models
🤝 Contributing

Contributions are welcome!

Feel free to fork the repository and submit pull requests.

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Ujjwal Kumar
