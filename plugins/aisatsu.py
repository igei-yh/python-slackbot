from slackbot.bot import respond_to
from slackbot.bot import listen_to
import random


morning_messages = [
    'おはようございます。:coffee:',
    'おはよう！:sunny:',
    'GoodMorning!! :coffee:',
    '今日も一日頑張りましょう！！:fire:'
]

lanch_messages = [
    'お腹すいた。 :hushed:',
    "i'm hungry. :meat_on_bone:",
    '腹減った〜。。 :tired_face:'
]

goodbye_messages = [
    'お疲れ様です。:bow:',
    'また明日！ :sunglasses:',
    'see you again :wave:'
]


@respond_to('おはよ')
def morning(message):
    message.reply(random.choice(morning_messages))

@listen_to('おはよ')
def greeting(message):
    message.reply(random.choice(morning_messages))

@respond_to('お昼')
def lanch(message):
    message.reply(random.choice(lanch_messages))

@respond_to('おつかれ')
@respond_to('お疲れ')
def goodby(message):
    message.reply(random.choice(goodbye_messages))
