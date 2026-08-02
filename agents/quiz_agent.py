from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def generate_quiz(topic):
    prompt = f"""
    Create a quiz on the topic: {topic}

    Include:
    - 10 multiple-choice questions
    - Four options (A, B, C, D)
    - Correct answer after each question

    Make it suitable for an engineering student.
    """

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content