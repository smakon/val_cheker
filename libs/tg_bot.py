import telebot

TOKEN = "your_token"
bot = telebot.TeleBot(TOKEN)
def send_notify(message):
    bot.send_message(your_chat_id, message)
    
