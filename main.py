import telebot
from logic import generate_signal
import time
import threading

BOT_TOKEN = "8000946649:AAEpgwDFFNrQhUnXVBXOdVESS-Os_R
bot = telebot.TeleBot(BOT_TOKEN)

active_users = set()

def send_signals_loop(chat_id):
    while chat_id in active_users:
        signal = generate_signal()
        bot.send_message(chat_id, signal)
        time.sleep(60)

@bot.message_handler(commands=['start'])
def start_handler(message):
    chat_id = message.chat.id
    active_users.add(chat_id)
    bot.send_message(chat_id, "Bot activated! You'll now receive sniper signals 30 seconds before the candle starts.")
    threading.Thread(target=send_signals_loop, args=(chat_id,)).start()

@bot.message_handler(commands=['stop'])
def stop_handler(message):
    chat_id = message.chat.id
    if chat_id in active_users:
        active_users.remove(chat_id)
        bot.send_message(chat_id, "Bot stopped. No more signals will be sent.")

bot.polling()
