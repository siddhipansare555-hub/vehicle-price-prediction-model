import streamlit as st
import pickle
import pandas as pd
from datetime import datetime
import numpy as np

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="wide"
)

# ---------------- LOAD MODEL ---------------- #
model = pickle.load(open('final_model.pkl', 'rb'))
columns = pickle.load(open('columns.pkl', 'rb'))

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #141e30, #243b55);
    color: white;
}

/* Card */
.card {
    background: #1c1f26;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
    height: 100%;
}

/* Title */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #ccc;
}

/* Result */
.result-card {
    background: linear-gradient(to right, #0072ff, #00c6ff);
    padding: 30px;
    border-radius: 15px;
    text-align: center;
    color: white;
    font-size: 26px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #
st.markdown('<div class="title">🚗 Car Price Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">ML-powered used car price estimator</div>', unsafe_allow_html=True)
st.markdown("---")

# ---------------- INPUT SECTION ---------------- #
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🔧 Basic Details")

    insurance_validity = st.selectbox(
        'Insurance validity',
        ['Comprehensive', 'Third Party insurance', 'Zero Dep', 'Not Available']
    )

    fuel_type = st.selectbox(
        'Fuel Type',
        ['Petrol', 'Diesel', 'CNG']
    )

    ownership = st.selectbox(
        'Ownership',
        ['First Owner', 'Second Owner', 'Third Owner', 'Fourth Owner']
    )

    transmission = st.selectbox(
        'Transmission',
        ['Manual', 'Automatic']
    )

    kms_driven = st.number_input('KMs Driven', min_value=0)

    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### ⚙️ Technical Details")

    seats = st.number_input('Seats', min_value=2, max_value=10, value=5)
    mileage = st.number_input('Mileage (kmpl)')
    engine = st.number_input('Engine (cc)')
    max_power = st.number_input('Max Power (bhp)')
    torque = st.number_input('Torque (Nm)')
    manufacturing_year = st.number_input(
        'Manufacturing Year', min_value=1990, max_value=2026
    )

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------- PREDICTION ---------------- #
if st.button('🚀 Predict Price'):

    with st.spinner("Predicting price... ⏳"):
        try:
            current_year = datetime.now().year
            car_age = current_year - manufacturing_year

            input_dict = {
                'kms_driven': kms_driven,
                'seats': seats,
                'mileage(kmpl)': mileage,
                'engine(cc)': engine,
                'max_power(bhp)': max_power,
                'torque(Nm)': torque,
                'car_age': car_age,
                'insurance_validity': insurance_validity,
                'fuel_type': fuel_type,
                'ownership': ownership,
                'transmission': transmission
            }

            input_df = pd.DataFrame([input_dict])
            input_df = pd.get_dummies(input_df)
            input_df = input_df.reindex(columns=columns, fill_value=0)

            prediction = model.predict(input_df)[0]

            # Convert to INR
            price_rs = int(prediction * 100000)

            # Confidence range (±10%)
            lower = prediction * 0.9
            upper = prediction * 1.1

        except Exception as e:
            st.error("⚠️ Error occurred")
            st.write(e)
            st.stop()

    # ---------------- RESULT DISPLAY ---------------- #
    st.markdown(f"""
    <div class="result-card">
        💰 Estimated Price <br><br>
        ₹ {price_rs:,} <br>
        ({prediction:.2f} Lakhs) <br><br>
        📊 Range: {lower:.2f}L – {upper:.2f}L
    </div>
    """, unsafe_allow_html=True)

    st.success("✅ Prediction completed successfully!")

# ---------------- SIDEBAR ---------------- #
st.sidebar.title("📌 About")
st.sidebar.info("""
🚗 Car Price Prediction App  

🔹 Model: Random Forest  
🔹 Accuracy: ~90% R²  
🔹 Real-time prediction  
""")