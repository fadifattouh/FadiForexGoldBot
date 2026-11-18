
import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "مرحباً بك في Fadi Forex Gold Bot! 🟡\n"
        "بوت تحليل الذهب والفوركس.\n"
        "قريباً ستتوفر التحليلات والإشارات."
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("البوت يعمل بنجاح! ✅")

def main():
    if not TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN غير مضبوط")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))

    print("FadiForexGoldBot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
