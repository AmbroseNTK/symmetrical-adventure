import streamlit as st
import google.generativeai as genai
import model 
from pages import chat


# create a control dashboard for the web app
st.sidebar.subheader('Dashboard')

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'Select a page:',
    ('Dashboard', 'Control', 'Chat')
)


# Display the selected page
if add_selectbox == 'Dashboard':
    st.write('This is the dashboard page')
    st.write('Here you can see the current status of the system')
elif add_selectbox == 'Control':
    st.write('This is the control page')
    st.write('Here you can control the system')
else:
    chat.prompt()


                
            
        
