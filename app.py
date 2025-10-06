import streamlit as st
import joblib

st.set_page_config(
    page_title="Exoplanet Classifier", 
    initial_sidebar_state="collapsed",
    page_icon="*"
)

with open("model/rf_model.pkl", "rb") as m:
    rf = joblib.load(m)

st.title("Exoplanet Classifier")

features = ["Orbital Period [days]", "Impact Parameter", "Transit Duration", "Transit Depth [ppm]", "Planetary Radius [Earth radii]", "Transit Signal-to-Noise", "Stellar Effective Temperature [K]", "Stellar Surface Gravity [log10(cm/s^2)]", "Stellar Radius [Solar radii]", "Not Transit-Like False Positive Flag", "Centroid Offset False Positive Flag", "Stellar Eclipse False Positive Flag", " Ephemeris Match Indicates Contamination False Positive Flag"]
inputFeat = []

for feature in features:
    inputFeat.append(st.number_input(label = f"{feature}: ", min_value = 0.00000, format = "%0.5f", key = feature))

if (all(inputFeat)):
    try:
        result = "Exoplanet" if (rf.predict([inputFeat]) == 1) else "Not exoplanet"
        st.header("> >" + result)
    except ValueError:
        st.warning("Please enter valid numeric values for all features.")
else:
    st.info("Please fill in all input values to get a prediction!")
