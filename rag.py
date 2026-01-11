import json
with open('data/knowledge_base.json') as f:
    KB = json.load(f)

def answer_pricing():
    return f"Basic: {KB['plans']['basic']['price']} | Pro: {KB['plans']['pro']['price']}"
