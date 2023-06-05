from matplotlib.backends.backend_tkagg import *
import numpy as np
from numpy import *
import matplotlib.pyplot as plt


# Calcular transformada de Fourier
def calc_trans(t, senal):
    trans = np.fft.fft(senal)
    frec = np.fft.fftfreq(len(senal), t[1] - t[0])
    return frec, trans


def generar_cuadrada(t, freq, num_terms):
    ond_cuad = np.zeros_like(t)
    for n in range(1, num_terms + 1):
        k = 2 * n - 1
        ond_cuad += (4 / (k * pi)) * sin(2 * pi * freq * k * t)
    return ond_cuad


def generar_triangular(t, freq, num_terms):
    ond_trian = np.zeros_like(t)
    for n in range(1, num_terms + 1):
        k = 2 * n - 1
        ond_trian += (8 / (pi ** 2 * k ** 2)) * sin(2 * pi * freq * k * t) * (-1) ** (n + 1)
    return ond_trian


def generar_d_sierra(t, freq, num_terms):
    ond_dsierr = np.zeros_like(t)
    for n in range(1, num_terms + 1):
        k = n
        ond_dsierr += (2 / (pi * k)) * sin(2 * pi * freq * k * t)
    return ond_dsierr
