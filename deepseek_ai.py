import requests

# Replace with your actual OpenRouter API key (keep it secret)
API_KEY = (
    "your-deepseekR1apikey"
)

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",  # Optional: can be your project name
    "X-Title": "JARVIS-Bhai"  # Optional: just a title
}

def ask_deepseek(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"

    payload = {
        "model": "deepseek-chat",  # or "deepseek-coder" for code stuff
        "messages": [
            {"role": "system", "content": "You are JARVIS Bhai, a helpful Indian assistant who speaks like a friend."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        res = requests.post(url, headers=headers, json=payload)
        res.raise_for_status()
        result = res.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        print("Error:", e)
        return "Sorry bhai, DeepSeek se jawab nahi aaya."
