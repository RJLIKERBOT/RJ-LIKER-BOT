from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

import os

TOKEN = os.getenv("BOT_TOKEN") or "8306309242:AAEUOSxq33LRUzjdMozco18R_4ak10D502U"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔐 Login with Facebook", callback_data="login")],
        [InlineKeyboardButton("❤️ Like Exchange", callback_data="exchange")],
        [InlineKeyboardButton("📊 My Account", callback_data="account")],
        [InlineKeyboardButton("❓ Help", callback_data="help")]
    ]

    await update.message.reply_text(
        "❤️ Welcome to RJ Liker\n\n"
        "Real Facebook Like Exchange System\n\n"
        "👇 Choose an option below",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
