import streamlit as st
import pandas as pd
import numpy as np

st.title("NEPSE AI Predictor")

volume = st.number_input("Volume")
close = st.number_input("Previous Close")

if st.button("Predict"):
    if volume > close:
        st.success("Market likely Bullish")
    else:
        st.warning("Market likely Bearish")
