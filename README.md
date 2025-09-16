# Python-heatmap-with-adafruit-MLX90640-IR-sensor-and-ESP32
Display an heatmap using a python script that reads data through a serial port. ESP32 board collects data coming from the MLX90640 IR sensor, data are the read by the python script through the serial port to which the esp32 is connected. 

# Shopping list
* Arduino IDE (Legacy or 2)
* VS code
* ESP32 dev kit C V2
* Adafruit MLX 90640 IR sensor

# 1) Setup arduino ide 
* Use this link https://www.arduino.cc/en/software/ to download and install youe preferred Arduino Ide version.
* Use this link https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html to install the ESP32 suport for Arduino.
* (ONLY FOR LINUX USERS) use the following command on the terminal to allow serial comunication, sudo usermod -a -G dialout $user. Restart the pc to apply the changes.
* Open the IDE and go to tools >> board, from the drop-donw menu choose “ESP32 Dev Module”.
* Connect the board and go to tools >> port to select the port which the board is connected to. On windows it is called COM3 (the number may change), for linux users the port is called “/dev/ttyUSB0”.
* Install the libraries for MLX 90640. Go to tools >> manage libraries, the library manager opens up, search "adafruit_mlx90640", click on install it will ask you if you want to install all or just mlx90640 libraries, click on "all".

# 2) Setup VS code  
* Install VS code from the following link https://code.visualstudio.com/.
* install python from the following link https://www.python.org/. If you are on LINUX you might have it already installed, to check open the terminal and type python3 --version, the same code can be used on command window (cmd) on Windowns.
* Install pip:
    * On Windows run the following command on command line (cmd): python -m ensurepip --upgrade, then check if pip is installed by running pip3 --version
    * On LINUX run the following commands on terminal: sudo apt update, sudo apt install python3-pip. to check the version type pip3 --version.
* Open VS code, use the following shortcut to open the extension search bar CTRL+Shift+X, search python, if not installed install it (do not install python debugger), it will automatically install all the needed extensions.
* Install pyserial numpy and matplotlib, on Vs code open the terminal and type: pip3 install pyserial numpy matplotlib.
* Open a new file. On the top left corner clock on file >> New Text File (choose python) and copy the foolowing script:
  
```
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
    print("Uscita dal programma...")
finally:
    ser.close()
```

* save the file in the desired location ad the run it by clicking the triangle shaped button on the top right side. You should see something like this 
