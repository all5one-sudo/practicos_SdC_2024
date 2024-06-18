import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button
import time

# Path del dispositivo de entrada
device = "dev/input_device"


# Función para escribir en el dispositivo de entrada
def write_character_device(data):
    with open(device, "w") as device_file:
        device_file.write(data)


# Pin por defecto seleccionado
default_device = "22"
current_pin = default_device
write_character_device(default_device)

# Variables globales para almacenar los valores leídos
values_pin22 = []
values_pin27 = []

# Pin actual seleccionado para la visualización
current_pin = 22


# Función de actualización para la animación
def update(frame):
    with open(device, "r") as device_file:
        read_data = device_file.read()
        value = int(read_data)
        global current_pin, ax
        if current_pin == "22":
            values_pin22.append(value)
            if len(values_pin22) > 10:
                values_pin22.pop(0)
            ax.clear()
            ax.plot(values_pin22)
        else:
            values_pin27.append(value)
            if len(values_pin27) > 50:
                values_pin27.pop(0)
            ax.clear()
            ax.plot(values_pin27)
        ax.set_title(f"Entrada Pin {current_pin}")
        ax.set_xlabel("Tiempo (s)")


# Función para cambiar el pin activo
def change_pin(event):
    global current_pin
    current_pin = "22" if current_pin == "27" else "27"  # se selecciona el pin a leer
    write_character_device(current_pin)
    values_pin22.clear()
    values_pin27.clear()


# Figura de matplotlib
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)

# Boton para cambiar de grafico
ax_button = plt.axes([0.81, 0.05, 0.1, 0.075])
btn = Button(ax_button, "Cambiar Pin")
btn.on_clicked(change_pin)

# Animacion de matplotlib
ani = animation.FuncAnimation(fig, update, interval=1000)  # intervalo de 1 segundo

plt.show()
