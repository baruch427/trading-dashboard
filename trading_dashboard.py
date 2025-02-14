import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import time

# Initialize Firebase
cred = credentials.Certificate("serviceAccount.json")  # Your Firebase credentials
firebase_admin.initialize_app(cred)
db = firestore.client()

# Streamlit UI
st.title("📈 Live Trading Dashboard")

# Function to fetch trading data from Firebase
def get_trade_data():
    doc_ref = db.collection("trading_data").document("MT5_Live")
    doc = doc_ref.get()
    return doc.to_dict() if doc.exists else None

# Live update loop
while True:
    trade_data = get_trade_data()
    if trade_data:
        st.subheader("💰 Account Summary")
        st.metric(label="Balance", value=f"${trade_data['balance']:.2f}")
        st.metric(label="Equity", value=f"${trade_data['equity']:.2f}")
        st.metric(label="Margin", value=f"${trade_data['margin']:.2f}")
        st.metric(label="Profit", value=f"${trade_data['profit']:.2f}")

    time.sleep(5)  # Update every 5 seconds
