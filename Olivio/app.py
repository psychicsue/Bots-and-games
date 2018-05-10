from slackclient import SlackClient

SLACK_TOKEN = "xoxb-346353260501-lrRidik99JvpYTyrjZDS9egw"

sc = SlackClient(SLACK_TOKEN)

if sc.rtm_connect():
    sc.api_call("chat.postMessage", channel="#general",
                text="test", asUser=False)
else:
    print("Connection failed")

