# Symbolic AI / Rule-Based Decision System for weather alerts
def weather_alert(temperature, humidity):
    if temperature > 100 and humidity > 70:
        return "Extreme heat warning!"
    elif temperature > 100:
        return "Too hot!"
    elif temperature < 40:
        return "Too cold!"
    else:
        return "Weather is normal."

print(weather_alert(105, 60))
