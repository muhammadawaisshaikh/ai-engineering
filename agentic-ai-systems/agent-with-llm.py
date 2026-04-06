from openai import OpenAI

client = OpenAI()

def ai_agent(task):
    prompt = f"""
    You are an intelligent AI agent.
    Break down the task and suggest next steps.

    Task: {task}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

print(ai_agent("Build a secure login system with validation"))
print(ai_agent("Test the new feature for edge cases"))
print(ai_agent("Handle customer support request about billing issue"))
