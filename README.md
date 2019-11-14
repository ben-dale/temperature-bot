# Temperature bot

## Setup

### Arduino
TODO

### Imgur
Imgur is used to host the image publically online.
1. Create an [Imgur](https://imgur.com/) account.
2. [Register a new application](https://api.imgur.com/oauth2/addclient), selecting "Anonymous usage without user authorization".
3. Make a note of the client ID.

### Slack
There is an assumption that you already have a Slack account if you're reading this.
1. [Create a new app](https://api.slack.com/apps) under the desired workspace.
2. Enable "Incoming Webhooks" for your application.
3. Make a note of the webhook URL.

### Python dependencies
```
pip3 install pyserial
pip3 install matplotlib
pip3 install requests
```

### Cronjobs
```
chmod +x log_temperature.py
chmod +x generate_temperature_report.py
crontab -e
0 */1 * * * log_temperature.py [ARDUINO_LOCATION] >> log_temperature.log 2>&1
1 */1 * * * generate_temperature_report.py [IMGUR_CLIENT_ID] [SLACK_WEBHOOK_URL] [GRAPH_TITLE] >> generate_temperature_report.log 2>&1
```
