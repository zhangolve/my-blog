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
import os

from telegram import Update, ForceReply, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext,ConversationHandler, CallbackQueryHandler
import leancloud
from fire import upload_blob
from search import search, search_button, search_text, could_search
leancloud.init("rkX7RdhzjQ0DdnpkcffRn4TD-gzGzoHsz", "pbWq8UDhvWbRpjebqfhqj4pG")

if os.environ.get('USER') == 'zhangolive':
    Shudong = leancloud.Object.extend('shudong_test')
else:
    Shudong = leancloud.Object.extend('shudong')


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

THREAD_ARR = []
PHOTOS = []

# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )



def write_single_shudong(text, photos=None):
    shudong = Shudong()
    shudong.set('content', text)
    if photos:
        shudong.set('photos', photos)
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
    write_single_shudong(shudong, [url])
    update.message.reply_text(shudong)
    update.message.reply_text(
        'photo uploaded'
    )
    return shudong


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def beiwang_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /beiwang is issued."""
    # 查看备忘信息
    # 更新备忘
    update.message.reply_text('https://github.com/hktkdy/shudong/blob/master/备忘.md')


def write_shudong(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    write_single_shudong(update.message.text)
    update.message.reply_text('content saved')




# thread logic

def could_thread(update: Update, context: CallbackContext):
    global THREAD_ARR
    global PHOTOS 
    THREAD_ARR = []
    PHOTOS = []
    update.message.reply_text('请开始你的表演')
    return 0


def tell_thread(update: Update, context: CallbackContext):
    if update.message.text:
        THREAD_ARR.append(update.message.text)
    if update.message.photo:
        photo_file = update.message.photo[-1].get_file()
        url = upload_single_photo(photo_file)
        PHOTOS.append(url)
    update.message.reply_text('请继续你的表演')
    return 0


def thread_create(update: Update, context: CallbackContext):
    print('create')
    global THREAD_ARR 
    global PHOTOS
    shudong = '\n'.join(THREAD_ARR) + '\n' + '\n'.join(PHOTOS)
    write_single_shudong(shudong, PHOTOS)
    update.message.reply_text('preview shudong:'+ shudong)
    THREAD_ARR= []
    PHOTOS = []
    return ConversationHandler.END


def cancel(update: Update, context: CallbackContext) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Bye! I hope we can talk again some day.', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def main(token) -> None:
    """Start the bot."""
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    # 备忘信息查看
    dispatcher.add_handler(CommandHandler("beiwang", beiwang_command))


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
                CommandHandler('enter', thread_create),
                CommandHandler('cancel', cancel)
            ],
        },
        fallbacks=[CommandHandler('enter', thread_create)],
    )
    dispatcher.add_handler(thread_handler)    

    # on non command i.e message - write_shudong the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, write_shudong))
    dispatcher.add_handler(MessageHandler(Filters.photo & ~Filters.command, upload_photo))
    dispatcher.add_handler(CallbackQueryHandler(search_button))
    
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()



def init():
    with open('./token.txt', 'r') as fp:
        token = fp.read().rstrip("\n")
        main(token)

if __name__ == '__main__':
    init()
