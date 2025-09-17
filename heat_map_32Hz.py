import serial
import numpy as np
import matplotlib.pyplot as plt

ser = serial.Serial('COM3', 460800, timeout=1)
ser.reset_input_buffer()  # cancella eventuali dati residui

plt.ion()
fig, ax = plt.subplots()
im = ax.imshow(np.zeros((24, 32)), cmap='jet', vmin=20, vmax=40)
plt.colorbar(im)
plt.title("MLX90640 Thermal Image")

try:
    while True:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if not line:
            continue
        try:
            values = np.array(list(map(float, line.split())))
            if values.size == 32*24:
                frame = values.reshape((24, 32))
                im.set_data(frame)
                plt.draw()
                plt.pause(0.01)
        except ValueError:
            continue
except KeyboardInterrupt:
    print("Uscita dal programma...")
finally:
    ser.close()
 