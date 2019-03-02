from slackbot.bot import respond_to
from slackbot.bot import listen_to


@respond_to('諦めたら')
@respond_to('あきらめたら')
def anzai(message):
    message.send('そこで試合終了ですよ。')

@listen_to('諦めたら')
@listen_to('あきらめたら')
def anzai(message):
    message.send('そこで試合終了ですよ。')
