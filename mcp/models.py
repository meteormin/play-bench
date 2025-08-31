from openai import OpenAI
from google import genai


def ask_to_openai(api_key: str, prompt: str):
    # 🔹 OpenAI API 키 환경변수 필요 (OPENAI_API_KEY)
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",  # 혹은 gpt-4o, gpt-4.1-mini 등
        messages=[
            {
                "role": "system",
                "content": "You are an expert in algorithms, programming languages, and performance analysis.",
            },
            {"role": "user", "content": prompt},
        ],
        max_tokens=1000,
    )
    return completion.choices[0].message.content


def ask_to_gemini(api_key: str, prompt: str):
    client = genai.Client(api_key=api_key)

    # Gemini는 messages 형식 대신 직접 prompt 전달
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=prompt,
    )
    return response.text
