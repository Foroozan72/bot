# import telebot

# bot = telebot.TeleBot("6804582307:AAFiTwiRpcm6fxubfTUWi3SsNJgIY-t2PT8")

# @bot.message_handler(cammands=['start'])
# def send_welcom(message):
#     bot.send_message(message.chat.id , "Hi")

# bot.infinity_polling()


# import requests

# response = requests.get('https://api.telegram.org/bot6804582307:AAFiTwiRpcm6fxubfTUWi3SsNJgIY-t2PT8/getMe')
# print(response.json())


import telebot
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Correct and valid bot token
bot = telebot.TeleBot("6804582307:AAFiTwiRpcm6fxubfTUWi3SsNJgIY-t2PT8")

first_button = telebot.types.InlineKeyboardButton("First" , url="https://t.me/afarinesh")
second_button = telebot.types.InlineKeyboardButton("Second" , url="https://t.me/ibtil")
markup = telebot.types.InlineKeyboardMarkup(row_width=1)
markup.add(first_button, second_button)

# Correcting the typo in the command decorator and function name
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hi" , reply_markup=markup)

@bot.message_handler(commands=['help'] )
def help_me(message):
    bot.reply_to(message , "what can i do? ")

# Start the bot
bot.infinity_polling()
