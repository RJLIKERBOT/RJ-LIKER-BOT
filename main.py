from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8306309242:AAEUOSxq33LRUzjdMozco18R_4ak10D502U"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔐 Login with Facebook", callback_data="login")],
        [InlineKeyboardButton("❤️ Like Exchange", callback_data="exchange")],
        [InlineKeyboardButton("📊 My Account", callback_data="account")],
        [InlineKeyboardButton("❓ Help", callback_data="help")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "❤️ Welcome to RJ Liker\n\n"
        "Real Facebook Like Exchange System\n\n"
        "👇 Choose an option below",
        reply_markup=reply_markup
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    app.run_polling()
