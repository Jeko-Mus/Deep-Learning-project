import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


st.markdown('# Familyiar App')
st.write(''' This project aims to build a chatbot to help with finding familiar back home favourites, 
            be it food, hair and beauty products or social activities when travelling or moving to a new city.''')

st.markdown('#### Reason behind the need for this App')
st.markdown('###### Many people move to new countries and cities across the world everyday')
st.markdown('###### Taking just Germany as an example with a population of 83 million. Todays presentation and chatbot will focus on just Berlin where 20% of the 3.6m population in Berlin are foreigners')
st.markdown('##### Germany foreigners statistics')
image = Image.open('migration_and_integration.png')
st.image(image) 
st.markdown('https://www.destatis.de/ (Dec, 2021)')
st.markdown('##### Share of foreigners in Germany among the total population from 1991 to 2020')
image2 = Image.open('share_of_foreigners.png')
st.image(image2)
st.markdown('statista.com')

st.markdown('### Inputs to be required for the Website/App')
city = st.text_input('Current city')
st.write(city)
country = st.text_input('Specific country whose products/services you would like information on')
st.write(country)
search = st.text_input('What you are searching for')
st.write(search)
favour = st.text_input('Please provide a favourite place you have found that reminds you of home so we can add it to our database for other users')
st.markdown(favour)

st.markdown('###### Based on your answers, we would reccommend you tryout....')


st.markdown('#### Chatbot to be used to assist on the website')



st.markdown('### To dos left')
st.markdown('- Incorporate other nationalities and cities')
st.markdown('- Incorporate more options eg general city advice section?')
st.markdown('- Create the website/ App')


