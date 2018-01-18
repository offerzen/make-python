import os
import rootbot
import time
from commands import run_command
from slackclient import SlackClient

DEFAULT_RESPONSE = "Sorry, I don't understand you"
API_TOKEN = os.environ.get('SLACK_API_TOKEN')


def run():
    slack_client = SlackClient(API_TOKEN)
    bot_id = slack_client.api_call("auth.test")["user_id"]

    if slack_client.rtm_connect(with_team_state=False):
        print("Successfully connected, listening for events")
        while True:
            events = slack_client.rtm_read()
            for event in events:
                handle_event(event, slack_client, bot_id)

            time.sleep(1)
    else:
        print("Connection Failed")


def handle_event(event, client, bot_id):
    if event['type'] != 'message':
        return

    if event['user'] == bot_id:
        return

    response = run_command(event['text'])

    client.api_call(
        "chat.postMessage",
        channel=event['channel'],
        text=response or DEFAULT_RESPONSE,
        as_user=True)



if __name__ == "__main__":
    run()
