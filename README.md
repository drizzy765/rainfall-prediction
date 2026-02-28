# 🌧️ Rainfall Prediction App

Try it live: [**Rainfall Prediction App**](https://rainfall-prediction-pdg3yzbenj9ddevli84lhl.streamlit.app/)

This Streamlit web application predicts the likelihood of rainfall based on various atmospheric conditions. By leveraging machine learning, it provides a simple and interactive interface for users to input weather metrics and receive instant predictions.

---

## ✨ Features

* **Live Prediction:** Utilizes a pre-trained machine learning model (`rainfall_prediction_model.pkl`) to forecast rain.
* **Custom Inputs:** Accepts user-defined atmospheric conditions, including:
    * Pressure
    * Humidity
    * Sunshine
    * Wind Speed & Direction
    * Dew Point
    * Cloud Cover
* **Interactive UI:** Built entirely with Streamlit for a fast, responsive, and user-friendly experience.

---

## 🛠️ Setup and Installation

Follow these steps to run the application on your local machine.

**1. Create a virtual environment (Recommended)**
```bash
python -m venv .venv
2. Activate the virtual environment

Windows:

Bash
.venv\Scripts\activate
macOS/Linux:

Bash
source .venv/bin/activate
3. Install dependencies

Bash
pip install -r requirements.txt
💻 Running the App
Once your environment is set up and dependencies are installed, you can launch the app locally by executing the following command in your terminal:

Bash
streamlit run app.py
📂 Project Structure
app.py: The main Python script containing the Streamlit application code.

requirements.txt: List of required Python packages (streamlit, pandas, scikit-learn, joblib).

rainfall_prediction_model.pkl: The exported, pre-trained predictive machine learning model.

Rainfall.csv: The original dataset used to train and test the model.

rainfallprediction (1).ipynb: A Jupyter Notebook containing the data exploration, preprocessing, and model training workflow.
