import telebot
from telebot import types
import logging
import sys
import time
from news_maker import get_last_news

source = "https://vc.ru"
API_TOKEN = 'TOKEN'

bot = telebot.TeleBot(API_TOKEN)
telebot.logger.setLevel(logging.DEBUG)

@bot.inline_handler(lambda query: True)
def news_retriver(inline_query):

    if inline_query.query == 'news':
        try:
            last_new = get_last_news(source)
            result = types.InlineQueryResultArticle('1', 'News', types.InputTextMessageContent(last_new))
            bot.answer_inline_query(inline_query.id, [result])

        except Exception as e:
            print(e)

    else:
        instruction = "Чтобы получить новость, введите имя бота @news_making_bot и слово news в placeholder"
        result = types.InlineQueryResultArticle('1', 'News', types.InputTextMessageContent(instruction))
        bot.answer_inline_query(inline_query.id, [result])


def main_loop():
    bot.infinity_polling()
    while 1:
        time.sleep(3)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print('\nExiting by user request.\n')
        sys.exit(0)
