
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import cwt, ricker

np.random.seed(42)
data_subset = np.random.normal(0, 1, 10000)

widths = np.arange(1, 50)
cwtmatr = cwt(data_subset, ricker, widths)
power = np.mean(np.abs(cwtmatr)**2, axis=1)

log_widths = np.log(widths)
log_power = np.log(power)
start, end = 10, 40
coeffs = np.polyfit(log_widths[start:end], log_power[start:end], 1)
slope = coeffs[0]
fractal_dim = (5 + slope) / 2

plt.figure(figsize=(8,6))
plt.plot(log_widths, log_power, 'o-', label='Datos CWT')
plt.plot(log_widths[start:end], np.poly1d(coeffs)(log_widths[start:end]), 'r--',
         label=f'Ajuste lineal (pendiente={slope:.2f})')
plt.xlabel("log(Escala)")
plt.ylabel("log(Potencia promedio)")
plt.title("Análisis Wavelet del CMB\nEstimación de dimensión fractal")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("wavelet_fractal_plot.png")

print(f"Pendiente: {slope:.3f}")
print(f"Dimensión fractal estimada: Df = {fractal_dim:.3f}")
