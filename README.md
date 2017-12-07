# teksaga 防犯システム

## 概要

センサーに近づくとスマホにプッシュ通知(Pushbullet経由)

## 手順

1. png画像に従い、ラズパイのGPIOから回路を組む
1. 同じディレクトリにUltrasonic.py mypush.sh ultrasoundpush.py を置き実行権限を与える
1. [Pushbullet](https://www.pushbullet.com)に登録し、SettingsのCreateAccessTokenから文字列を生成し、mypush.shのYourPushbulletAccessTokenのところに生成したアクセストークンを記入
1. スマート端末にアプリを入れ、通知を許可
1. ultrasoundpush.pyを実行
1. 一定時間以上センサーが人やものを検知すると、スマート端末に通知が飛ぶ
