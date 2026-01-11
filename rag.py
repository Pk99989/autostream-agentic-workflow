import json

with open("data/knowledge_base.json") as f:
    KB = json.load(f)

def answer_pricing():
    basic = KB["plans"]["basic"]
    pro = KB["plans"]["pro"]

    return (
        f"Basic Plan:\n"
        f"- Price: {basic['price']}\n"
        f"- {basic['videos_per_month']}\n"
        f"- Resolution: {basic['resolution']}\n\n"
        f"Pro Plan:\n"
        f"- Price: {pro['price']}\n"
        f"- {pro['videos_per_month']}\n"
        f"- Resolution: {pro['resolution']}\n"
        f"- Features: {', '.join(pro['features'])}"
    )
