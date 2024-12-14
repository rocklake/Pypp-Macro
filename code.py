import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import time
import digitalio
from board import *
import random
# _____
#|  __ \        _     _
#| |__) |   _ _| |_ _| |_   _ __ ___   __ _  ___ _ __ ___
#|  ___/ | | |_   _|_   _| | '_ ` _ \ / _` |/ __| '__/ _ \
#| |   | |_| | |_|   |_|   | | | | | | (_| | (__| | | (_)
#|_|    \__, |             |_| |_| |_|\__,_|\___|_|  \___/
#        __/ |
#       |___/
# config start
start_delay = 5.555
log_in = True
if log_in == True:
    username = "py"
    password = "hi"
fan_max = True
slowdown_level = "off"
# chip chipper
chip_chipper_repeat_all = 3
chip_chipper_start_amount = 1020
chip_chipper_cash_repeat = 100
chip_chipper_repeat_amount = 3
chip_chiper_multiplication = 50
chip_chipper_start_multiplication_amount = 1
quintillion_point_chance = 36
chip_chipper_repeat_amount_qt = 49
chosen_chip_of_buying = "r"
# trivia plus plus
trivia_repeat = 6000
# config end
# V 2                      by rocklake
# 1.3
#  |
# \_/
# triva coin in a hour       3,312.373
# rb_cc in a hour            12.575
# bot_points in a hour       795.694
# all points in a hour is    338.282
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
def slowdown(level1):
    if level1 == "l":
        if slowdown_level == "low":
            time.sleep(0.05)
        elif slowdown_level == "min":
            time.sleep(0.1)
        elif slowdown_level == "max":
            time.sleep(0.2)
        elif slowdown_level == "off":
            pass
    elif level1 == "m":
        if slowdown_level == "low":
            time.sleep(0.1)
        elif slowdown_level == "min":
            time.sleep(0.2)
        elif slowdown_level == "max":
            time.sleep(0.3)
        elif slowdown_level == "off":
            pass
    elif level1 == "h":
        if slowdown_level == "low":
            time.sleep(0.2)
        elif slowdown_level == "min":
            time.sleep(0.3)
        elif slowdown_level == "max":
            time.sleep(0.4)
        elif slowdown_level == "off":
            pass
while True:
    time.sleep(start_delay)
    try:
        if log_in == True:
            layout.write(username)
            kbd.press(Keycode.ENTER)
            kbd.release_all()
            time.sleep(0.4)
            layout.write(password)
            kbd.press(Keycode.ENTER)
            kbd.release_all()
            time.sleep(1)
        if fan_max == True:
            layout.write("pinctrl FAN_PWM op dl")
            kbd.press(Keycode.ENTER)
            kbd.release_all()
        # going to py++
        layout.write("tmux")
        kbd.press(Keycode.ENTER)
        kbd.release_all()
        kbd.press(Keycode.SPACE)
        kbd.release_all()
        slowdown("h")
        kbd.press(Keycode.CONTROL)
        kbd.press(Keycode.B)
        kbd.press(Keycode.SHIFT)
        layout.write("%")
        kbd.release_all()
        slowdown("l")
        kbd.press(Keycode.CONTROL)
        kbd.press(Keycode.B)
        kbd.press(Keycode.SHIFT)
        layout.write("%")
        kbd.release_all()
        slowdown("l")
        kbd.press(Keycode.CONTROL)
        kbd.press(Keycode.B)
        kbd.press(Keycode.SHIFT)
        layout.write(":")
        kbd.release_all()
        slowdown("l")
        layout.write("setw synchronize-panes on")
        kbd.press(Keycode.ENTER)
        kbd.release_all()
        slowdown("l")
        layout.write("cd py++")
        kbd.press(Keycode.ENTER)
        kbd.release_all()
        slowdown("l")
        layout.write("python3 py++_start.py")
        kbd.press(Keycode.ENTER)
        kbd.release_all()
        slowdown("m")
        # in py++

        kbd.press(Keycode.ENTER)
        kbd.release_all()
        slowdown("l")
        kbd.press(Keycode.CONTROL)
        kbd.press(Keycode.B)
        kbd.press(Keycode.SHIFT)
        layout.write(":")
        kbd.release_all()
        slowdown("l")
        layout.write("setw synchronize-panes off")
        kbd.press(Keycode.ENTER)
        kbd.release_all()
        slowdown("m")
        # going to trivia
        layout.write("3")
        kbd.press(Keycode.ENTER)
        kbd.release_all()
        slowdown("l")
        layout.write("e")
        kbd.press(Keycode.ENTER)
        kbd.release_all()
        slowdown("l")
        kbd.press(Keycode.CONTROL)
        kbd.press(Keycode.B)
        kbd.press(Keycode.LEFT_ARROW)
        kbd.release_all()
        slowdown("m")
        # going to bot
        layout.write("5")
        kbd.press(Keycode.ENTER)
        kbd.release_all()
        slowdown("l")
        layout.write("l")
        kbd.press(Keycode.ENTER)
        kbd.release_all()
        slowdown("l")
        kbd.press(Keycode.CONTROL)
        kbd.press(Keycode.B)
        kbd.press(Keycode.LEFT_ARROW)
        kbd.release_all()
        slowdown("m")
        # to chip chipper
        layout.write("2")
        kbd.press(Keycode.ENTER)
        kbd.release_all()
        slowdown("l")
        layout.write("l")
        kbd.press(Keycode.ENTER)
        kbd.release_all()
        slowdown("l")
        kbd.press(Keycode.CONTROL)
        kbd.press(Keycode.B)
        kbd.press(Keycode.RIGHT_ARROW)
        kbd.release_all()
        slowdown("l")
        kbd.press(Keycode.CONTROL)
        kbd.press(Keycode.B)
        kbd.press(Keycode.RIGHT_ARROW)
        kbd.release_all()
        slowdown("l")

        kbd.press(Keycode.CONTROL)
        kbd.press(Keycode.B)
        kbd.press(Keycode.SHIFT)
        layout.write(":")
        kbd.release_all()
        slowdown("m")
        layout.write("setw synchronize-panes on")
        kbd.press(Keycode.ENTER)
        kbd.release_all()

        # main code
        while True:
            slowdown("m")
            count1 = 0
            count2 = 0
            gcount = 0
            coun = 0
            qt = random.randint(0, int(quintillion_point_chance))
            qt = int(qt)
            while count1 <= int(trivia_repeat):
                layout.write("8")
                kbd.press(Keycode.ENTER)
                kbd.release_all()
                count1 = count1 + 1
            kbd.press(Keycode.CONTROL)
            kbd.press(Keycode.B)
            kbd.press(Keycode.SHIFT)
            layout.write(":")
            kbd.release_all()
            slowdown("m")
            layout.write("setw synchronize-panes off")
            kbd.press(Keycode.ENTER)
            kbd.release_all()
            slowdown("l")
            kbd.press(Keycode.CONTROL)
            kbd.press(Keycode.B)
            kbd.press(Keycode.LEFT_ARROW)
            kbd.release_all()
            slowdown("l")
            kbd.press(Keycode.CONTROL)
            kbd.press(Keycode.B)
            kbd.press(Keycode.LEFT_ARROW)
            kbd.release_all()
            while coun <= int(chip_chipper_repeat_all):
                layout.write("b")
                kbd.press(Keycode.ENTER)
                kbd.release_all()
                slowdown("l")
                layout.write("1")
                kbd.press(Keycode.ENTER)
                kbd.release_all()
                slowdown("l")
                layout.write("g")
                kbd.press(Keycode.ENTER)
                kbd.release_all()
                while gcount <= chip_chipper_start_amount:
                    kbd.press(Keycode.ENTER)
                    kbd.release_all()
                    gcount = gcount + 1
                gcount = 0
                layout.write("e")
                kbd.press(Keycode.ENTER)
                kbd.release_all()
                slowdown("l")
                r = chip_chipper_start_multiplication_amount
                while count2 <= int(chip_chipper_repeat_amount):
                    layout.write(chosen_chip_of_buying)
                    kbd.press(Keycode.ENTER)
                    kbd.release_all()
                    slowdown("l")
                    r = r + r * chip_chiper_multiplication
                    r = int(r)
                    layout.write(str(r))
                    kbd.press(Keycode.ENTER)
                    kbd.release_all()
                    slowdown("l")
                    layout.write("g")
                    kbd.press(Keycode.ENTER)
                    kbd.release_all()
                    while gcount <= chip_chipper_cash_repeat:
                        kbd.press(Keycode.ENTER)
                        kbd.release_all()
                        gcount = gcount + 1
                    layout.write("e")
                    kbd.press(Keycode.ENTER)
                    kbd.release_all()
                    gcount = 0
                    count2 = count2 + 1
                layout.write("rb")
                kbd.press(Keycode.ENTER)
                kbd.release_all()
                slowdown("l")
                layout.write("s")
                kbd.press(Keycode.ENTER)
                kbd.release_all()
                slowdown("l")
                count1 = 0
                count2 = 0
                gcount = 0
                slowdown("l")
                if qt == 1:
                    layout.write("b")
                    kbd.press(Keycode.ENTER)
                    kbd.release_all()
                    slowdown("l")
                    layout.write("1")
                    kbd.press(Keycode.ENTER)
                    kbd.release_all()
                    slowdown("l")
                    layout.write("g")
                    kbd.press(Keycode.ENTER)
                    kbd.release_all()
                    slowdown("l")
                    while gcount <= chip_chipper_start_amount:
                        kbd.press(Keycode.ENTER)
                        kbd.release_all()
                        gcount = gcount + 1
                    gcount = 0
                    layout.write("e")
                    kbd.press(Keycode.ENTER)
                    kbd.release_all()
                    slowdown("l")
                    r = chip_chipper_start_multiplication_amount
                    while count2 <= int(chip_chipper_repeat_amount_qt):
                        layout.write(chosen_chip_of_buying)
                        kbd.press(Keycode.ENTER)
                        kbd.release_all()
                        slowdown("l")
                        r = r + r * chip_chiper_multiplication
                        r = int(r)
                        layout.write(str(r))
                        kbd.press(Keycode.ENTER)
                        kbd.release_all()
                        slowdown("l")
                        layout.write("g")
                        kbd.press(Keycode.ENTER)
                        kbd.release_all()
                        slowdown("l")
                        while gcount <= chip_chipper_cash_repeat:
                            kbd.press(Keycode.ENTER)
                            kbd.release_all()
                            gcount = gcount + 1
                        layout.write("e")
                        kbd.press(Keycode.ENTER)
                        kbd.release_all()
                        slowdown("l")
                        gcount = 0
                        count2 = count2 + 1
                        d = 0
                    while d <= 100:
                        layout.write("qt")
                        kbd.press(Keycode.ENTER)
                        kbd.release_all()
                        slowdown("l")
                        layout.write("g")
                        kbd.press(Keycode.ENTER)
                        kbd.release_all()
                        slowdown("l")
                        kbd.press(Keycode.ENTER)
                        kbd.release_all()
                        slowdown("l")
                        layout.write("e")
                        kbd.press(Keycode.ENTER)
                        kbd.release_all()
                        d = d + 1
                coun = coun + 1
                slowdown("l")
            kbd.press(Keycode.CONTROL)
            kbd.press(Keycode.B)
            kbd.press(Keycode.RIGHT_ARROW)
            kbd.release_all()
            slowdown("l")
            kbd.press(Keycode.CONTROL)
            kbd.press(Keycode.B)
            kbd.press(Keycode.RIGHT_ARROW)
            kbd.release_all()
            slowdown("l")
            kbd.press(Keycode.CONTROL)
            kbd.press(Keycode.B)
            slowdown("l")
            kbd.press(Keycode.SHIFT)
            layout.write(":")
            kbd.release_all()
            slowdown("m")
            layout.write("setw synchronize-panes on")
            kbd.press(Keycode.ENTER)
            kbd.release_all()
            gcount = 0

    except:
        print("fall")