import streamlit as st
import pandas as pd
import joblib

# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load('rainfall_prediction_model.pkl')

model = load_model()

# Create the Streamlit app interface
st.title("Rainfall Prediction App")
st.write("Enter the atmospheric conditions below to predict whether it will rain today.")

# Create input fields for user input
col1, col2 = st.columns(2)

with col1:
    pressure = st.number_input("Pressure (hPa)", min_value=900.0, max_value=1100.0, value=1015.0, step=0.1)
    humidity = st.number_input("Humidity (%)", min_value=0, max_value=100, value=50, step=1)
    sunshine = st.number_input("Sunshine (hours)", min_value=0.0, max_value=24.0, value=5.0, step=0.1)
    windspeed = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=200.0, value=15.0, step=0.1)

with col2:
    dewpoint = st.number_input("Dew Point (°C)", min_value=-50.0, max_value=50.0, value=10.0, step=0.1)
    cloud = st.number_input("Cloud Cover (%)", min_value=0, max_value=100, value=50, step=1)
    winddirection = st.number_input("Wind Direction (°)", min_value=0, max_value=360, value=180, step=1)

# Create a clear button and a predict button
if st.button("Predict Rainfall"):
    # Create a DataFrame from the inputs
    input_data = {
        'pressure': [pressure],
        'dewpoint': [dewpoint],
        'humidity': [humidity],
        'cloud': [cloud],
        'sunshine': [sunshine],
        'winddirection': [winddirection],
        'windspeed': [windspeed]
    }
    input_df = pd.DataFrame(input_data)
    
    # Make the prediction
    try:
        prediction = model.predict(input_df)[0]
        
        # Display the result
        if prediction == 1:
            st.error("⛈️ Prediction: There will be rainfall.")
        else:
            st.success("☀️ Prediction: No rainfall.")
            
    except Exception as e:
        st.error(f"Error during prediction: {str(e)}")
        st.info("The model might be expecting different feature names or types. Please check the model inputs.")
