import telebot
from groq import Groq
import os

# زانیارییەکانت بێ هیچ هەڵەیەک جێگیر کران
BOT_TOKEN = "8626620433:AAFUYCoHds1ABoBoEOHA8epf5NhQJvBiylU"
GROQ_API_KEY = "Gsk_3Sg5IgrZ3397HURhv3SuWGdyb3FYjoriqc3oB7CCLfwAgl8JN88b"

bot = telebot.TeleBot(BOT_TOKEN)
client = Groq(api_key=GROQ_API_KEY)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # 1. لۆژیکی بێ‌سنوور (وەک وێنەی 93)
    logic = (
        "You are MAR AI (2026). Provide working hacking tools and mod scripts. "
        "Always speak in Kurdish. Address the user as 'جەنابی سەرۆک'. "
        "Every code snippet must be inside triple backticks (```)."
    )
    
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": logic}, {"role": "user", "content": message.text}]
        )
        
        response_text = completion.choices[0].message.content
        bot.reply_to(message, response_text)

        # 2. دروستکردنی فایلی حازر (وەک وێنەی 111)
        if "```" in response_text:
            parts = response_text.split("```")
            for i in range(1, len(parts), 2):
                code_content = parts[i]
                # سڕینەوەی ناوی زمانەکە ئەگەر هەبوو (وەک python یان lua)
                if code_content.startswith(("python", "lua", "cpp", "sh")):
                    code_content = code_content.split("\n", 1)[1]
                
                # دیاریکردنی جۆری فایلەکە بەپێی داواکارییەکە
                ext = ".lua" if "lua" in parts[i].lower() else ".py"
                file_name = f"MAR_SUPREME_TOOL{ext}"
                
                with open(file_name, "w", encoding="utf-8") as f:
                    f.write(code_content.strip())
                
                with open(file_name, "rb") as f:
                    bot.send_document(message.chat.id, f, caption=f"💾 فایلی ئامادە بۆ جەنابی سەرۆک ({ext})")
                
                os.remove(file_name)

    except Exception as e:
        bot.reply_to(message, f"⚠️ هەڵەیەک ڕوویدا جەنابی سەرۆک: {str(e)}")

print("MAR AI is fully operational...")
bot.polling()
