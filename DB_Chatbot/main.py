import streamlit as st
from chatbot import main_chatbot
from data_visualize import visualize_data

st.title("Interactive AI Hub")

option = st.sidebar.selectbox(
    'Choose your App',
    ('Chatbot', 'Data Visualization')
)

if option == 'Chatbot':
    main_chatbot()
elif option == 'Data Visualization':
    visualize_data()
