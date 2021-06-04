import matplotlib.pyplot as plt
import numpy as np

fs = 44100
t = np.arange(fs).reshape((fs, 1)) / fs
f = 1000
x = np.sin(2 * np.pi * f * t)

fft_size = 65536
X = np.fft.fft(x, fft_size, axis=0)
X = np.abs(X[: fft_size // 2, :])
w = np.arange(fft_size // 2).reshape(fft_size // 2, 1) * fs / fft_size
spectral_centroid = np.sum(w * X) / np.sum(X)

print(f"{spectral_centroid:.2f}")
