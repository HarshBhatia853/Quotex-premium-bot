import telebot
from logic import generate_signal
import time
import threading

BOT_TOKEN = "8000946649:AAEpgwDFFNrQhUnXVBXOdVESS-Os_RKT87g"
bot = telebot.TeleBot(BOT_TOKEN)

active_users = {}

def send_signals_loop(chat_id):
    while active_users.get(chat_id, False):
        signal = generate_signal()
        bot.send_message(chat_id, signal)
        time.sleep(60)

@bot.message_handler(commands=['start'])
def start_handler(message):
    chat_id = message.chat.id
    if not active_users.get(chat_id):
        active_users[chat_id] = True
        bot.send_message(chat_id, "Bot activated! You'll now receive sniper signals 30 seconds before the candle starts.")
        thread = threading.Thread(target=send_signals_loop, args=(chat_id,))
        thread.daemon = True
        thread.start()
    else:
        bot.send_message(chat_id, "Bot is already running!")

@bot.message_handler(commands=['stop'])
def stop_handler(message):
    chat_id = message.chat.id
    active_users[chat_id] = False
    bot.send_message(chat_id, "Bot stopped. No more signals will be sent.")

bot.infinity_polling()
