# 🚢 Titanic AI — Survival Predictor

A Machine Learning web application that predicts whether a Titanic passenger would survive based on their personal and travel information.

The project combines a trained Machine Learning model with a Flask web interface to provide real-time survival predictions.

## ✨ Features

- 🚢 Titanic passenger survival prediction
- 🤖 Machine Learning model using Random Forest
- 🧹 Data preprocessing and feature transformation
- 🌐 Flask-based web application
- 🎨 Interactive and responsive user interface
- 📊 Prediction result displayed directly on the webpage

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML
- CSS
- Git & GitHub

## 🧠 Machine Learning

The project uses a **Random Forest Classifier** for prediction.

### Input Features

The application uses the following passenger information:

- Passenger Class
- Sex
- Age
- Siblings / Spouse Aboard
- Parents / Children Aboard
- Ticket Fare
- Port of Embarkation

The preprocessing pipeline handles numerical and categorical features before passing them to the trained model.

## 📁 Project Structure

```text
titanic-survival-prediction/
│
├── app.py
├── titanic_model.pkl
├── titanic_preprocessor.pkl
├── .gitignore
│
├── templates/
│   └── index.html
│
└── README.md