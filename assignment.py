# Name
# CIS 3330
# CODE 1 - Weather Assistant
# Conversion formula: (Temperature in °F - 32) * .5556
# Note that the message to user should be the following
# "What is the temperature outside: "

def main():
    pass
     
    fahrenheit = int(input(
        "What is the temperature outside: "))
    temperature = fahrenheit
    
    celsius = (temperature - 32) * .5556

    if celsius < 10:
        print("Wear a heavy jacket")
    elif celsius >= 10 and celsius < 20:
        print("Wear a light jacket")
    elif celsius > 20:
        print("Wear a hat")

if __name__ == "__main__":
    main()