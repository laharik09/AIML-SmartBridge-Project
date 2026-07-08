import os
from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Dynamic path helper to prevent FileNotFoundError on Windows
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load models safely using absolute paths
model = joblib.load(os.path.join(BASE_DIR, "models", "credit_card_model.pkl"))
gender_encoder = joblib.load(os.path.join(BASE_DIR, "models", "gender_encoder.pkl"))
car_encoder = joblib.load(os.path.join(BASE_DIR, "models", "car_encoder.pkl"))
realty_encoder = joblib.load(os.path.join(BASE_DIR, "models", "realty_encoder.pkl"))
income_encoder = joblib.load(os.path.join(BASE_DIR, "models", "income_encoder.pkl"))
education_encoder = joblib.load(os.path.join(BASE_DIR, "models", "education_encoder.pkl"))
family_encoder = joblib.load(os.path.join(BASE_DIR, "models", "family_encoder.pkl"))
housing_encoder = joblib.load(os.path.join(BASE_DIR, "models", "housing_encoder.pkl"))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict")
def predict_page():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    try:
        # 1. Extract inputs from the HTML form
        gender = request.form["gender"]
        own_car = request.form["own_car"]
        own_realty = request.form["own_realty"]
        children = int(request.form["children"])
        income = float(request.form["income"])
        income_type = request.form["income_type"]
        education = request.form["education"]
        family = request.form["family_status"]
        housing = request.form["housing_type"]
        birth = int(request.form["days_birth"])
        employed = int(request.form["days_employed"])
        mobil = int(request.form["mobil"])
        work_phone = int(request.form["work_phone"])
        phone = int(request.form["phone"])
        email = int(request.form["email"])
        family_members = float(request.form["family_members"])

        # 2. Transform categorical inputs using loaded encoders
        gender_encoded = gender_encoder.transform([gender])[0]
        own_car_encoded = car_encoder.transform([own_car])[0]
        own_realty_encoded = realty_encoder.transform([own_realty])[0]
        income_type_encoded = income_encoder.transform([income_type])[0]
        education_encoded = education_encoder.transform([education])[0]
        family_encoded = family_encoder.transform([family])[0]
        housing_encoded = housing_encoder.transform([housing])[0]

        # 3. Create structural array for the model
        features = np.array([[
            gender_encoded,
            own_car_encoded,
            own_realty_encoded,
            children,
            income,
            income_type_encoded,
            education_encoded,
            family_encoded,
            housing_encoded,
            birth,
            employed,
            mobil,
            work_phone,
            phone,
            email,
            family_members
        ]])

        # 4. Predict
        prediction = model.predict(features)[0]
        
        # Fixed variable conflict (changed variable 'result' to 'prediction_text')
        if prediction == 1:
            prediction_text = "Approved ✅"
            color = "green"
        else:
            prediction_text = "Rejected ❌"
            color = "red"

        return render_template(
            "result.html",
            prediction=prediction_text,
            color=color
        )

    except Exception as e:
        # Prints the error directly to your VS Code terminal for easier debugging
        print(f"Form submission error: {e}")
        return render_template(
            "result.html",
            prediction="Error",
            color="red",
            error=str(e)
        )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)