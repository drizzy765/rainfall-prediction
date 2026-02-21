# Rainfall Prediction App

This is a Streamlit web application that predicts rainfall based on atmospheric conditions. 

## Features
- Predicts rainfall using a trained machine learning model (`rainfall_prediction_model.pkl`).
- Takes user inputs for atmospheric conditions like Pressure, Humidity, Sunshine, Wind Speed, Dew Point, Cloud Cover, and Wind Direction.
- Interactive user interface built with Streamlit.

## Setup and Installation

1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the App

To run the Streamlit application, execute the following command in your terminal:

```bash
streamlit run app.py
```

## Files
- `app.py`: The main Streamlit Python script.
- `requirements.txt`: List of required Python packages (`streamlit`, `pandas`, `scikit-learn`, `joblib`).
- `rainfall_prediction_model.pkl`: The trained predictive model.
- `Rainfall.csv`: The dataset used to train the model.
- `rainfallprediction (1).ipynb`: A Jupyter Notebook containing the data exploration and model training code.
