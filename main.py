from agent.agent import agent_app

state = {
    "messages": [],
    "intent": None,
    "name": None,
    "email": None,
    "platform": None
}

while True:
    user_input = input("User: ")
    state["messages"].append(user_input)

    if state["intent"] == "high_intent":
        if state["name"] is None:
            state["name"] = user_input
        elif state["email"] is None:
            state["email"] = user_input
        elif state["platform"] is None:
            state["platform"] = user_input

    state = agent_app.invoke(state)
    print("Agent:", state["messages"][-1])
