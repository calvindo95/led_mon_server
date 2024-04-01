import math

import board
import neopixel

class LedControl():
    pixels = None

    def __init__(self,num_cpu):
        num_pixels = 12 * (num_cpu+1)
        self.pixels = neopixel.NeoPixel(board.D18, num_pixels,auto_write=False, brightness=0.2)
        self.pixels.fill((0,0,0))

    def set_led(self, cpu_num, m_float):
        led_count = math.floor(m_float/10 * 12/10)
        
        r_pix = math.floor(m_float * 255 / 100)
        g_pix = 255 - (math.floor(m_float * 255 / 100))
        for i in range(12 * (cpu_num), led_count + 12 * (cpu_num)):
            self.pixels[i] = (r_pix,g_pix,0)
 
        for i in range(led_count + 12 * cpu_num, (cpu_num * 12)+12):
            self.pixels[i] = (0,0,0)
    
    def set_rings(self, json_message):
        num_cpu = int(json_message["cpuNum"])
        for i in range(num_cpu+1):
            cpu_perc = json_message["CPU"][f"cpu{i}"]
            self.set_led(i, cpu_perc)

    def set_zero(self):
        self.pixels.fill((0,0,0))
        self.pixels.show()

    def set_show(self):
        self.pixels.show()
