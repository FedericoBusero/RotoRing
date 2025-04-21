import board
import digitalio
from adafruit_debouncer import Debouncer
import neopixel
import rotaryio

import time

NUM_PIXELS = [60,40]
#NUM_PIXELS = [48,24]
pixels = neopixel.NeoPixel(board.IO1, NUM_PIXELS[0]+NUM_PIXELS[1], auto_write=False)
LED_START = [40,0]

# Rotary encoder setup
encoder = rotaryio.IncrementalEncoder(board.IO10, board.IO9)

pin_button = digitalio.DigitalInOut(board.IO13)
pin_button.direction = digitalio.Direction.INPUT
pin_button.pull = digitalio.Pull.UP
switch_button = Debouncer(pin_button)

pin_rotarybutton = digitalio.DigitalInOut(board.IO8)
pin_rotarybutton.direction = digitalio.Direction.INPUT
pin_rotarybutton.pull = digitalio.Pull.UP
switch_rotarybutton = Debouncer(pin_rotarybutton)
