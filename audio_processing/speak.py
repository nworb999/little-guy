from utils.ollama import get_response

def respond(input):
    prompt = f"How would you respond to this sentence in one line?  If it sounds like gibberish, respond in kind.  {input}"
    return get_response(prompt=prompt)
