from slackbot.bot import respond_to


@respond_to('ありがとう')
@respond_to('thank')
def thanks_react(message):
    message.react('+1')
