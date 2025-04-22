import telebot
from logic import generate_signal
import time
import threading

BOT_TOKEN = "8000946649:AAGBUpsVqhRk9e896IYG2_QfxU9lYD-xz7Q"
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
    bot.send_message(chat_id, "Bot activated! You'll now receive live signals.")
    threading.Thread(target=send_signals_loop, args=(chat_id,)).start()

@bot.message_handler(commands=['stop'])
def stop_handler(message):
    chat_id = message.chat.id
    if chat_id in active_users:
        active_users.remove(chat_id)
        bot.send_message(chat_id, "Bot stopped. You won't receive further signals.")

bot.polling()
