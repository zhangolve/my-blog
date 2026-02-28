from datetime import datetime, timedelta, timezone
import json
import os
from dateutil import parser
try:
    from zoneinfo import ZoneInfo
except ImportError:
    from backports.zoneinfo import ZoneInfo

utc = ZoneInfo('UTC')
local = ZoneInfo('Asia/Shanghai')

twitter_utc_time_format = '%a %b %d %H:%M:%S  +0000  %Y'
show_format = '%Y-%m-%d %H:%M:%S'


def parse_date(date_str):
    print(date_str,'date_str')
    if not date_str:
        return None
    # 处理带 Z 的 UTC 时间格式
    return datetime.fromisoformat(date_str.replace('Z', '+00:00'))


# def datetime_to_twitter_utc_time(dt):
#     datetime_utc= dt.astimezone(utc)
#     datetime_utc_twitter = datetime_utc.strftime(twitter_utc_time_format)
#     return datetime_utc_twitter


# def twitter_utc_time_to_local_time(utc_time):
#     dt = datetime.strptime(utc_time, twitter_utc_time_format).replace(tzinfo=timezone.utc)
#     dt_local = dt.astimezone(local)
#     return dt_local.strftime('%Y-%m-%d %H:%M:%S')


# print(twitter_utc_time_to_local_time('Thu May 16 01:02:31 +0000 2013'))


def format_tweet_to_beijing(tweet):
    """
    将 Supabase 的 ISO 字符串转为东八区北京时间并格式化
    """
    content = tweet.get('content', '')
    raw_date = tweet.get('createdAt')
    
    display_date = "未知时间"
    
    if raw_date:
        try:
            # 1. 解析 Supabase 字符串 (处理 Z 或 +00:00)
            # 无论带不带毫秒，fromisoformat 都能处理
            dt_utc = parser.isoparse(raw_date)
        
            # 3. 转换为北京时间
            dt_beijing = dt_utc.astimezone(local)
            # 3. 格式化为人类可读样式
            display_date = dt_beijing.strftime('%Y-%m-%d %H:%M:%S')
        except Exception as e:
            print(f"时间转换失败: {e}")
            display_date = str(raw_date)

    # 4. 组装 Telegram 消息
    message = f"{content}\n{display_date}"
    return message


# 测试你的报错字符串
# print(safe_parse_to_beijing('2024-01-09T14:45:46.64+00:00'))