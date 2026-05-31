from openai import OpenAI
from api import key

def ai():
    client = OpenAI(
        api_key=key,
        base_url="https://api.groq.com/openai/v1",
    )

    response = client.responses.create(
        input="Tu es une IA qui doit donner 10 pseudos gaming stylés sans rien dire d'autre juste des pseudo",
        model="openai/gpt-oss-20b",
    )

    return response.output_text
    