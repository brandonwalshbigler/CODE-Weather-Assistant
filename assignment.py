import random

# Name
# CIS 3330
# CODE 1 - Weather Assistant
# Conversion formula: (Temperature in °F - 32) * .5556
# Note that the message to user should be the following
# "What is the temperature outside: "

def main():

cold_weather_clothing = ["heavy jacket","scarf","hat"]
cool_weather_clothing = ["jacket","sweater","gloves"]
warm_weather_clothing = ["sun glasses","t-shirt","hat"]
hot_weather_clothing = ["sun screen","water","shorts"]

        
def get_temperature_in_celsius(temp_in_f):
    temp_in_c = (temp_in_f - 32) * .5556
    return temp_in_c
def get_temperature_in_kelvin_from_c(temp_in_c):
    temp_in_k = temp_in_c + 273.15
    return temp_in_k
def get_temperature_in_kelvin_from_f(temp_in_f):
    temp_in_k = ((temp_in_f - 32) * .5556) + 273.15
    return temp_in_k
def get_clothing_recommendation(temp_in_c):
    if temp_in_c <= 10:
        cold_item = random.choice(cold_weather_clothing)
        return cold_item
    elif temp_in_c > 10 and temp_in_c <= 15: 
        cool_item = random.choice(cool_weather_clothing)
        return cool_item
    elif temp_in_c > 15 and temp_in_c <= 25:
        warm_item = random.choice(warm_weather_clothing)
        return warm_item
    elif temp_in_c > 26 and temp_in_c <= 35:
        hot_item = random.choice(hot_weather_clothing)
        return hot_item

if __name__ == "__main__":
    main()
