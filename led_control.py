import math

import board
import neopixel

class LedControl():
    pixels = neopixel.NeoPixel(board.D18, 12,auto_write=False)

    def __init__(self):
        self.pixels.fill((0,0,0))

    def set_led(self, m_float):
        self.set_zero()

        led_count = math.ceil(m_float/10 * 12/10)
        
        r_pix = math.floor(m_float * 255 / 100)
        g_pix = 255 - (math.floor(m_float * 255 / 100))

        for i in range(led_count):
            self.pixels[i] = (r_pix,g_pix,0) 
        self.pixels.show()

    def set_zero(self):
        self.pixels.fill((0,0,0))
        self.pixels.show()
