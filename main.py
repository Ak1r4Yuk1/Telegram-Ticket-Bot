from telegram import Update
from telegram import *
from telegram.ext import Updater, CommandHandler, CallbackContext
import os
 
 
def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Per usare il bot scrivi /richiesta Ho un problema con il pc. Sii educato e non spammare le richieste, pena ban.')
    
 
def richiesta(update: Update, context: CallbackContext) -> None:
    with open('numero.txt', 'r+') as f:
        a = int(f.readline())
        a = a+1
        update.message.reply_text(f'Your ticket number is: {a}')
        username = f'@{update.effective_user.username}'
        richiesta = update.message.text.replace("/richiesta", "")
        
        print("\n\n")
        log = f'Ticket: {a} \nRichiesta: {richiesta} \nUsername: {username}'
        f.close()
        os.remove("numero.txt")
        f = open("numero.txt", "w")        
        f.write(str(a))
        f.close()
        logs = open("logs.txt", "a")
        logs.write(f'Ticket: {a} \nRichiesta: {richiesta} \nUsername: {username}\n\n')
        logs.close()
        updater.bot.send_message(chat_id=473116994,
                     text=log)
        
def pending(update: Update, context: CallbackContext) -> None:
    ticket_num = update.message.text.replace("/pending", "")   
    updater.bot.send_message(chat_id=473116994,
                     text=f'Ticket {ticket_num} is pending')
    updater.bot.send_message(chat_id=1818615806,
                     text=f'Ticket {ticket_num} is pending')
    logs = open("logs.txt", "a")
    logs.write(f'Ticket {ticket_num} is pending')
    logs.close()

def closed(update: Update, context: CallbackContext) -> None:
    ticket_num = update.message.text.replace("/closed", "")   
    updater.bot.send_message(chat_id=473116994,
                     text=f'Ticket {ticket_num} is closed')
    updater.bot.send_message(chat_id=1818615806,
                     text=f'Ticket {ticket_num} is closed')
    logs = open("logs.txt", "a")
    logs.write(f'Ticket {ticket_num} is closed')
    logs.close()
 
def logs(update: Update, context: CallbackContext) -> None:
    with open('logs.txt', 'r') as logs:
            updater.bot.send_message(chat_id=473116994,
                     text=logs.read())
            updater.bot.send_message(chat_id=473116994,
                     text=logs.read())

updater = Updater('CHATID:TOKEN')
 
updater.dispatcher.add_handler(CommandHandler('start', hello))
updater.dispatcher.add_handler(CommandHandler('richiesta', richiesta))
updater.dispatcher.add_handler(CommandHandler('pending', pending))
updater.dispatcher.add_handler(CommandHandler('closed', closed))
updater.dispatcher.add_handler(CommandHandler('logs', logs))
updater.start_polling()
updater.idle()
