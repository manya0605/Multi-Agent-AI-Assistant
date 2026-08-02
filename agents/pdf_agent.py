from pypdf import PdfReader
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def pdf_summary(uploaded_file, option):

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    prompt = f"""
    You are an AI study assistant.

    Read the following PDF.

    User selected: {option}

    If the option is:

    - Generate Summary → Give a concise summary.
    - Generate Notes → Create clean study notes with headings.
    - Generate Quiz → Create 10 MCQs with answers.
    - Explain Difficult Concepts → Explain difficult topics in simple language.

    PDF Content:

    {text}
    """

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content