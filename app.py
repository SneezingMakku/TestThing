import streamlit as st
import pandas as pd
import joblib

st.title("Voorspelling Montage Uitgaven (DEBUG)")
st.write("Deze versie toont eventuele fouten bij het laden van het model.")

try:
    model = joblib.load("random_forest_montage_model.pkl")
    st.success("✅ Model succesvol geladen!")

    jaar = st.number_input("Jaar", min_value=2020, max_value=2030, value=2025)
    maand = st.number_input("Maand", min_value=0, max_value=11, value=0)
    tijdindex = st.number_input("TijdIndex", min_value=0, max_value=100, value=0)

    if st.button("Voorspel"):
        input_df = pd.DataFrame([[jaar, maand, tijdindex]], columns=["Jaar", "Maand", "TijdIndex"])
        voorspelling = model.predict(input_df)[0]
        st.success(f"Geschatte Montage Uitgaven: €{voorspelling:,.2f}")

except Exception as e:
    st.error("❌ Er is een fout opgetreden bij het laden van het model:")
    st.exception(e)
