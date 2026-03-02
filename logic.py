from telegram import Update
from telegram.ext import ContextTypes
from database import get_colleges

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome! 🎓\n\nType /colleges to see top colleges."
    )

# /colleges command
async def colleges(update: Update, context: ContextTypes.DEFAULT_TYPE):
    college_list = get_colleges()

    if not college_list:
        await update.message.reply_text("No colleges found in database.")
        return

    for c in college_list:
        try:
            with open(c["image_url"], "rb") as photo:
                await update.message.reply_photo(
                    photo=photo,
                    caption=f"🏫 {c['name']}\n\n📍 Location: {c['location']}\n\n📝 {c['description']}"
                )
        except Exception as e:
            await update.message.reply_text(
                f"Error showing {c['name']}: {str(e)}"
            )