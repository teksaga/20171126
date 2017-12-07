#!/bin/bash
CURL=/usr/bin/curl
PUSHBULLET_TOKEN= #YourPushbulletAccessToken
PUSHBULLET_TITLE=Raspberry\ Pi

LANG=ja_JP.utf8

${CURL} --header "Access-Token: ${PUSHBULLET_TOKEN}" \
		--header "Content-Type: application/json" \
		--request POST \
		--data-binary "{\"type\": \"note\", \"title\": \"${PUSHBULLET_TITLE}\", \"body\": \"$1\"}" \
		https://api.pushbullet.com/v2/pushes

