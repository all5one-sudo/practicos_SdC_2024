import time
import machine

machine.freq(125e6)

def suma_enteros():
    total = 0
    for i in range(333333):
        total += i
    return total

def suma_flotantes():
    total = 0.0
    for i in range(240000):
        total += i
    return total

start_time = time.ticks_ms()
resultado_enteros = suma_enteros()
tiempo_enteros = time.ticks_diff(time.ticks_ms(), start_time)

start_time = time.ticks_ms()
resultado_flotantes = suma_flotantes()
tiempo_flotantes = time.ticks_diff(time.ticks_ms(), start_time)

print("Tiempo enteros en ms: ", tiempo_enteros)
print("Tiempo flotantes en ms: ", tiempo_flotantes)