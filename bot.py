# bot.py
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import sys
import logging

# ------------------- Logging setup -------------------
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ------------------- BOT TOKEN -------------------
BOT_TOKEN = "8723625802:AAGUxIhgiFz4EL0ANC5QlvyYS8H0m0k_i1k"  # <-- Replace with your bot token

# Token check
if BOT_TOKEN == "YOUR_REAL_BOT_TOKEN_HERE":
    print("❌ ERROR: Please replace 'YOUR_REAL_BOT_TOKEN_HERE' with your actual bot token from @BotFather")
    sys.exit(1)

# ------------------- Top 5 Colleges Data -------------------
colleges = [
    {"name": "IIT Delhi", "image": "IIT_Delhi.jpg", "description": "Premier engineering institute in India, known for tech research.", "location": "New Delhi, India", "ranking": "1"},
    {"name": "IIT Bombay", "image": "IIT_Bombay.jpg", "description": "Top engineering college, famous for innovation and startups.", "location": "Mumbai, Maharashtra, India", "ranking": "2"},
    {"name": "IISc Bangalore", "image": "IISc_Bangalore.jpg", "description": "Leading institute for scientific research and higher education.", "location": "Bengaluru, Karnataka, India", "ranking": "3"},
    {"name": "BITS Pilani", "image": "BITS_Pilani.jpg", "description": "Known for flexible curriculum and strong alumni network.", "location": "Pilani, Rajasthan, India", "ranking": "4"},
    {"name": "NIT Trichy", "image": "NIT_Trichy.jpg", "description": "One of the top NITs in India, famous for engineering programs.", "location": "Tiruchirappalli, Tamil Nadu, India", "ranking": "5"},
]

# ------------------- Command Handlers -------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        welcome_text = (
            "👋 Hello! Welcome to the Top Colleges Bot.\n\n"
            "Use /topcolleges to see the top 5 colleges in India with images, location and ranking."
        )
        await update.message.reply_text(welcome_text)
    except Exception as e:
        logger.error(f"Error in /start: {e}")
        await update.message.reply_text("❌ Something went wrong with /start.")

async def top_colleges(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for college in colleges:
        caption = (
            f"🏫 {college['name']}\n"
            f"{college['description']}\n"
            f"📍 Location: {college['location']}\n"
            f"🏆 Ranking: #{college['ranking']}"
        )
        try:
            with open(college["image"], "rb") as photo:
                await update.message.reply_photo(photo=photo, caption=caption)
        except FileNotFoundError:
            logger.warning(f"Image not found: {college['image']}")
            await update.message.reply_text(f"❌ Image not found for {college['name']}!")
        except Exception as e:
            logger.error(f"Error sending photo for {college['name']}: {e}")
            await update.message.reply_text(f"❌ Failed to send {college['name']} info.")

# ------------------- Unknown Command / Message Handler -------------------
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_text("❌ Oops! Something went wrong or unknown command. Please use /start or /topcolleges.")
    except Exception as e:
        logger.error(f"Error in unknown handler: {e}")

# ------------------- Main Bot Setup -------------------
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("topcolleges", top_colleges))

    # Unknown command handler
    app.add_handler(MessageHandler(filters.COMMAND | filters.TEXT, unknown))

    # Global error handler
    async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
        logger.error(msg="Exception while handling an update:", exc_info=context.error)
        if hasattr(update, "message") and update.message:
            await update.message.reply_text("❌ Oops! Something went wrong. Try again later.")

    app.add_error_handler(error_handler)

    print("✅ Bot is running... Use /start or /topcolleges in Telegram")
    app.run_polling()