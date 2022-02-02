import requests
import pandas as pd
import numpy as np
from Functions import calc_mean, calc_median


temp_list = []
hum_list = []
ans=True
api_key = '3d2d38480e022a3914b5040a40b17199'

while ans:
    print("\n")
    print("""
     ###############  
     ## MAIN MENU ##
     ###############
    """)
    print("""
        1.Sensor Metrics
        2.Average of sensor metrics   
        3.Exit/Quit
        """)
    ans= input("What would you like to do? ")
    if ans=="1":
        user_input = input("Enter City/Country name: ")

        # print(user_input)

        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

        if weather_data.json()['cod'] == '404':
            print('City Country not found')
        else:
            weather = weather_data.json()['weather'][0]['main']
            temp = round(weather_data.json()['main']['temp'])
            hum = round(weather_data.json()['main']['humidity'])

            print(f"Weather conditions in {user_input} is: {weather}")
            print(f"The temperature in {user_input} is: {temp}°C")
            print(f"The humidity in {user_input} is: {hum} (grams per cubic meter)")

            dict = {'City': [user_input], 'weather': [weather], 'temperature': [temp], 'humidity': [hum]}

            df = pd.DataFrame(dict)

            df.to_csv(r'C:\Users\Joe\AdvancedMachineLearning\WeatherProject\Files\export_dataframe.csv', index=None)

    elif ans=="2":
        with open("weatherData.csv") as data_file:
            headers = data_file.readline()
            for line in data_file:
                city, temperature, humidity = line.split(",")

                temp_list.append(int(temperature))
                hum_list.append(int(humidity))

        print(f"Mean Temperature: {calc_mean(temp_list):.2f}°C")
        print(f"Mean Humidity: {calc_mean(hum_list):.2f}(grams per cubic meter)")
        print("")
        print(f"Median Temperature: {calc_median(temp_list):.2f}°C")
        print(f"Median Humidity: {calc_median(hum_list):.2f}(grams per cubic meter)")

    elif ans=="3":
        print("\n Goodbye")
        break
    elif ans !="":
        print("\n Choice is not valid, please try again")