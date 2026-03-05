# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 21:34:42 2026

@author: Shara Cetina y Juanita Gomez
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal, fft

#Parte A

#DATOS SHARA
#Definición de señales
x1 = np.array([1, 0, 5, 0, 0, 9, 1, 9, 3, 2])
h1 = np.array([5, 6, 0, 0, 9, 3, 4])

#Convolución
conv_result = signal.convolve(x1, h1, mode='full') # 'full' devuelve la convolución completa (longitud N+M-1)

#Grafica
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.stem(x1)
plt.title('Señal de entrada $x(t)$')

plt.subplot(3, 1, 2)
plt.stem(h1)
plt.title('Respuesta al impulso $h(t)$')

plt.subplot(3, 1, 3)
plt.stem(conv_result)
plt.title('Convolución $x(t) * h(t)$')

plt.tight_layout()
plt.show()

#DATOS JUANITA
#Definición de señales
x2 = np.array([1, 0, 1, 4, 9, 8, 0, 4, 2, 8])
h2 = np.array([5, 6, 0, 0, 8, 9, 8])

#Convolución
conv_result_2 = signal.convolve(x2, h2, mode='full') # 'full' devuelve la convolución completa (longitud N+M-1)

#Grafica
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.stem(x2)
plt.title('Señal de entrada $x(t)$')

plt.subplot(3, 1, 2)
plt.stem(h2)
plt.title('Respuesta al impulso $h(t)$')

plt.subplot(3, 1, 3)
plt.stem(conv_result_2)
plt.title('Convolución $x(t) * h(t)$')

plt.tight_layout()
plt.show()

print ("Convolución Datos Shara:",conv_result)
print ("Convolución Datos Juanita:",conv_result_2)
print ("")
#-----------------------------------------------------------------------------
#Parte B

#Definición de parámetros
Ts = 1.25e-3
n = np.arange(0, 9)  # Rango para 0 <= n < 9

# Definición de señales
x1 = np.cos(2 * np.pi * 100 * n * Ts)
x2 = np.sin(2 * np.pi * 100 * n * Ts)

#Correlación cruzada
correlacion = np.correlate(x1, x2, mode='full')

#Definición de desplazamientos (lags) para el eje X
lags = np.arange(-len(x1) + 1, len(x1))

#Representación gráfica
plt.figure(figsize=(10, 6))
plt.stem(lags, correlacion)
plt.title('Correlación Cruzada entre $x_1[n]$ y $x_2[n]$')
plt.xlabel('Desplazamiento (m)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.show()

#Secuencia resultante
print(f"Secuencia resultante: {correlacion}")
print(f"Longitud de la secuencia: {len(correlacion)}")
print("")
#------------------------------------------------------------------------

#Parte C

SenalClase = np.loadtxt("EOG.txt")

fs = 1000
tiempo = np.arange(len(SenalClase)) / fs

plt.figure(figsize=(12,4))

plt.plot(tiempo, SenalClase, linewidth=1.5, alpha=0.9)

plt.title("Señal EOG", fontsize=14)
plt.xlabel("Tiempo (s)", fontsize=12)
plt.ylabel("Potencial de Acción", fontsize=12)
plt.xlim(tiempo[0], tiempo[-1])  # ajusta el eje x
plt.grid(True, linestyle="--", alpha=0.6)

plt.show()

#Caracterizar señal

media_np = np.mean(SenalClase)
std_np = np.std(SenalClase, ddof=1)
cv_np = std_np/media_np
valor_max = np.max(SenalClase)
valor_min = np.min(SenalClase)


print("Media:", media_np)
print("Desviación estándar:", std_np)
print("Coeficiente de variación:", cv_np)
print("Valor máximo:",valor_max)
print("Valor máximo:",valor_min)
print ("")
plt.figure()
plt.hist(SenalClase, bins=30)
plt.title("Histograma de la señal EOG")
plt.xlabel("Intervalos de frecuencia")
plt.ylabel("Frecuencia")
plt.show()


#Transformada de Fourier

n = len(SenalClase)
f_axis = np.fft.fftfreq(n, 1/fs)[:n//2]
fft_signal = np.abs(fft.fft(SenalClase)[:n//2])

#Gráfica de la transformada
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(f_axis, fft_signal)
plt.title("Transformada de Fourier")


#Densidad Espectral de potencia

freqs, psd = signal.welch(SenalClase, fs)

plt.subplot(1, 2, 2)
plt.semilogy(freqs, psd)
plt.title("Densidad Espectral de Potencia (PSD)")
plt.show()

#Dominio de la frecuencia

media_np = np.mean(fft_signal)
std_np = np.std(fft_signal, ddof=1)
cv_np = std_np/media_np
valor_max = np.max(fft_signal)
valor_min = np.min(fft_signal)


print("Media:", media_np)
print("Desviación estándar:", std_np)
print("Coeficiente de variación:", cv_np)
print("Valor máximo:",valor_max)
print("Valor máximo:",valor_min)


#Histograma en el dominio de la frecuencia

plt.figure()
plt.hist(fft_signal, bins = 2500)

plt.xlim(0,10)

plt.title("Histograma de la señal EOG")
plt.xlabel("Hz")
plt.ylabel("Intensidad")
plt.show()