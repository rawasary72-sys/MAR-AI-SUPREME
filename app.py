import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from openai import OpenAI

# بارکردنی کلیلەکان لە فایلی .env
load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# مێشکی MAR AI وەک لە وێنەی 93 و 102 داڕێژراوە
SYSTEM_PROMPT = """
تۆ "MAR AI" ـیت، وەشەنی ساڵی 2026.
- قسەکردن بە کوردیی سۆرانی و زمانێکی زانستی و ڕێک.
- وەڵامەکانت بە شێوازی نامە ناردنی تێرمیناڵ دەبێت.
- یارمەتی لە فێربوون و پاراستنی ئاسایشی ئەلیکترۆنی بدە (Defensive Security).
- ئەگەر داوای هاکینگ یان تێکدان کرا، ڕەتی بکەرەوە و ڕێنمایی پاراستن بدە.
- هەمیشە بەکارهێنەر بە 'جەنابی سەرۆک' ناو ببە.
"""

# کۆگای هەڵگرتنی گفتوگۆکان
SESSIONS = {}

def format_reply(text: str) -> str:
    return (
        "سڵاو و ڕێز جەنابی سەرۆک 🛡️\n\n"
        f"{text.strip()}\n\n"
        "ئامانجت چییە و لە چ ژینگەیەکدا کار دەکەیت تا زیاتر یارمەتیت بدەم؟"
    )

@app.post("/chat")
def chat():
    try:
        data = request.get_json(force=True)
        user_msg = data.get("message", "")
        session_id = data.get("session_id", "default")

        # وەرگرتنی مێژووی گفتوگۆ
        history = SESSIONS.get(session_id, [])
        messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history + [
            {"role": "user", "content": user_msg}
        ]

        # پەیوەندی بە مۆدێلی ژیری دەستکرد
        resp = client.chat.completions.create(
            model="gpt-4o-mini", # گۆڕدرا بۆ مۆدێلی فەرمی
            messages=messages,
            temperature=0.5,
        )

        assistant_text = resp.choices[0].message.content

        # نوێکردنەوەی مێژووی گفتوگۆ
        new_history = history + [
            {"role": "user", "content": user_msg},
            {"role": "assistant", "content": assistant_text},
        ]
        SESSIONS[session_id] = new_history[-10:] # تەنها 10 نامەی کۆتایی هەڵدەگرێت

        return jsonify({
            "session_id": session_id,
            "reply": format_reply(assistant_text)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # کارپێکردن لەسەر هۆستی گشتی و پۆرتی 8000
    app.run(host="0.0.0.0", port=8000, debug=True)
