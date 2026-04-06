def get_weather(city):
    weather_data = {
        "Vaasa": "12°C, windy",
        "Helsinki": "15°C, cloudy",
        "Tampere": "10°C, rainy"
    }
    return weather_data.get(city, "Weather data not available")


def get_product_price(product_name):
    product_prices = {
        "laptop": 1200,
        "headphones": 250,
        "keyboard": 90
    }
    return product_prices.get(product_name.lower(), "Product not found")


def call_tool(task):
    task_lower = task.lower()

    if "weather in" in task_lower:
        city = task.split("in")[-1].strip()
        return f"Weather result: {get_weather(city)}"

    elif "price of" in task_lower:
        product = task.split("of")[-1].strip()
        return f"Price result: ${get_product_price(product)}"

    else:
        return "No matching tool found for this request."


print(call_tool("Get weather in Vaasa"))
print(call_tool("Get price of laptop"))
print(call_tool("Get weather in Helsinki"))
print(call_tool("Get price of headphones"))
print(call_tool("Get weather in Tampere"))
print(call_tool("Get price of keyboard"))
print(call_tool("Get weather in Oulu"))
print(call_tool("Get price of smartphone"))
