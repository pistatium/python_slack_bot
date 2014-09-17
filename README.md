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
   dev_appserver.py .
   ```

Visit the application [http://localhost:8080](http://localhost:8080)

## deploy


## documents
https://slack.com/services/new/outgoing-webhook


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
