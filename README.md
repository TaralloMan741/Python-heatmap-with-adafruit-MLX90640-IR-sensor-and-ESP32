# Python-heatmap-with-adafruit-MLX90640-IR-sensor-and-ESP32
Display an heatmap using a python script that reads data through a serial port. ESP32 board collects data coming from the MLX90640 IR sensor, data are the read by the python script through the serial port to which the esp32 is connected. 

# Shopping list
* Arduino IDE (Legacy or 2)
* VScode
* ESP32 dev kit C V2
* Adafruit MLX 90640 IR sensor

# 1) Setup arduino ide 
* Use this link https://www.arduino.cc/en/software/ to download and install youe preferred Arduino Ide version.
* Use this link https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html to install the ESP32 suport for Arduino.
* (ONLY FOR LINUX USERS) use the following command on the terminal to allow serial comunication, `sudo usermod -a -G dialout $user`. Restart the pc to apply the changes.
* Open the IDE and go to `tools >> board`, from the drop-donw menu choose “ESP32 Dev Module”.
* Connect the board and go to `tools >> port` to select the port which the board is connected to. On windows it is called `COM3` (the number may change), for linux users the port is called `“/dev/ttyUSB0”`.
* Install the libraries for MLX 90640. Go to `tools >> manage libraries`, the library manager opens up, search `"adafruit_mlx90640"`, click on install it will ask you if you want to install all or just mlx90640 libraries, click on `"install all"`.

# 2) Setup VScode  
* Install VScode from the following link https://code.visualstudio.com/.
* install python from the following link https://www.python.org/. If you are on LINUX you might have it already installed, to check open the terminal and type `python3 --version`, the same code can be used on command window (cmd) on Windowns.
* Install pip:
    * On Windows run the following command on command line (cmd): `python -m ensurepip --upgrade`, then check if pip is installed by running `pip3 --version`
    * On LINUX run the following commands on terminal: `sudo apt update`, `sudo apt install python3-pip`. to check the version type `pip3 --version`.
* Open VScode, use the following shortcut to open the extension search bar `CTRL+Shift+X`, search python, if not installed install it (do not install python debugger), it will automatically install all the needed extensions.
* Install pyserial numpy and matplotlib, on Vs code open the terminal and type: `pip3 install pyserial numpy matplotlib`.

# 3) Program ESP32 on Arduino IDE
* Open Arduino IDE and create a sketch, use the following script provided by Adafruit, you can find it in `Arduino folder >> libraries >> Adafruit_MLX90640 >> examples >> MLX90640_simpletest >> MLX90640_simpletest.ino`:

```
#include <Adafruit_MLX90640.h>

Adafruit_MLX90640 mlx;
float frame[32*24]; // buffer for full frame of temperatures

// uncomment *one* of the below to choose 
#define PRINT_TEMPERATURES
//#define PRINT_ASCIIART

void setup() {
  //while (!Serial) delay(10);
  Serial.begin(115200);
  delay(100);

  Serial.println("Adafruit MLX90640 Simple Test");
  //Serial.flush();
  if (! mlx.begin(MLX90640_I2CADDR_DEFAULT, &Wire)) {
    Serial.println("MLX90640 not found!");
    while (1) delay(10);
  }
  Serial.println("Found Adafruit MLX90640");

  Serial.print("Serial number: ");
  Serial.print(mlx.serialNumber[0], HEX);
  Serial.print(mlx.serialNumber[1], HEX);
  Serial.println(mlx.serialNumber[2], HEX);

  //mlx.setMode(MLX90640_INTERLEAVED);
  mlx.setMode(MLX90640_CHESS);
  Serial.print("Current mode: ");
  if (mlx.getMode() == MLX90640_CHESS) {
    Serial.println("Chess");
  } else {
    Serial.println("Interleave");
  }

  mlx.setResolution(MLX90640_ADC_18BIT);
  Serial.print("Current resolution: ");
  mlx90640_resolution_t res = mlx.getResolution();
  switch (res) {
    case MLX90640_ADC_16BIT: Serial.println("16 bit"); break;
    case MLX90640_ADC_17BIT: Serial.println("17 bit"); break;
    case MLX90640_ADC_18BIT: Serial.println("18 bit"); break;
    case MLX90640_ADC_19BIT: Serial.println("19 bit"); break;
  }

  mlx.setRefreshRate(MLX90640_2_HZ);
  Serial.print("Current frame rate: ");
  mlx90640_refreshrate_t rate = mlx.getRefreshRate();
  switch (rate) {
    case MLX90640_0_5_HZ: Serial.println("0.5 Hz"); break;
    case MLX90640_1_HZ: Serial.println("1 Hz"); break;
    case MLX90640_2_HZ: Serial.println("2 Hz"); break;
    case MLX90640_4_HZ: Serial.println("4 Hz"); break;
    case MLX90640_8_HZ: Serial.println("8 Hz"); break;
    case MLX90640_16_HZ: Serial.println("16 Hz"); break;
    case MLX90640_32_HZ: Serial.println("32 Hz"); break;
    case MLX90640_64_HZ: Serial.println("64 Hz"); break;
  }
}

void loop() {
  delay(500);
  if (mlx.getFrame(frame) != 0) {
    Serial.println("Failed");
    return;
  }
  Serial.println("===================================");
  Serial.print("Ambient temperature = ");
  Serial.print(mlx.getTa(false)); // false = no new frame capture
  Serial.println(" degC");
  Serial.println();
  Serial.println();
  for (uint8_t h=0; h<24; h++) {
    for (uint8_t w=0; w<32; w++) {
      float t = frame[h*32 + w];
#ifdef PRINT_TEMPERATURES
      Serial.print(t, 1);
      Serial.print(", ");
#endif
#ifdef PRINT_ASCIIART
      char c = '&';
      if (t < 20) c = ' ';
      else if (t < 23) c = '.';
      else if (t < 25) c = '-';
      else if (t < 27) c = '*';
      else if (t < 29) c = '+';
      else if (t < 31) c = 'x';
      else if (t < 33) c = '%';
      else if (t < 35) c = '#';
      else if (t < 37) c = 'X';
      Serial.print(c);
#endif
    }
    Serial.println();
  }
}
```
* upload the sketch on the ESP32, then open the serial monitor to verify that the ESP32 is functioning correctly, you shoud see a 32 x 24 matrix (with symbols or numbers depending on which line you commented between PRINT_TEMPERATURES or PRINT_ASCIIART). if this is not the case you have to change the BAUDRATE on the serial monitor to 115200, or whatever value is written in `Serial.begin(115200);`.
* Before going to Vscode be sure to close the serial monitor.

# 4) Plot real-time heatmap on VScode 
* Open a new file. On the top left corner clock on `file >> New Text File` (choose python) and copy the foolowing script:
  
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
    print("Uscita dal programma...")<img width="1102" height="691" alt="heatmap_python" src="https://github.com/user-attachments/assets/289a3cb4-6732-4d9b-a28c-36b790e94c12" />

finally:
    ser.close()
```

* save the file in the desired location ad the run it by clicking the triangle shaped button on the top right side. You should see something like this 
<img width="1102" height="691" alt="heatmap_python" src="https://github.com/user-attachments/assets/a9a9f6ae-acb7-4677-9189-cf03deffa437" />
