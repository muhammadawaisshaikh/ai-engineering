from agent.analyzer import analyze_task
from agent.executor import execute_plan
from agent.planner import plan_solution
from agent.validator import validate_result


def run_agent(task):
    analysis = analyze_task(task)
    plan = plan_solution(analysis)
    results = execute_plan(task, plan)
    validation = validate_result(results)

    return {
        "task": task,
        "analysis": analysis,
        "plan": plan,
        "results": results,
        "validation": validation,
    }
