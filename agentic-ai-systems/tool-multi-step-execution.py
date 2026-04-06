def run_agent(task):
    analysis = analyze_task(task)
    plan = plan_solution(analysis)
    results = execute_plan(task, plan)
    validation = validate_result(results)

    return {
        "task": task,
        "plan": plan,
        "results": results,
        "validation": validation
    }


response = run_agent("Get weather in Vaasa")
print(response)
response = run_agent("Get price of headphones")
print(response)
response = run_agent("Get weather in Oulu")
print(response)
response = run_agent("Get price of smartphone")
print(response)