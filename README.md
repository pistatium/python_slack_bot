# Python Slack Bot
This is a sample of Slack bot running on Python.

This system is suitable for GoogleAppEngine.

If you want to create bot for your teams Slack,
customize this codes according to the following procedure.

## development setup 
clone from git

   ```
   git clone https://github.com/pistatium/python_slack_bot.git
   ```

install requirements

   ```
   cd python_slack_bot
   pip install -r requirements.txt -t lib
   ```

Run this project locally from the command line:

   ```
   # Require google appengine SDK
   # https://developers.google.com/appengine/downloads?hl=ja
   dev_appserver.py .
   ```

## deploy slack_bot

1. edit app.yaml
    * modify ```application:```
2. deploy to AppEngine
    * ```appcfg.py update .```
3. Setting Slack Integrations
    * Add Integrations Outgoing-web-hook
        * https://slack.com/services/new/outgoing-webhook
    * ![integrations setting](https://raw.githubusercontent.com/pistatium/python_slack_bot/master/static/integration_settings.png)
4. Check
    * On Slack: ```daniel yo```
    * ![daniel sample](https://raw.githubusercontent.com/pistatium/python_slack_bot/master/static/daniel_sample.png)

## Customize
if you want to add bot functions, you should write ```src/bot/daniel.py``` or create new bot class.

```(BaseBot).say()``` detects method matching conditions automatically.


## documents
https://github.com/GoogleCloudPlatform/appengine-python-flask-skeleton
https://slack.com/services/new/outgoing-webhook
https://appengine.google.com/


## LICENSE
```
Copyright (C) 2014 kimihiro_n

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
