import keyboard
import time

F8_DOWN = False
F9_DOWN = False

def on_press(key):
    global F8_DOWN
    global F9_DOWN
    if key == 'F8':
        F8_DOWN = True
    if key == 'F9':
        F9_DOWN = True

def on_release(key):
    global F8_DOWN
    global F9_DOWN
    if key == 'F8':
        F8_DOWN = False
    if key == 'F9':
        F9_DOWN = False

keyboard.on_press(on_press)
keyboard.on_release(on_release)

while True:
    if F8_DOWN:
        keyboard.press('left_click')
        keyboard.release('left_click')
        time.sleep(0.008)
    if F9_DOWN:
        keyboard.press('right_click')
        keyboard.release('right_click')
        time.sleep(0.008)
