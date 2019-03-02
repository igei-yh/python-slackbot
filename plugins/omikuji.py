from slackbot.bot import respond_to
import random


omikuji_messages = [
    '大吉', '吉', '中吉', '小吉', '末吉', '凶', '大吉'
]


@respond_to('おみくじ')
def omikuji(message):
    message.reply(random.choice(omikuji_messages))
