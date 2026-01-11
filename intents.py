def detect_intent(text: str) -> str:
    text = text.lower()
    if any(x in text for x in ['hi','hello','hey']): return 'greeting'
    if any(x in text for x in ['price','pricing','cost','plan']): return 'pricing'
    if any(x in text for x in ['sign up','try','buy','get started']): return 'high_intent'
    return 'other'
