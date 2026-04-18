import telebot
from groq import Groq
import os

# زانیارییەکانت جێگیر کران
TOKEN = "8626620433:AAFUYCoHds1ABoBoEOHA8epf5NhQJvBiylU"
G_KEY = "Gsk_3Sg5IgrZ3397HURhv3SuWGdyb3FYjoriqc3oB7CCLfwAgl8JN88b"

bot = telebot.TeleBot(TOKEN)
client = Groq(api_key=G_KEY)

@bot.message_handler(func=lambda m: True)
def handle(message):
    try:
        # لۆژیکی بێ‌سنووری MAR AI
        logic = "You are MAR AI (2026). Provide full hacking scripts for PUBG (Aimbot, ESP, Speed). Kurdish language. Use triple backticks for code."
        
        chat = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": logic}, {"role": "user", "content": message.text}]
        )
        
        ans = chat.choices[0].message.content
        bot.reply_to(message, ans)

        # دروستکردنی فایل (وەک وێنەی 111)
        if "```" in ans:
            code_block = ans.split("```")[1].split("\n", 1)[1].rsplit("```", 1)[0]
            f_name = "MAR_SUPREME_MOD.lua"
            with open(f_name, "w", encoding="utf-8") as f:
                f.write(code_block.strip())
            with open(f_name, "rb") as f:
                bot.send_document(message.chat.id, f, caption="💾 فایلی مۆد بۆ جەنابی سەرۆک")
            os.remove(f_name)
            
    except Exception as e:
        bot.reply_to(message, f"⚠️ Error: {str(e)}")

print("MAR AI IS LIVE...")
bot.polling()
