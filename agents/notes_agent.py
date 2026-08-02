from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def generate_notes(text):
    prompt = f"""
    Summarize the following text into easy-to-read study notes.

    Include:
    - Important points
    - Key concepts
    - Definitions
    - Short explanations
    - Revision tips
    - Exam strategies
    - A short revision plan if appropriate

    IMPORTANT:
    - Do NOT generate Mermaid diagrams.
    - Do NOT use Mermaid syntax.
    - Do NOT use HTML tags such as <br>.
    - Use normal headings and bullet points only.
    - Keep the notes clear and easy for students to study.

    Text:
    {text}
    """

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content