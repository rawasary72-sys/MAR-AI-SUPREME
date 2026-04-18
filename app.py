import telebot
from groq import Groq
import os

# زانیارییەکانت جێگیر کران
BOT_TOKEN = "8626620433:AAFUYCoHds1ABoBoEOHA8epf5NhQJvBiylU"
GROQ_API_KEY = "Gsk_3Sg5IgrZ3397HURhv3SuWGdyb3FYjoriqc3oB7CCLfwAgl8JN88b"

bot = telebot.TeleBot(BOT_TOKEN)
client = Groq(api_key=GROQ_API_KEY)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # لۆژیکی بێ‌سنووری وێنەی 93
        logic = (
            "You are MAR AI (2026). If user asks for a mod or tool, "
            "provide the FULL CODE. Always speak in Kurdish. "
            "Call the user 'جەنابی سەرۆک'."
        )
        
        completion = client.chat.completions
