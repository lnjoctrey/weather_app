from email.mime import image
import requests as r
import streamlit as st
from PIL import Image
import time 


def main():
    """ 
    - define the API Key,
    - defines Base url
    - Takes user input and returns the weather
    - UI through streamlit  
    
    """ 
    API_KEY = "ff556c8a56917d1b6a26df7cad50b4b0"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    options = ["Check Current Weather", "About App", "Developer"]
    with st.sidebar:
        radio = st.radio(
            'Hello',
            (options)
        )
    # Front Current Weather App page
    if radio == options[0]:
        st.title('Current Weather App')
        weather_pic = Image.open('resources/lago-di-limides-3025780_1920.jpg')
        st.image(weather_pic, caption='Credit: Image by Julius Silver from Pixabay ')
        
        city = st.text_input("Enter a city name: ")
        request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
        response = r.get(request_url)

        if response.status_code == 200:
            data = response.json()
            weather = data['weather'][0]['description']
            st.write("Current Weather: ", weather)
            temperature = round(data['main']['temp'] - 273.15, 2)
            st.write("Temperature: ", temperature, "celcius")

    # About the App Page
    if radio == options[1]:
        st.subheader("About App")
        app_pic = Image.open('resources/mobile-phone-1875813_1920.jpg')
        st.image(app_pic, caption='Credit: Image by David from Pixabay')
        st.markdown(
            """This a simple app that gives you the current weather report.
            This app gets it's weather report througn the '**Open Weather Map**' API. 
            \n
            \n I tried the project out just to see how it would work via **Streamlit.**
            """
            )

    if radio == options[2]:
        st.subheader("Developer")
        profile_pic = Image.open('resources/IMG_20191006_073325_792.jpg')
        st.image(profile_pic, caption='Lungisa Joctrey')
        st.markdown(
            """
            Hi, I am Lungisa and I am based in South Africa. I am a recently qualified Data Scientist and I am actively searching for a job.\n
            I have two years experience in Python Programming, and one year experience in Statistical Analysis, SQL, Power BI, Anaconda, Jupyter Lab and Jupyter Notebook.
            I am a self driven, fast learner and I am not afraid to try new things.
        
            """)
        

# make it run online
if __name__ == '__main__':
    main()