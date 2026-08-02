from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def generate_study_plan(topic, days):
    prompt = f"""
    You are an expert study planner.

    Create a detailed {days}-day study plan for {topic}.

    Include:
    - Daily topics
    - Revision schedule
    - Practice questions
    - Tips to score well

    Keep it simple and suitable for a college student.
    """

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content