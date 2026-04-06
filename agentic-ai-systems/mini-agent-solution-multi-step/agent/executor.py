from agent.analyzer import analyze_task
from agent.tools import query_pricing_tool, query_weather_tool


def execute_plan(task, plan):
    """Execute a plan using mock tool endpoints."""
    analysis = analyze_task(task)
    intent = analysis["intent"]
    entity = analysis["entity"]
    trace = []

    if intent == "get_weather":
        trace.append({"step": plan[0], "status": "done"})
        tool_result = query_weather_tool(entity)
        trace.append({"step": plan[1], "status": "done", "tool_result": tool_result})

        if tool_result["ok"]:
            data = tool_result["data"]
            summary = (
                f"Weather in {entity}: {data['temperature_c']}C, "
                f"{data['condition']}, humidity {data['humidity_pct']}%."
            )
            trace.append({"step": plan[2], "status": "done"})
            return {"ok": True, "summary": summary, "raw": data, "trace": trace}

        return {"ok": False, "summary": tool_result["error"], "raw": None, "trace": trace}

    if intent == "get_price":
        trace.append({"step": plan[0], "status": "done"})
        tool_result = query_pricing_tool(entity)
        trace.append({"step": plan[1], "status": "done", "tool_result": tool_result})

        if tool_result["ok"]:
            data = tool_result["data"]
            summary = (
                f"Price of {entity}: {data['price_eur']} {data['currency']} "
                f"at {data['store']}."
            )
            trace.append({"step": plan[2], "status": "done"})
            return {"ok": True, "summary": summary, "raw": data, "trace": trace}

        return {"ok": False, "summary": tool_result["error"], "raw": None, "trace": trace}

    trace.append({"step": plan[0], "status": "done"})
    return {
        "ok": False,
        "summary": "Unsupported task type. Supported: weather lookup, price lookup.",
        "raw": None,
        "trace": trace,
    }
