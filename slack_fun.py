"""More fun with Dean! Now on Slack!

"""
import sys
import random
import time

# 3rd party
import click
from slacker import Slacker

# local settings
from settings import SLACK_TOKEN

# use this for all calls to slack API
API = Slacker(SLACK_TOKEN)


def find_channel_id(username):
    """This finds the IM channel ID given a user name."""

    user_id = API.users.get_user_id(username)

    channel_id = None
    for user in API.im.list().body['ims']:
        if user['user'] == user_id:
            channel_id = user['id']

    return channel_id


def perform_fun(username, channel_id):
    """This is the FUNction."""
    fun_count = 0
    try:
        while True:
            fun_count += 1
            msg = 'Hi %s! This is %ix fun!' % (username, fun_count)
            API.chat.post_message(channel_id, msg, as_user=True)
            wait = random.randint(1, 10)
            msg = 'You funned %s %i times, now waiting %i seconds' % \
                (username, fun_count, wait)
            print >> sys.stderr, msg
            time.sleep(wait)
    except KeyboardInterrupt:
        API.chat.post_message(channel_id, 'The fun is over.', as_user=True)


@click.command()
@click.argument('username')
def fun(username):
    """Begin execution of fun here."""
    channel_id = find_channel_id(username)

    if channel_id:
        perform_fun(username, channel_id)
    else:
        raise ValueError('could not find IM channel id for `%s`' % username)


if __name__ == '__main__':
    fun()
