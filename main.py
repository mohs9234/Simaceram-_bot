import json
import logging
from telegram import Update, InputMediaPhoto
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = 'توکن_ربات_تو_اینجا_قرار_بده'

# خواندن محصولات از فایل JSON
def load_products():
    with open('products.json', 'r', encoding='utf-8') as f:
        return json.load(f)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! به ربات Simaceramic خوش آمدید.\n"
        "برای دیدن محصولات، دستور /products را بفرستید."
    )

async def products(update: Update, context: ContextTypes.DEFAULT_TYPE):
    products = load_products()
    media = []
    for p in products:
        caption = f"نام محصول: {p['name']}\nقیمت: {p['price']}\nموجودی: {p['inventory']}"
        media.append(InputMediaPhoto(p['image'], caption=caption))
    if media:
        await update.message.reply_media_group(media)
    else:
        await update.message.reply_text("فعلا محصولی موجود نیست.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('products', products))

    print("ربات در حال اجراست...")
    app.run_polling()
