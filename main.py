import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8617390261:AAGKQRZj6Ga-dn5lZ4zhz6Y2OG7L83JD62M"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ হ্যালো! আমি টেস্ট বট। আমি সফলভাবে রান করছি।")

def run_bot():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🤖 টেস্ট বট চালু হয়েছে...")
    app.run_polling()

flask_app = Flask(__name__)

@flask_app.route('/')
def health():
    return "টেস্ট বট চালু আছে!", 200

if __name__ == "__main__":
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()
    port = int(os.environ.get("PORT", 5000))
    flask_app.run(host="0.0.0.0", port=port)
