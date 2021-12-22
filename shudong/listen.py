#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
RUN pip install --no-cache-dir -r requirements.txt

Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext,ConversationHandler
import leancloud
from fire import upload_blob
from search import search
leancloud.init("rkX7RdhzjQ0DdnpkcffRn4TD-gzGzoHsz", "pbWq8UDhvWbRpjebqfhqj4pG")

Shudong = leancloud.Object.extend('shudong')


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

THREAD_ARR = []

# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )



def write_single_shudong(text):
    shudong = Shudong()
    shudong.set('content', text)
    shudong.save()


def upload_single_photo(photo_file):
    file_unique_id = photo_file['file_unique_id']
    file_name = '{}.jpg'.format(file_unique_id)
    photo_file.download(file_name)
    url = upload_blob('./{}'.format(file_name), file_name)
    return url


def upload_photo(update: Update, context: CallbackContext) -> int:
    """Stores the photo and asks for a location."""
    caption = update.message.caption or ''
    photo_file = update.message.photo[-1].get_file()
    url = upload_single_photo(photo_file)
    shudong = caption + '\n' + url
    write_single_shudong(shudong)
    update.message.reply_text(shudong)
    update.message.reply_text(
        'photo uploaded'
    )
    return shudong


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')



def write_shudong(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    write_single_shudong(update.message.text)
    update.message.reply_text('content saved')


def could_search(update: Update, context: CallbackContext):
    update.message.reply_text('清输入搜索内容')
    return 0


def search_text(update: Update, context: CallbackContext):
    tweet_list = search(update.message.text)
    reply_content = ''
    if tweet_list:
        for tweet in tweet_list:
            reply_content = reply_content + f'{tweet["tweet"]["full_text"]}\n' + f'{tweet["tweet"]["created_at"]}\n'
    else:
        reply_content = '没有找到相关内容'
    update.message.reply_text(reply_content)
    return ConversationHandler.END


# thread logic

def could_thread(update: Update, context: CallbackContext):
    global THREAD_ARR 
    THREAD_ARR = []
    update.message.reply_text('请开始你的表演')
    return 0


def tell_thread(update: Update, context: CallbackContext):
    if update.message.text:
        THREAD_ARR.append(update.message.text)
    if update.message.photo:
        photo_file = update.message.photo[-1].get_file()
        url = upload_single_photo(photo_file)
        THREAD_ARR.append(url)
    update.message.reply_text('请继续你的表演')
    return 0


def thread_create(update: Update, context: CallbackContext):
    print('create')
    global THREAD_ARR 
    shudong = '\n'.join(THREAD_ARR)
    write_single_shudong(shudong)
    update.message.reply_text('preview shudong:'+ shudong)
    THREAD_ARR= []
    return ConversationHandler.END


def cancel(update: Update, context: CallbackContext) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Bye! I hope we can talk again some day.', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("5065608320:AAHV4EkYAW9mFRK6QwWtAonI8nZ83LVeQSI")
    # dev bot
    # updater = Updater("5064508364:AAEfTF9IlNUwIrEaL3VPWn0WsQsgb4bhzNA")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

        
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('search', could_search)],
        states={
            0: [MessageHandler(Filters.text, search_text)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    dispatcher.add_handler(conv_handler)    

    thread_handler = ConversationHandler(
        entry_points=[CommandHandler('thread', could_thread)],
        states={
            0: [
                MessageHandler((Filters.text | Filters.photo) & ~Filters.command, tell_thread), 
                CommandHandler('enter', thread_create)
            ],
        },
        fallbacks=[CommandHandler('enter', thread_create)],
    )
    dispatcher.add_handler(thread_handler)    

    # on non command i.e message - write_shudong the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, write_shudong))
    dispatcher.add_handler(MessageHandler(Filters.photo & ~Filters.command, upload_photo))
    
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()