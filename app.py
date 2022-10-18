import streamlit as st
import joblib


model = joblib.load('spam-ham') # we are li=oding the pipeline model using joblib
st.title('SPAM-HAM CLASSIFIER') # It creates a title in web app
ip = st.text_input('Enter the message') # It create a text box in WEBAPP
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
