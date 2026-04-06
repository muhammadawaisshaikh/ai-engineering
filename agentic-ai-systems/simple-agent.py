def agent(task):
    if "code" in task:
        return "Developer Agent assigned to write code"
    elif "test" in task:
        return "QA Agent assigned to test functionality"
    else:
        return "General Agent handling the request"

print(agent("write code for login system"))
print(agent("test the new feature"))
print(agent("handle customer support request"))
