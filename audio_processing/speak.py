import re
from utils import get_ollama_response

def strip_response(text):
    pattern = r'"(.*?)"'
    matches = re.findall(pattern, text)

    return matches[0]


def respond(input):
    prompt = f"""How would you respond to this sentence in one line?  Only include the response.
    If it sounds like gibberish, respond in kind (but don't say gibberish):  {input}"""
    return strip_response(get_ollama_response(prompt=prompt))
