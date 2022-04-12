# -*- coding: utf-8 -*-
from gpiozero import Motor
from time import sleep

### TA8428K モータドライバテスト ###

motor = Motor(14, 15) # GPIO14をIN1へ、GPIO15をIN2へ繋ぐ

motor.forward(0.3) # 0.3はモータの速度
sleep(2) # 2秒間正転し続ける
motor.forward(0.6)
sleep(2)
motor.forward(1.0)
sleep(2)
motor.backward(1.0) # ここで反転する
sleep(2)
motor.backward(0.6)
sleep(2)
motor.backward(0.3)
sleep(2)

motor.stop()