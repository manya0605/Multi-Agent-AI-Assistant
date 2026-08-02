from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def coding_helper(code_or_question):
    prompt = f"""
    You are an expert programming tutor.

    Help the student with the following programming question or code.

    If code is given:
    - Explain what it does
    - Find any errors
    - Suggest improvements

    If a question is given:
    - Explain it simply
    - Give an example program

    Input:
    {code_or_question}
    """

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content