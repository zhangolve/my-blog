import json
from datetime import datetime, timedelta, timezone
from telegram import Update, ForceReply, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext,ConversationHandler, CallbackQueryHandler
from shudong_utils import twitter_utc_time_to_local_time, twitter_utc_time_format, datetime_to_twitter_utc_time
import glob
import urllib.parse
import bs4 as bs
import leancloud
import os



leancloud.init("rkX7RdhzjQ0DdnpkcffRn4TD-gzGzoHsz", "pbWq8UDhvWbRpjebqfhqj4pG")

if os.environ.get('USER') == 'zhangolive':
    Shudong = leancloud.Object.extend('shudong_test')
else:
    Shudong = leancloud.Object.extend('shudong')



SEARCH_REPLY_PAGE = 0
TOTAL_SEARCH_REPLY = ''

GITHUB_REPO_PREVIEW = 'github.com/zhangolve/my-blog/blob/master/'

def search_in_shudong(text):
    result = []
    with open('./data.json') as fp:
        data = json.load(fp)
        if data:
            for shudong in data:
                full_text = shudong['tweet']['full_text']
                lower_text = text.lower()
                lower_full_text = full_text.lower()
                if lower_text in lower_full_text:
                    result.append(shudong['tweet'])
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
                lower_text = text.lower()
                lower_full_text = full_text.lower()
                if text in lower_full_text:
                    created_at = tweet['tweet']['created_at']
                    createdAt = twitter_utc_time_to_local_time(created_at)
                    tweet['tweet']['createdAt'] = createdAt
                    result.append(tweet['tweet'])
    return result


def search_in_markdown(text):
    result = []
    md_files = []
    for file in glob.glob("../**/*.md"):
        md_files.append(file)
    for file in md_files:
        with open(file, 'r') as fp:
            fp_str = fp.read()
            if text in fp_str.lower():
                index = fp_str.find(text)
                abbr = fp_str[index-100:index+100]
                result.append(abbr + '\n'+ file.replace('../',GITHUB_REPO_PREVIEW))
    return result


def search_in_text(text):
    result = []
    text_files = []
    for file in glob.glob("../*.txt"):
        text_files.append(file)
    print(text_files)
    for file in text_files:
        with open(file, 'r') as fp:
            fp_str = fp.read()
            if text in fp_str.lower():
                index = fp_str.find(text)
                abbr = fp_str[index-100:index+100]
                result.append(abbr + '\n'+ urllib.parse.quote(file.replace('../',GITHUB_REPO_PREVIEW)))
    return result



def search_weibo_contents(text):
    contents = []
    for path in glob.glob("../weibo-backup/weibo/*.html"):
        with open(path, 'r') as f:
            content = f.read()
            if text not in content.lower():
                continue
            soup = bs.BeautifulSoup(content, 'html.parser')
            single_weibo_list = soup.findAll('div', {'class': 'WB_detail'})
            for single_weibo in single_weibo_list: 
                single_content = single_weibo.find(attrs={'node-type': 'feed_list_content'})
                if single_content and text in str(single_content).lower():
                    contents.append(single_weibo.get_text(' ', strip=True)) 
    return contents



Shudong = leancloud.Object.extend('shudong')


def search_ocr(str):
    query = Shudong.query
    query.contains('new_ocr', str)
    results = query.find()
    ocr_results = []
    for r in results:
        r_dict = {}
        r_dict['full_text'] = r.get('content')
        createdAt = r.get('createdAt')
        createdAt_twitter_format = datetime_to_twitter_utc_time(createdAt)
        r_dict['created_at'] = createdAt_twitter_format
        ocr_results.append(r_dict)
    return ocr_results


def search(text):
    result = []
    result.extend(search_in_tweet(text))
    result.extend(search_in_shudong(text))
    result.extend(search_ocr(text))
    return sorted(result, key=lambda shudong: datetime.strptime(shudong['created_at'], twitter_utc_time_format))


def search_blog(text):
    result = []
    result.extend(search_in_markdown(text))
    result.extend(search_in_text(text))
    return result


def could_search(update: Update, context: CallbackContext):
    update.message.reply_text('清输入搜索内容')
    return 0


def search_text(update: Update, context: CallbackContext):
    tweet_list = search(update.message.text.lower())
    count = len(tweet_list)
    reply_content = ''
    reply_markup = None
    if tweet_list:
        for tweet in tweet_list:
            reply_content = reply_content + f'{tweet["full_text"]}\n' + f'{tweet["createdAt"]}\n'
    blog_list = search_blog(update.message.text)

    weibo_list = search_weibo_contents(update.message.text)
    count += len(blog_list)
    count += len(weibo_list)

    if blog_list:
        for blog in blog_list:
            reply_content = reply_content + f'{blog}\n'
    if weibo_list:
        for weibo in weibo_list:
            reply_content = reply_content + f'{weibo}\n'
    if not reply_content:
        reply_content = '没有找到相关内容'
    else:
        reply_content = '共计找到' + str(count) + '条搜索结果\n' + reply_content 
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
    InlineKeyboardButtons = []
    if SEARCH_REPLY_PAGE > 0: 
        InlineKeyboardButtons.append(
            InlineKeyboardButton("上一页", callback_data="-1")
        )
    if NEXT_TWO_PAGE_EXIST:
        InlineKeyboardButtons.append(
            InlineKeyboardButton("下一页", callback_data="1")
        )
    keyboard = [InlineKeyboardButtons]
    reply_markup = InlineKeyboardMarkup(keyboard)
    print(SEARCH_REPLY_PAGE , len(TOTAL_SEARCH_REPLY))
    query.edit_message_text(TOTAL_SEARCH_REPLY[SEARCH_REPLY_PAGE*4096:(SEARCH_REPLY_PAGE+1)*4096], reply_markup=reply_markup)

