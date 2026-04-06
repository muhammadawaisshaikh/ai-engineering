def plan_solution(analysis):
    """Generate a simple, explicit plan from analysis."""
    intent = analysis["intent"]
    entity = analysis["entity"]

    if intent == "get_weather":
        return [
            "Validate city extracted from user task",
            f"Call weather tool for city '{entity}'",
            "Format weather response",
        ]

    if intent == "get_price":
        return [
            "Validate product extracted from user task",
            f"Call pricing tool for product '{entity}'",
            "Format price response",
        ]

    return ["Return graceful fallback for unsupported intent"]
