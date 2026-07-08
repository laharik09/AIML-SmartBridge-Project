# 💳 Credit Card Approval Prediction using Machine Learning

## 📌 Project Overview

The **Credit Card Approval Prediction** project is a Machine Learning-based web application that predicts whether a credit card application is likely to be **Approved** or **Rejected** based on an applicant's financial and demographic information.

The system automates the credit card approval process, reducing manual effort and enabling faster decision-making for banks and financial institutions. It combines machine learning techniques with a Flask web application to provide real-time predictions through an interactive user interface.

---

## 🚀 Features

- Predicts credit card approval instantly
- User-friendly Flask web application
- Responsive and modern banking-inspired interface
- Multiple Machine Learning models implemented
- Automatic selection of the best-performing model
- Real-time prediction using Flask
- Trained model saved using Joblib
- Professional HTML and CSS frontend

---

## 🛠 Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Joblib

### Data Analysis
- Pandas
- NumPy

### Visualization
- Matplotlib
- Seaborn

### Web Development
- Flask
- HTML5
- CSS3

---

## 📂 Dataset

The project uses two CSV files:

- `application_record.csv`
- `credit_record.csv`

These datasets contain applicant demographic information and historical credit payment records that are merged and processed before training the machine learning models.

---

## 📊 Machine Learning Workflow

### 1️⃣ Data Collection

- Load applicant dataset
- Load credit history dataset

---

### 2️⃣ Exploratory Data Analysis (EDA)

Performed:

- Dataset inspection
- Shape analysis
- Missing value analysis
- Feature exploration

---

### 3️⃣ Univariate Analysis

- Occupation distribution
- Count plots
- Category frequency analysis

---

### 4️⃣ Multivariate Analysis

- Correlation Heatmap
- Feature relationships

---

### 5️⃣ Descriptive Analysis

Generated statistical summaries using:

- Mean
- Standard deviation
- Minimum
- Maximum
- Percentiles

---

### 6️⃣ Data Preprocessing

Performed:

- Duplicate removal
- Missing value handling
- Dataset merging
- Feature engineering
- Label Encoding

---

### 7️⃣ Machine Learning Models

The following models were trained and evaluated:

- Logistic Regression
- Random Forest Classifier
- Decision Tree Classifier
- Gradient Boosting Classifier

---

### 8️⃣ Model Evaluation

Models were compared using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

The best-performing model was saved as:

```text
credit_card_model.pkl
```

---

# 🌐 Flask Web Application

The trained model is integrated into a Flask application that allows users to enter applicant details and receive an instant approval prediction.

---

## 🏠 Home Page

- Project Overview
- Navigation Menu
- Start Prediction Button

---

## 📄 Prediction Page

Users enter the following information:

- Gender
- Own Car
- Own House
- Number of Children
- Annual Income
- Income Type
- Education
- Family Status
- Housing Type
- Days Since Birth
- Days Employed
- Mobile Availability
- Work Phone
- Phone
- Email
- Family Members

---

## ✅ Result Page

Displays the prediction result as:

- ✅ Credit Card Approved
- ❌ Credit Card Rejected

---

# 📁 Project Structure

```
Credit-Card-Approval-Prediction/
│
├── app.py
├── credit_card_model.pkl
├── gender_encoder.pkl
├── car_encoder.pkl
├── realty_encoder.pkl
├── income_encoder.pkl
├── education_encoder.pkl
├── family_encoder.pkl
├── housing_encoder.pkl
├── requirements.txt
├── README.md
│
├── static/
│   └── style.css
│
└── templates/
    ├── home.html
    ├── index.html
    └── result.html
```

---

# ⚙ Installation

## Clone the Repository

```bash
git clone https://github.com/laharik09/Credit-Card-Approval-Prediction.git
```

---

## Navigate to the Project Folder

```bash
cd Credit-Card-Approval-Prediction
```

---

## Create a Virtual Environment

```bash
python -m venv venv
```

---

## Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Required Packages

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Application

Run the Flask application:

```bash
python app.py
```

The application will start on:

```
http://127.0.0.1:5000
```

Open this URL in your browser to use the Credit Card Approval Prediction system.

---

# 📈 Model Inputs

The trained model uses the following input features:

- CODE_GENDER
- FLAG_OWN_CAR
- FLAG_OWN_REALTY
- CNT_CHILDREN
- AMT_INCOME_TOTAL
- NAME_INCOME_TYPE
- NAME_EDUCATION_TYPE
- NAME_FAMILY_STATUS
- NAME_HOUSING_TYPE
- DAYS_BIRTH
- DAYS_EMPLOYED
- FLAG_MOBIL
- FLAG_WORK_PHONE
- FLAG_PHONE
- FLAG_EMAIL
- CNT_FAM_MEMBERS
