def analyze_task(task):
    return {
        "original_task": task,
        "needs_weather": "weather" in task.lower(),
        "needs_price": "price" in task.lower()
    }


def plan_solution(task_analysis):
    plan = []

    if task_analysis["needs_weather"]:
        plan.append("Use weather tool")

    if task_analysis["needs_price"]:
        plan.append("Use pricing tool")

    if not plan:
        plan.append("Respond directly without tools")

    return plan


def execute_plan(task, plan):
    results = []

    for step in plan:
        if step == "Use weather tool":
            results.append(call_tool(task))
        elif step == "Use pricing tool":
            results.append(call_tool(task))
        else:
            results.append("Direct response: No tool needed")

    return results


def validate_result(results):
    for result in results:
        if "not available" in result.lower() or "not found" in result.lower():
            return "Validation failed: incomplete result"
    return "Validation successful"


def agent_loop(task):
    analysis = analyze_task(task)
    print("Analysis:", analysis)

    plan = plan_solution(analysis)
    print("Plan:", plan)

    results = execute_plan(task, plan)
    print("Execution Results:", results)

    validation = validate_result(results)
    print("Validation:", validation)


agent_loop("Get weather in Vaasa")
agent_loop("Get price of headphones")
agent_loop("Get weather in Oulu")
agent_loop("Get price of smartphone")
