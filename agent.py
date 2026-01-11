from langgraph.graph import StateGraph
from agent.state import AgentState
from agent.intents import detect_intent
from agent.rag import answer_pricing
from agent.tools import mock_lead_capture

def agent_node(state: AgentState):
    user_msg = state['messages'][-1]
    intent = detect_intent(user_msg)
    state['intent'] = intent
    if intent == 'pricing': state['messages'].append(answer_pricing())
    elif intent == 'high_intent':
        if not state.get('name'): state['messages'].append('May I have your name?')
        elif not state.get('email'): state['messages'].append('Please share your email.')
        elif not state.get('platform'): state['messages'].append('Which platform do you create on?')
        else:
            mock_lead_capture(state['name'], state['email'], state['platform'])
            state['messages'].append('Lead captured successfully!')
    return state

graph = StateGraph(AgentState)
graph.add_node('agent', agent_node)
graph.set_entry_point('agent')
graph.set_finish_point('agent')
agent_app = graph.compile()
