from p5 import *

import numpy as np

class FFTDrawer:
    def calculate_fft_values(self, path):
        self.fft_values = np.fft.fft(path)
        print(len(self.fft_values))

    def draw_epicycles(self, x_start,y_start, rotation, time):

        x = x_start
        y = y_start

        for fft_val in self.fft_values:
            prevx = x
            prevy = y

            freq = 1
            radius = abs(fft_val)
            phase = np.angle(fft_val)

            x += radius * cos(freq * time + phase + rotation)
            y += radius * sin(freq * time + phase + rotation)


            stroke(255, 100)
            noFill()
            ellipse(prevx, prevy, radius * 2)
            stroke(255)
            line(prevx, prevy, x, y)