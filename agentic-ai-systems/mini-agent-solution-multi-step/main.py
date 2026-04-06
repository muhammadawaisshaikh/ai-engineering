from agent.orchestrator import run_agent


def main():
    tasks = [
        "Get weather in Vaasa",
        "Get price of headphones",
        "Get weather in Oulu",
        "Get price of smartphone",
    ]

    for task in tasks:
        response = run_agent(task)
        print(response)


if __name__ == "__main__":
    main()
