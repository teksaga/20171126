# -*- coding: utf-8 -*-
#
#  日経Linux 2015年7月号
#  特集2  Part3
#  超音波距離センサー「HC-SR04」制御ライブラリ
#
#  (c) 2015 Kazuhiro Fukuda and NikkeiBP
#

# 『使い方』
#
# 【インスタンスの作成】
# インスタンス名 = hc_sr04(トリガー端子,エコー端子)
#   利用するにはhc_sr04()でインスタンスを作成する
#     トリガー端子：HC-SR04のTrig端子に接続したGPIOの端子番号
#     エコー端子：HC-SR04のEcho端子に接続したGPIOの端子番号
#
# 【関数】
# インスタンス名.measure()
#   障害物までの距離を測定する

import time
import RPi.GPIO as GPIO

class Ultrasonic:
	def __init__(self,trig,echo):
		self.trig = trig
		self.echo = echo
		GPIO.setup(trig, GPIO.OUT)
		GPIO.setup(echo, GPIO.IN)
		GPIO.output(trig, GPIO.LOW)
		time.sleep(1)


	def measure(self):
		GPIO.output(self.trig, GPIO.HIGH)
		time.sleep(0.00001)
		GPIO.output(self.trig, GPIO.LOW)
		while GPIO.input(self.echo) == 0:
			sigoff = time.time()

		while GPIO.input(self.echo) == 1:
			sigon = time.time()

		return (sigon - sigoff) * 17000

