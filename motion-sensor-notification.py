import os
import json
from datetime import datetime
from urllib.request import urlopen
from bot_settings import *

import telegram

# Temporal filename
FILENAME = "current.jpeg"

# Get current date and time
now = datetime.now()
date_time = now.strftime("%d/%m/%Y, %H:%M:%S")

caption = f'🚨 *MOTION DETECTED* 🚨\n {date_time}'

# Start bot connection
bot = telegram.Bot(token=TELEGRAM_TOKEN)

# Get current camera image
web_img = urlopen('{MOTIONEYEOS_URL}/picture/1/current/?_username={MOTIONEYEOS_USER}&_signature={MOTIONEYEOS_API_KEY}')

# Download the image
output = open(FILENAME,"wb")
output.write(web_img.read())
output.close()

# Open image
img = open(FILENAME, 'rb')

# Send message to channel
bot.send_photo(chat_id=TELEGRAM_CHAT_ID, caption=caption, photo=img, parse_mode=telegram.ParseMode.MARKDOWN)

# Remove file
os.remove(FILENAME)
