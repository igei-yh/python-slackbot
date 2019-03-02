from slackbot.bot import listen_to
import random


cheerup_messages = [
    'ファイト！ :triumph:',
    'fight !! :fist:',
    '頑張って :two_hearts:'
]


@listen_to('疲れた')
@listen_to('つかれた')
def cheerup(message):
    message.reply(random.choice(cheerup_messages))
