import os 
import streamlit as st

import google.generativeai as genai
# import the pillow so that we can work with images
from PIL import Image

# loading the invironment variables
from dotenv import load_dotenv
load_dotenv()

my_api_key = os.getenv("GOOGLE_API_KEY")

# configure the generative ai model with the retrieved api key
genai.configure(api_key = my_api_key)

# define out desired model
model = genai.GenerativeModel('gemini-1.5-flash')

# define a function that will generate responses using the model
def get_gemini_response(user_quest, image):
    response = model.generate_content([user_quest, image])

    return response.text

# setup the streamlit app
st.set_page_config(page_title = 'GeminiVision App', page_icon = '🤖')

st.title("Gemini PicAnalyzer Application ")
file = st.file_uploader('Choose an image...', type = ['png', 'jpg', 'webp'])

if file is not None:
    img = Image.open(file)
    st.image(img, width = 200)

st.subheader("Ask the model about the image")  
with st.form(key = 'input', clear_on_submit = True):
    user_quest = st.text_input("Enter Your question about an image you uploaded.", placeholder = 'Type here...')
    btn = st.form_submit_button()

if btn and user_quest:
    response = get_gemini_response(user_quest, img)
    st.subheader("Answer: ")
    st.write(response)
else:
    st.markdown('<div style="height: 150px;"></div>', unsafe_allow_html=True) 
    # st.info('This bot uses the Google\'s Generative AI model, gemini-1.5-flash, developed by Kaletsidik. The model generates text based on the given input query and image. If you need help with a specific issue, feel free to ask.')
    st.markdown('---')
    st.success("Made By Kaletsidik ©2024")