import winsound
import tkinter as tk
import pyautogui

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


TOKEN = "8931478982:AAG0VxaPy1W9-ZDZb8sRlc2OFuFGr29ik8M"
OWNER_ID = 5411414588


def allowed(update):
    return update.effective_user and update.effective_user.id == OWNER_ID


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not allowed(update):
        return

    await update.message.reply_text(
        "Пранк-ПК подключён!\n\n"
        "/sound — звук\n"
        "/altf4 — Alt+F4\n"
        "/text текст — показать текст на экране\n"
        "/stop — проверить связь"
    )


async def sound(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not allowed(update):
        return

    winsound.MessageBeep()
    await update.message.reply_text("Бип!")


async def altf4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not allowed(update):
        return

    pyautogui.hotkey("alt", "f4")
    await update.message.reply_text("Alt+F4 выполнен")


async def text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not allowed(update):
        return

    message = " ".join(context.args)

    if not message:
        await update.message.reply_text(
            "Напиши текст после команды.\n"
            "Например: /text Привет!"
        )
        return

    root = tk.Tk()
    root.title("Сообщение")
    root.attributes("-topmost", True)

    label = tk.Label(
        root,
        text=message,
        font=("Arial", 20),
        padx=40,
        pady=30
    )
    label.pack()

    button = tk.Button(
        root,
        text="Закрыть",
        command=root.destroy
    )
    button.pack(pady=10)

    root.mainloop()


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not allowed(update):
        return

    await update.message.reply_text("ПК на связи")


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("sound", sound))
    app.add_handler(CommandHandler("altf4", altf4))
    app.add_handler(CommandHandler("text", text))
    app.add_handler(CommandHandler("stop", stop))

    app.run_polling()


if __name__ == "__main__":
    main()
