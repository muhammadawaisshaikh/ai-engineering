import re


def analyze_task(task):
    """Extract intent and entity from a task string."""
    normalized_task = task.strip()
    lowered = normalized_task.lower()

    if "weather" in lowered:
        city_match = re.search(r"weather\s+in\s+(.+)$", normalized_task, re.IGNORECASE)
        city = city_match.group(1).strip() if city_match else None
        return {
            "intent": "get_weather",
            "entity_type": "city",
            "entity": city,
            "confidence": 0.95 if city else 0.65,
        }

    if "price" in lowered:
        product_match = re.search(r"price\s+of\s+(.+)$", normalized_task, re.IGNORECASE)
        product = product_match.group(1).strip() if product_match else None
        return {
            "intent": "get_price",
            "entity_type": "product",
            "entity": product,
            "confidence": 0.95 if product else 0.65,
        }

    return {
        "intent": "unknown",
        "entity_type": None,
        "entity": None,
        "confidence": 0.2,
    }
