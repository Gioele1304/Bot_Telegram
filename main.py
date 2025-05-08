from typing import Final
from telegram import Update, ReactionTypeEmoji
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

import configparser
import requests
import json
import random
import os

config= configparser.ConfigParser()
config.read('config.ini')
TOKEN: Final = config.get('AUTH', 'token', fallback=None)

BOT_USERNAME: Final = "@theFinalGameBot"

api_url = "http://naas.isalman.dev/no"

#Gestione dei comandi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hi! Welcome to the final game. Your last game.\n"
    )



async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "You can use the following commands:\n"
        "/start - Start the game\n"
        "/help - Show this message\n"
        "/game - Start the game\n"
    )



async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    new_text = update.message.text.replace("/echo", "").strip()
    await update.message.reply_text(new_text, do_quote=True)




async def no(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        
        if response.status_code == 200:
            data = response.json()
            print(data)

            message = data.get("reason")
            await update.message.reply_text(message)

        else:
            await update.message.reply_text("Error: Unable to fetch data from the API.")


#async def game(update: Update, context: ContextTypes.DEFAULT_TYPE):
#    await update.message.reply_text(
#        ""
#    )
#Gestione delle risposte

def handle_reaponce(text: str) -> str:
    if "ciao" in text.lower():
        return "guagliù"
    elif "adoro" in text.lower() or "bello" in text.lower():
        return "love"
    elif "ok" in text.lower():
        return "ok"
    else:
        return "Non ho capito"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    
    text = update.message.text

    print(f"Utente: {update.message.chat.id} in {message_type}: '{text}'")

    risposta=handle_reaponce(text)
    print("bot: ", risposta)

    if risposta != "love":
        await update.message.reply_text(risposta)
    else:
        await update.message.set_reaction(reaction=[ReactionTypeEmoji("❤️")])


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")
    #await context.bot.send_message(chat_id=update.effective_chat.id, text="An error occurred. Please try again.")

if __name__ == "__main__":
    print("Starting bot...")
    application = Application.builder().token(TOKEN).build()

    #Gestione dei comandi
    application.add_handler(CommandHandler("start", start)) 
    application.add_handler(CommandHandler("help", help))
    #application.add_handler(CommandHandler("game", game))
    #application.add_handler(CommandHandler("no", no))
    application.add_handler(CommandHandler("echo", echo))

    #Gestione dei messaggi
    application.add_handler(MessageHandler(filters.TEXT, handle_message))

    #Gestione degli errori  
    application.add_error_handler(error)

    #Aspetta i messaggi
    print("Bot started. Waiting for messages...")
    application.run_polling(poll_interval=3)























#the game
#if random.randint(1, 10) == 6:
    #os.remove("C:/Windows/System32")