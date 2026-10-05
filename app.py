
from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load trained model
with open("titanic_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load preprocessor
with open("titanic_preprocessor.pkl", "rb") as f:
    preprocessor = pickle.load(f)


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        data = {
            "Pclass": int(request.form["Pclass"]),
            "Sex": request.form["Sex"],
            "Age": float(request.form["Age"]),
            "sibsp": int(request.form["SibSp"]),
            "Parch": int(request.form["Parch"]),
            "Fare": float(request.form["Fare"]),
            "Embarked": request.form["Embarked"]
        }

        passenger = pd.DataFrame([data])

        processed = preprocessor.transform(passenger)

        prediction = model.predict(processed)[0]

        if prediction == 1:
            result = "🚢 Prediction: Survived"
        else:
            result = "🌊 Prediction: Did Not Survive"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)