from agent.config import WEATHER_DATA


def query_weather_tool(city):
    if not city:
        return {"ok": False, "error": "No city provided"}

    payload = WEATHER_DATA.get(city.lower())
    if not payload:
        return {"ok": False, "error": f"No weather data found for '{city}'"}

    return {"ok": True, "data": payload}
