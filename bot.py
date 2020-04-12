#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards.
"""
import logging
import os
import requests
from urllib.request import urlopen
from datetime import datetime
from settings import *

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ChatAction, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def is_admin(user):
  return user.id in get_list_of_admins()

def get_chat_id(update):
  return update.effective_chat.id

def set_typing(update, context):
  context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=ChatAction.TYPING)

def get_reply_markup():
  keyboard = [
              [InlineKeyboardButton("Get a shoot", callback_data='get_current_shoot')],
              [InlineKeyboardButton("Enable motion detection", callback_data='toggle_alarm')],
              [InlineKeyboardButton("Admin", callback_data='admin_url')],
            ]

  return InlineKeyboardMarkup(keyboard)


def start(update, context):
    user = update.message.from_user

    if is_admin(user):
      update.message.reply_text(f'Hi {user.first_name}!\nWhat do you want to do?:', reply_markup=get_reply_markup())
    else:
      update.message.reply_text('🚨 PERMISSION DENIED 🚨')


def get_current_shoot(update, context):
    filename = "current.jpeg"
    now = datetime.now()
    chat_id = get_chat_id(update)
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    caption = f'🕒 {date_time}'
    url = f'{MOTIONEYEOS_URL}/picture/1/current/?_username={MOTIONEYEOS_USER}&_signature={MOTIONEYEOS_API_KEY}'
    # Get current camera image
    web_img = urlopen(url)
    # Download the image
    output = open(filename,"wb")
    output.write(web_img.read())
    output.close()
    # Open image
    img = open(filename, 'rb')
    context.bot.send_photo(chat_id=chat_id, caption=caption, photo=img, parse_mode=ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=chat_id, text="What's next?", reply_markup=get_reply_markup())
    # Remove so it doesn't take space in the filesystem
    os.remove(filename)


def developing_functionality(update, context):
    context.bot.send_message(chat_id=get_chat_id(update), text='😞 Sorry, still developing this function.', reply_markup=get_reply_markup())


def get_admin_url(update, context):
    ip = requests.get('https://checkip.amazonaws.com').text.strip()
    context.bot.send_message(chat_id=get_chat_id(update), text=f'http://{ip}:8765', reply_markup=get_reply_markup())


def get_command(command):
    switcher = {
        'get_current_shoot': get_current_shoot,
        'toggle_alarm': developing_functionality,
        'admin_url': get_admin_url,
    }
    return switcher.get(command, error)


def button(update, context):
    query = update.callback_query.data
    command = get_command(query)
    command(update, context)


def help(update, context):
    update.message.reply_text("Use /start to test this bot.")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
