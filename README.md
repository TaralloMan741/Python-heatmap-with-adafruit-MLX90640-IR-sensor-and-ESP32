# Real-Time-heatmap-using-adafruit-MLX90640-IR-sensor-and-ESP32-Python
Display a real-time heatmap using a python script that reads data through a serial port. ESP32 board collects data coming from the MLX90640 IR sensor, data are the read by the python script through the serial port to which the esp32 is connected. 

## Shopping cart
* Arduino IDE (Legacy or 2)
* VScode
* ESP32 dev kit C V2
* Adafruit MLX 90640 IR sensor
* Bread-board and jumpers (in case the esp32 and the sensor cant be directly conncted)

## 1) Setup Arduino IDE
* Use this link https://www.arduino.cc/en/software/ to download and install your preferred Arduino Ide version (on LINUX I suggest Arduino 1.8.9 Legacy instead of version 2).
* Use this link https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html to install the ESP32 suport for Arduino.
* (ONLY FOR LINUX USERS) use the following command on the terminal to allow serial comunication <br />
   `sudo usermod -a -G dialout $user`. Restart the pc to apply the changes.
* Open the IDE and go to <ins>**tools >> board**</ins>, from the drop-down menu choose <ins>**“ESP32 Dev Module”**</ins>.
* Connect the board and go to <ins>**tools >> port**</ins> to select the port which the board is connected to. On windows it is called __COM3__ (the number may change), for linux users the port is called __/dev/ttyUSB0__.
* Install the libraries for MLX 90640. Go to <ins>**tools >> manage libraries**</ins>, in the library manager window search <ins>**"adafruit_mlx90640"**</ins>, click on install it will ask you if you want to install all or just mlx90640 libraries, click on <ins>"install all"</ins>.

## 2) Setup VScode  
* Install VScode from the following link https://code.visualstudio.com/.
* install python from the following link https://www.python.org/. If you are on LINUX you probably have it already installed, to check open the terminal and type `python3 --version`, the same code can be used on command window (cmd) on Windows.
* Install pip:
    * On Windows run the following command on command line (cmd) `python -m ensurepip --upgrade`, then check if pip is installed by running `pip3 --version`
    * On LINUX run the following commands on terminal: `sudo apt update`, `sudo apt install python3-pip`. to check the version type `pip3 --version`.
* Open VScode, use the following shortcut to open the extension search bar __CTRL+Shift+X__, search __python__, if not installed install it (do not install python debugger), it will automatically install all the needed extensions.
* Install __pyserial numpy and matplotlib__, on Vs code open the terminal and type: `pip3 install pyserial numpy matplotlib`.

## 3) Program ESP32 on Arduino IDE
* Open Arduino IDE and create a sketch, use the script called <a href="https://github.com/TaralloMan741/Real-time-heatmap-python-MLX90640-ESP32/blob/main/MLX90640_32Hz.ino">__MLX90640_32Hz.ino__</a>. Use the 32Hz setting, otherwise it will not work with Python code below.

* upload the sketch on the ESP32, then open the serial monitor to verify that the ESP32 is functioning correctly, you shoud see a stream of numbers, representing each pixel temperature, if this is not the case you have to change the BAUDRATE on the serial monitor to 460800, or whatever value is written in `Serial.begin(460800);`.
* Before going to Vscode be sure to close the serial monitor.

## 4) Plot real-time heatmap on VScode 
* On VScode create a new file. On the top left corner clock on <ins>**file >> New Text File**</ins> (choose python), use the file provided in this repository called <a href="https://github.com/TaralloMan741/Real-time-heatmap-python-MLX90640-ESP32/blob/main/heat_map_32Hz.py">__heat_map_32Hz.py__</a>.
* Save the file in the desired location ad the run it by clicking the triangle shaped button on the top right side. You should see something like this:

https://github.com/user-attachments/assets/55c8c5ca-f98b-4da1-a4e4-8f94753d5188


## ESP32 and MLX90640 wiring


| ESP32  | MLX 90640 |
| ------------- | ------------- |
| GP22  | SCL  |
| GP21  | SDA  |
| GND  | GND  |
| 3V3  | VIN  |


![ESP32-DOIT-DEVKIT-V1-Board-Pinout-36-GPIOs-updated](https://github.com/user-attachments/assets/230f8e6d-63ad-4918-add3-b66e808cf87b)
<figcaption>Image found at https://randomnerdtutorials.com/esp32-pinout-reference-gpios/</figcaption> <br />
<br />
<br />

![adafruit_products_MLX90640_55_back_pinouts](https://github.com/user-attachments/assets/94942398-c675-446f-999e-6b3590b8639b)
<figcaption>Image found at https://learn.adafruit.com/assets/87353 Autor: Kattni Rembor, License: Attribution-ShareAlike Creative Commons</figcaption>

