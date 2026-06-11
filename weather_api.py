import requests

city = input("Enter city name: ")

url = f"https://wttr.in/{city}?format=j1"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        temperature = data["current_condition"][0]["temp_C"]
        weather = data["current_condition"][0]["weatherDesc"][0]["value"]
        humidity = data["current_condition"][0]["humidity"]

        print("\n===== WEATHER REPORT =====")
        print("City:", city.title())
        print("Temperature:", temperature, "°C")
        print("Weather:", weather)
        print("Humidity:", humidity, "%")

    else:
        print("Failed to fetch weather data.")

except requests.exceptions.RequestException:
    print("Error connecting to API.")