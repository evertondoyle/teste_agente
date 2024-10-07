#import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key = GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash' ,generation_config=genai.GenerationConfig(
        temperature=0.9))
response = model.generate_content(input('Entre com o Prompt: '))
print(response.text)

#st.write('Ta funcionando a bagaça 2')

