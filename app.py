import streamlit as st
import datetime as dt
import requests

date = st.date_input('Enter a date: ', value = dt.datetime(2014,7,6,19,18,0))
time = st.time_input('Enter a time: ', value = dt.datetime(2014,7,6,19,18,0))
pickup_longitude = st.number_input('Enter a pickup longitude: ', value =  -73.950655)
pickup_latitude = st.number_input('Enter a pickup latitude: ', value = 40.783282)
dropoff_longitude = st.number_input('Enter a dropoff longitude: ',value = -73.984365)
dropoff_latitude = st.number_input('Enter a dropoff latitude: ', value = 40.769802)
passenger_count = st.number_input('Number of passangers: ', value = 2)



dictionary = {
    'pickup_datetime': f'{date} {time}',
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': passenger_count,
}

url = 'https://taxifare.lewagon.ai/predict'

button = st.button('Press me')
if button :
    api = requests.get(url = url,params = dictionary).json()
    st.write(api)
    st.success(api['fare'])
    st.balloons()

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

 Finally, we can display the prediction to the user
'''
