import streamlit as st
import functions as ft

# import for chat bot
import os

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai



# Streamlit UI
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
    
    



# Load environment variables
load_dotenv()


# calling API key from .env file
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-2.0-flash')


# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role


# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])


# Display the chatbot's title on the page
st.write(f"<h1 style='font-size:48px; color:orange; text-align:center; background-color:grey; border-radius:50px;  margin:20px auto;'>CHAT WITH ME</h1>", unsafe_allow_html=True)


# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input field for user's message
user_prompt = st.chat_input("Let's chat....")
if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)

    # Send user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)
