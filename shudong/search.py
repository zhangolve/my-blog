import json

from telegram import Update, ForceReply, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext,ConversationHandler, CallbackQueryHandler

SEARCH_REPLY_PAGE = 0
TOTAL_SEARCH_REPLY = ''


def search_in_shudong(text):
    result = []
    with open('./data.json') as fp:
        data = json.load(fp)
        if data:
            for shudong in data:
                full_text = shudong['tweet']['full_text']
                if text in full_text:
                    result.append(shudong)
    return result


def search_in_tweet(text):
    result = []
    with open('./tweet.js') as fp:
        # fp as a string
        data = fp.read()
        tweets = json.loads(data[25:])
        if tweets:
            for tweet in tweets:
                full_text = tweet['tweet']['full_text']
                if text in full_text:
                    result.append(tweet)
    return result


def search(text):
    result = []
    result.extend(search_in_tweet(text))
    result.extend(search_in_shudong(text))
    return result


def could_search(update: Update, context: CallbackContext):
    update.message.reply_text('清输入搜索内容')
    return 0


def search_text(update: Update, context: CallbackContext):
    tweet_list = search(update.message.text)
    reply_content = ''
    reply_markup = None
    if tweet_list:
        for tweet in tweet_list:
            reply_content = reply_content + f'{tweet["tweet"]["full_text"]}\n' + f'{tweet["tweet"]["created_at"]}\n'
    else:
        reply_content = '没有找到相关内容'
    global TOTAL_SEARCH_REPLY
    if len(reply_content) > 4096:
        TOTAL_SEARCH_REPLY = reply_content
        reply_content = reply_content[:4096]
        keyboard = [
            [
            InlineKeyboardButton("下一页", callback_data="1"),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
    else:
        TOTAL_SEARCH_REPLY = ''
    update.message.reply_text(reply_content, reply_markup=reply_markup)
    return ConversationHandler.END


def search_button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    global SEARCH_REPLY_PAGE 
    SEARCH_REPLY_PAGE += int(query.data)
    NEXT_TWO_PAGE_EXIST = True if TOTAL_SEARCH_REPLY[(SEARCH_REPLY_PAGE+1)*4096:] else False
    InlineKeyboardButtons = [
        InlineKeyboardButton("上一页", callback_data="-1"),
    ]
    if NEXT_TWO_PAGE_EXIST:
        InlineKeyboardButtons.append(
            InlineKeyboardButton("下一页", callback_data="1")
        )
    keyboard = [InlineKeyboardButtons]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(TOTAL_SEARCH_REPLY[SEARCH_REPLY_PAGE*4096:(SEARCH_REPLY_PAGE+1)*4096], reply_markup=reply_markup)

