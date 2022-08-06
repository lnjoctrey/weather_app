import requests as r
import streamlit as st


def main():
    """ 
    - define the API Key,
    - defines Base url
    - Takes user input and returns the weather
    - UI through streamlit  
    
    """ 
    API_KEY = "ff556c8a56917d1b6a26df7cad50b4b0"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    options = ["Check Weather", "About App", "Developer"]
    with st.sidebar:
        radio = st.radio(
            'Hello',
            (options)
        )

    if radio == options[0]:
        st.title('Weather App') 
        
        city = st.text_input("Enter a city name: ")
        request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
        response = r.get(request_url)

        if response.status_code == 200:
            data = response.json()
            weather = data['weather'][0]['description']
            st.write("Current Weather: ", weather)
            temperature = round(data['main']['temp'] - 273.15, 2)
            st.write("Temperature: ", temperature, "celcius")

    if radio == options[1]:
        st.subheader("About App")
        st.markdown(
            """This a simple app that gives you the current weather report.
            This app gets it's weather report througn the '**Open Weather Map**' API. 
            \n
            \n I tried the project out just to see how it would work via **Streamlit.**
            """
            )

    if radio == options[2]:
        st.subheader("Developer")

# make it run online
if __name__ == '__main__':
    main()