# BMI Calculator

import streamlit as st
import pandas as pd

# Set the page configuration
st.set_page_config(page_title="BMI Calculator", page_icon=":weight_lifter:", layout="wide")

st.title("BMI Calculator ")
st.write("This app calculates your Body Mass Index (BMI) based on your weight and height.")

# BMI cateories
st.write("BMI Categories:")
st.write("1. Underweight: BMI less then 18.5")
st.write("2. Normal weight: BMI between 18.5 and 24.9")
st.write("3. Overweight: BMi between 25 and 29.9")
st.write("4. Obesity: BMI 30 or greater")

weight = st.number_input("Enter your weight in (kg): ", min_value=0.0, format="%.1f")
height = st.number_input("Enter your height in (meter): ", min_value=0.0, format="%.2f")

# Add a button to calculate BMI
if st.button("Calculate BMI"):
    # Validate inputs
    if height == 0:
        st.error("Height cannot be zero.")
    else:
        bmi = weight / (height ** 2) 
        st.write(f"Your BMI is: {bmi:.2f}")
     
    # Provide feedback based on BMI value   
    if bmi < 18.5:
        st.warning("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")
