from email.mime import image
from re import M
import requests as r
import streamlit as st
from PIL import Image
import datetime 


def main():
    """ 
    - define the API Key,
    - defines Base url
    - Takes user input and returns the weather
    - UI through streamlit  
    
    """ 
    # defining API parameters
    API_KEY = "ff556c8a56917d1b6a26df7cad50b4b0"
    API_KEY2 = "8041d04c4e8759a4836392b7f899447d"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    BASE_URL2 = "http://api.openweathermap.org/data/2.5/forecast"

    #setting up the sidebar
    options = ["Check Current Weather","Weather Forecast", "About App", "Developer"]
    with st.sidebar:
        radio = st.radio(
            'Hello',
            (options)
        )
    #Front Current Weather App page
    if radio == options[0]:
        st.title('Current Weather')
        weather_pic = Image.open('resources/lago-di-limides-3025780_1920.jpg')
        st.image(weather_pic, caption='Credit: Image by Julius Silver from Pixabay ')
        
        city = st.text_input("Enter a city name: ")
        request_url = f"{BASE_URL}?appid={API_KEY}&units=metric&q={city}"
        response = r.get(request_url)

        if response.status_code == 200:
            data = response.json()
            weather = data['weather'][0]['description']
            st.write("Current Weather: ", weather)
            temperature = round(data['main']['temp'], 2)
            st.write("Temperature: ", temperature, "celcius")

    if radio == options[1]:
        st.title('Weather Forecast')
        st.write('This section is still under development')
        weather_pic = Image.open('resources/lightning-2660929_1920.jpg')
        st.image(weather_pic, caption='Credit: Image by Gerd Altmann from Pixabay ')

        city = st.text_input("Enter a city name: ")
        request_url = f"{BASE_URL2}?appid={API_KEY2}&units=metric&q={city}"
        response2 = r.get(request_url)

        if response2.status_code == 200:
            data2 = response2.json()
            wf = data2["list"][:11][-1]
            dt = wf['dt_txt']
            st.write("Date: ", dt)
            st.write("Clouds: ", wf['weather'][0]['description'])
            st.write("Humidity: ", wf["main"]['humidity'])
            #st.write("Minimum Temp: ", round(wf["main"]['temp_min'], 2), "celcius")
            st.write("Maximum Temp: ", round(wf["main"]['temp_max'], 2), "celcius")
            st.write("Wind Speed: ", wf["wind"]["speed"], "kph")


    # About the App Page
    if radio == options[2]:
        st.subheader("About App")
        app_pic = Image.open('resources/mobile-phone-1875813_1920.jpg')
        st.image(app_pic, caption='Credit: Image by David from Pixabay')
        st.markdown(
            """This is a simple app that gives you the current weather report.
            This app gets it's weather report througn the '**Open Weather Map**' API. 
            \n
            \n I tried the project out just to see how it would work via **Streamlit.**
            I am still working on the 'Weather Forecast' section.
            """
            )

    if radio == options[3]:
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