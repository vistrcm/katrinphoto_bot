# This bot sends photos of beautiful cat.

Link: telegram.me/KatrinPhoto_bot

To run docker container with application create copy of katrinbot_settings.py with valid tokens and start by:

```
docker run -d -v  ${PWD}/katrinbot_settingsprod.py:/usr/src/app/katrinbot_settings.py -p 8080:8080 katrinphoto_bot
```
