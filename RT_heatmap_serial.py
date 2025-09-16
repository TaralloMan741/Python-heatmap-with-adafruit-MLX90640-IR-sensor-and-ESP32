import serial
import numpy as np
import matplotlib.pyplot as plt
import time

# Apri la seriale (se non è COM3, sostituirla con la porta corretta)
ser = serial.Serial('COM3', 115200, timeout=1)

def read_frame():
    values = []
    while len(values) < 32*24:  # finché non abbiamo 768 valori
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if not line:
            continue
        # Rimuove eventuali spazi extra e split su virgola
        parts = [s.strip() for s in line.split(',') if s.strip()]
        try:
            nums = list(map(float, parts))
            values.extend(nums)
        except ValueError:
            # Se qualche valore non è convertibile, lo ignora
            continue
    # Restituisce un frame 24x32
    return np.array(values[:32*24]).reshape((24, 32))

# Inizializza Matplotlib
plt.ion()
fig, ax = plt.subplots()
im = ax.imshow(np.zeros((24, 32)), cmap='jet', vmin=25, vmax=40)
plt.colorbar(im)
plt.title("MLX90640 Thermal Image")

try:
    while True:
        frame = read_frame()
        im.set_data(frame)
        plt.draw()
        plt.pause(0.01)
except KeyboardInterrupt:
    print("Uscita dal programma...")<img width="1102" height="691" alt="heatmap_python" src="https://github.com/user-attachments/assets/289a3cb4-6732-4d9b-a28c-36b790e94c12" />

finally:
    ser.close()
