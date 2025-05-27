from p5 import *
import numpy as np
import OpenGL.GL as gl
from math import atan2, pi

TWO_PI = 2 * pi

x = []
fourierX = []
time = 0
path = []

# Replace with your own shape if needed
drawing = [Vector(np.cos(t) * 150, np.sin(t) * 150) for t in np.radians(np.arange(0, 360, 2))]

def compute_fourier(x):
    N = len(x)
    X = np.fft.fft(x) / N
    freqs = np.fft.fftfreq(N, d=1)  # Normalized frequency bins

    # Package the result
    result = []
    for k in range(N):
        value = X[k]
        result.append({
            'value': value,
            'freq': freqs[k] * N,  # match manual DFT freq scale
            'amp': abs(value),
            'phase': atan2(value.imag, value.real)
        })

    return sorted(result, key=lambda f: -f['amp'])  # Sort by amplitude descending

def setup():
    global x, fourierX
    size(800, 600)
    x = np.array([complex(pt.x, pt.y) for pt in drawing])
    fourierX = compute_fourier(x)

def epicycles(x, y, rotation, fourier):
    for f in fourier:
        prevx = x
        prevy = y
        freq = f['freq']
        radius = f['amp']
        phase = f['phase']
        x += radius * np.cos(freq * time + phase + rotation)
        y += radius * np.sin(freq * time + phase + rotation)

        stroke(255, 100)
        no_fill()
        ellipse((prevx, prevy), radius * 2, radius * 2)
        stroke(255)
        line((prevx, prevy), (x, y))
    return Vector(x, y)

def draw():
    gl.glViewport(0, 0, width, height)
    global time, path
    background(0)
    v = epicycles(width / 2, height / 2, 0, fourierX)
    path.insert(0, v)

    stroke(255, 255, 0)
    no_fill()

    dt = TWO_PI / len(fourierX)
    time += dt

    if time > TWO_PI:
        time = 0
        path = []

run()


## chatgtp