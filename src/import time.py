import time
import sys

# Definir los caracteres que formarán la rueda giratoria
spinner = ['|', '/', '-', '\\']

# Tiempo de espera entre los cambios de frame
delay = 0.1

# Número de ciclos de la animación
cycles = 20

for _ in range(cycles):
    for frame in spinner:
        # Muestra el frame actual
        sys.stdout.write('\r' + frame)
        sys.stdout.flush()
        # Espera antes de pasar al siguiente frame
        time.sleep(delay)

# Deja la línea limpia después de la animación
sys.stdout.write('\r ')
