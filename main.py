import numpy as np
from fft_class import FFTDrawer
import path
from p5 import *

FFTd = FFTDrawer()

def setup():
    size(800,800)
    FFTd.calculate_fft_values(path.path)

def draw():
    background(0)
    FFTd.draw_epicycles(0,0,0,0)

run()