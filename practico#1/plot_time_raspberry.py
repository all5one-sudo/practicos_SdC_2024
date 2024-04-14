import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

df = pd.read_csv('time_log.csv')
freq = df['freq(mhz)']
time = df['time(ms)']

plt.figure()
plt.plot(freq, time)
plt.xlabel('Frecuencia de clock (MHz)')
plt.ylabel('Tiempo (ms)')
plt.title('Duración del programa vs frecuencia de clock')
plt.grid(True)
plt.savefig('data_plot.png')
plt.savefig('data_plot.pdf')

# Interpolacion
f = interp1d(freq, time, kind='quadratic')
freq_interp = np.linspace(75, 250, 500)
coeffs = np.polyfit(freq, time, 2)
p = np.poly1d(coeffs)

plt.figure()
plt.plot(freq_interp, f(freq_interp), '-')
plt.plot(freq, time, 'o', 'r')
plt.xlabel('Frecuencia de clock (MHz)')
plt.ylabel('Tiempo (ms)')
plt.title('Interpolación cuadrática duración del programa vs frecuencia de clock')
plt.grid(True)
plt.xlim(75, 250)
plt.ylim(3500, 13000)
plt.yticks(np.arange(3500, 13000, 3000))
plt.text(80, 4000, f'y = {coeffs[0]:.2e} x^2 + {coeffs[1]:.2e} x + {coeffs[2]:.2e}')
plt.savefig('interpolated_data.png')
plt.savefig('interpolated_data.pdf')