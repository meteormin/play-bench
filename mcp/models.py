from openai import OpenAI
from google import genai

promptLangs = {
    "ko": "답변은 반드시 한국어로 작성해 주세요.",
    "en": "Please answer in English.",
    "ja": "日本語で答えてください。",
}

def req_tranlate(prompt: str, lang: str) -> str:
    return f"{prompt}\n\n{promptLangs.get(lang, '')}"
    

def ask_to_openai(api_key: str, prompt: str, lang: str = "en"):
    # 🔹 OpenAI API 키 환경변수 필요 (OPENAI_API_KEY)
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",  # 혹은 gpt-4o, gpt-4.1-mini 등
        messages=[
            {
                "role": "system",
                "content": "You are an expert in algorithms, programming languages, and performance analysis.",
            },
            {"role": "user", "content": req_tranlate(prompt,lang)},
        ],
        max_tokens=1000,
    )
    return completion.choices[0].message.content


def ask_to_gemini(api_key: str, prompt: str, lang: str = "en"):
    client = genai.Client(api_key=api_key)

    # Gemini는 messages 형식 대신 직접 prompt 전달
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=req_tranlate(prompt,lang),
    )
    return response.text
