import streamlit as st
import functions as ft


# Streamlit UI
# st.title("Unit Convertor")
st.write(f"<h1 style='font-size:48px; color:red; text-align:center; background-color:grey; border-radius:50px;  margin:20px auto;'>Unit Convertor</h1>", unsafe_allow_html=True)

category = st.selectbox("Select Category", ["Distance", "Temperature", "Weight", "Pressure", "Speed"])

if category == "Distance":
    st.write("<h4 style='color:blue; text-align:center;'>Distance Conversion</h>", unsafe_allow_html=True)
    from_unit = st.selectbox("From", ["Meters", "Kilometers", "Feet", "Miles"])
    to_unit = st.selectbox("To", ["Meters", "Kilometers", "Feet", "Miles"])
    value = st.number_input("Enter Value")
    result = ft.distance_converter(from_unit, to_unit, value)
    st.write(f"<p style='font-size:24px; color:green;  text-align:center;'>{value} {from_unit} is equal to {result:.2f} {to_unit}</p>", unsafe_allow_html=True)

elif category == "Temperature":
    st.write("<h4 style='color:blue; text-align:center;'>Temperature Conversion</h>", unsafe_allow_html=True)
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit"])
    value = st.number_input("Enter Value")
    result = ft.temperature_converter(from_unit, to_unit, value)
    st.write(f"<p style='font-size:24px; color:green; text-align:center;'>{value} {from_unit} is equal to {result:.2f} {to_unit}</p>", unsafe_allow_html=True)

elif category == "Weight":
    st.write("<h4 style='color:blue; text-align:center;'>Weight Conversion</h>", unsafe_allow_html=True)
    from_unit = st.selectbox("From", ["Kilograms", "Grams", "Pounds", "Ounces"])
    to_unit = st.selectbox("To", ["Kilograms", "Grams", "Pounds", "Ounces"])
    value = st.number_input("Enter Value")
    result = ft.weight_converter(from_unit, to_unit, value)
    st.write(f"<p style='font-size:24px; color:green; text-align:center;'>{value} {from_unit} is equal to {result:.2f} {to_unit}</p>", unsafe_allow_html=True)

elif category == "Pressure":
    st.write("<h4 style='color:blue; text-align:center;'>Pressure Conversion</h>", unsafe_allow_html=True)
    from_unit = st.selectbox("From", ["Pascals", "Hectopascals", "Kilopascals", "Bar"])
    to_unit = st.selectbox("To", ["Pascals", "Hectopascals", "Kilopascals", "Bar"])
    value = st.number_input("Enter Value")
    result = ft.pressure_converter(from_unit, to_unit, value)
    st.write(f"<p style='font-size:24px; color:green; text-align:center;'>{value} {from_unit} is equal to {result:.2f} {to_unit}</p>", unsafe_allow_html=True)
    
elif category == "Speed":
    st.write("<h4 style='color:blue; text-align:center;'>Speed Conversion</h>", unsafe_allow_html=True)
    from_unit = st.selectbox("From", ["Meter per Second","Kilometre per Hour","foot per Second","Mile per Hour"])
    to_unit = st.selectbox("To", ["Meter per Second","Kilometre per Hour","foot per Second","Mile per Hour"])
    value = st.number_input("Enter Value ")
    result = ft.speed_convertor(from_unit, to_unit, value)
    st.write(f"<p style='font-size:24px; color:green; text-align:center;'>{value} {from_unit} is equal to {result:.2f} {to_unit}</p>", unsafe_allow_html=True)
    
    

