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
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext,ConversationHandler, CallbackQueryHandler
import leancloud
from fire import upload_blob
from search import search, search_button, search_text, could_search
from pathlib import Path
import tempfile

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


async def upload_single_photo(photo_file, id):
    # file_unique_id = photo_file['file_unique_id']
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_dir = Path(tmp_dir)
        file_name = '{}.jpg'.format(id)
        file_path = tmp_dir / file_name
        await photo_file.download_to_drive(file_path)
        url = upload_blob(file_path, file_name)
        return url


async def upload_photo(update: Update, context: CallbackContext) -> int:
    """Stores the photo and asks for a location."""
    caption = update.message.caption or ''
    photo = update.message.photo[-1]
    photo_file = await context.bot.get_file(photo.file_id)
    url = await upload_single_photo(photo_file, photo.file_id)
    shudong = caption + '\n' + url
    write_single_shudong(shudong, [url])
    await update.message.reply_text(shudong)
    await update.message.reply_text(
        'photo uploaded'
    )
    return shudong


async def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text('Help!')


async def beiwang_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /beiwang is issued."""
    # 查看备忘信息
    # 更新备忘
    await update.message.reply_text('https://github.com/hktkdy/shudong/blob/master/备忘.md')


async def todo_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /todo is issued."""
    # 查看备忘信息
    # 更新备忘
    await update.message.reply_text('https://github.com/hktkdy/shudong/blob/master/todo.md')


async def write_shudong(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    write_single_shudong(update.message.text)
    await update.message.reply_text('content saved')


# thread logic

async def could_thread(update: Update, context: CallbackContext):
    global THREAD_ARR
    global PHOTOS 
    THREAD_ARR = []
    PHOTOS = []
    await update.message.reply_text('请开始你的表演')
    return 0


async def tell_thread(update: Update, context: CallbackContext):
    if update.message.text:
        THREAD_ARR.append(update.message.text)
    if update.message.photo:
        photo_file = update.message.photo[-1].get_file()
        url = upload_single_photo(photo_file)
        PHOTOS.append(url)
    await update.message.reply_text('请继续你的表演')
    return 0


async def thread_create(update: Update, context: CallbackContext):
    print('create')
    global THREAD_ARR 
    global PHOTOS
    shudong = '\n'.join(THREAD_ARR) + '\n' + '\n'.join(PHOTOS)
    write_single_shudong(shudong, PHOTOS)
    await update.message.reply_text('preview shudong:'+ shudong)
    THREAD_ARR= []
    PHOTOS = []
    return ConversationHandler.END


async def cancel(update: Update, context: CallbackContext) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text(
        'Bye! I hope we can talk again some day.', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


async def error_handle(update: Update, context: CallbackContext) -> None:
    if update:
        await context.bot.send_message(update.effective_chat.id, "Some error in error handler")
    else:
        logger.info("user got error")
        exit(1)
        

def main(token) -> None:
    """Start the bot."""
    updater = (
       ApplicationBuilder()
        .token(token)
        .concurrent_updates(True)
        .build()
    )

    dispatcher = updater

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    # 备忘信息查看
    dispatcher.add_handler(CommandHandler("beiwang", beiwang_command))
    dispatcher.add_handler(CommandHandler("todo", todo_command))


    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('search', could_search)],
        states={
            0: [MessageHandler(filters.TEXT, search_text)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    dispatcher.add_handler(conv_handler)    

    thread_handler = ConversationHandler(
        entry_points=[CommandHandler('thread', could_thread)],
        states={
            0: [
                MessageHandler((filters.TEXT | filters.PHOTO) & ~filters.COMMAND, tell_thread), 
                CommandHandler('enter', thread_create),
                CommandHandler('cancel', cancel)
            ],
        },
        fallbacks=[CommandHandler('enter', thread_create)],
    )
    dispatcher.add_handler(thread_handler)    

    # on non command i.e message - write_shudong the message on Telegram
    dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, write_shudong))
    dispatcher.add_handler(MessageHandler(filters.PHOTO & ~filters.COMMAND, upload_photo))
    dispatcher.add_handler(CallbackQueryHandler(search_button))
    dispatcher.add_error_handler(error_handle)
    # Start the Bot
    updater.run_polling()


def init():
    with open('./token.txt', 'r') as fp:
        token = fp.read().rstrip("\n")
        main(token)

if __name__ == '__main__':
    init()
