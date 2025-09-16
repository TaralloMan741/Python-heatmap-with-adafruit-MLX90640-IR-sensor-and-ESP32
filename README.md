# Python-heatmap-with-adafruit-MLX90640-IR-sensor-and-ESP32
Display an heatmap using a python script that reads data through a serial port. ESP32 board collects data coming from the MLX90640 IR sensor, data are the read by the python script through the serial port to which the esp32 is connected. 

# lista della spesa
* Arduino IDE (Legacy or 2)
* VS code
* ESP32 dev kit C V2
* Adafruit MLX 90640 IR sensor

# 1) Setup arduino ide 
* Use this link https://www.arduino.cc/en/software/ to download and install youe preferred Arduino Ide version.
* Use this link https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html to install the ESP32 suport for Arduino.
* (ONLY FOR LINUX USERS) use the following command on the terminal to allow serial comunication, sudo usermod -a -G dialout $user. Restart the pc to apply the changes
* Open the IDE and go to tools >> board, from the drop-donw menu choose “ESP32 Dev Module”
* Connect the board and go to tools >> port to select the port which the board is connected to. On windows it is called COM3 (the number may change), for linux users the port is called “/dev/ttyUSB0”.
* Install the libraries for MLX 90640. Go to tools >> manage libraries, the library manager opens up, search "adafruit_mlx90640", click on install it will ask you if you want to install all or just mlx90640 libraries, click on "all".

# 2) Setup VS code  
