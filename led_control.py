import math

import board
import neopixel

class LedControl():
    pixels = neopixel.NeoPixel(board.D18, 12,auto_write=False, brightness=0.2)

    def __init__(self):
        self.pixels.fill((0,0,0))

    def set_led(self, m_num_cpu, m_float):

        led_count = math.ceil(m_float/10 * 12/10)
        
        r_pix = math.floor(m_float * 255 / 100)
        g_pix = 255 - (math.floor(m_float * 255 / 100))

        for i in range(led_count * m_num_cpu, led_count * m_num_cpu + 12):
            self.pixels[i] = (r_pix,g_pix,0) 
        for i in range(led_count * m_num_cpu, led_count * m_num_cpu + 12):
            self.pixels[i] = (0,0,0)
        
        self.pixels.show()
    
    def set_rings(self, json_message):
        num_cpu = int(json_message["cpuNum"])

        for i in range(num_cpu):
            cpu_perc = json_message[f"cpu{i}"]
            self.set_led(i, cpu_perc)

    def set_zero(self):
        self.pixels.fill((0,0,0))
        self.pixels.show()
