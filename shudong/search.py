import json


def search_in_shudong(text):
    result = []
    with open('../shudong_data/leancloud/data.json') as fp:
        data = json.load(fp)
        if data:
            for shudong in data:
                full_text = shudong['tweet']['full_text']
                if text in full_text:
                    result.append(shudong)
    return result


def search_in_tweet(text):
    result = []
    with open('../shudong_data/leancloud/tweet.js') as fp:
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

