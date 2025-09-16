# Real-Time-heatmap-using-adafruit-MLX90640-IR-sensor-and-ESP32-Python
Display a real-time heatmap using a python script that reads data through a serial port. ESP32 board collects data coming from the MLX90640 IR sensor, data are the read by the python script through the serial port to which the esp32 is connected. 

## Shopping list
* Arduino IDE (Legacy or 2)
* VScode
* ESP32 dev kit C V2
* Adafruit MLX 90640 IR sensor

## 1) Setup Arduino IDE
* Use this link https://www.arduino.cc/en/software/ to download and install youe preferred Arduino Ide version.
* Use this link https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html to install the ESP32 suport for Arduino.
* (ONLY FOR LINUX USERS) use the following command on the terminal to allow serial comunication, `sudo usermod -a -G dialout $user`. Restart the pc to apply the changes.
* Open the IDE and go to `tools >> board`, from the drop-donw menu choose “ESP32 Dev Module”.
* Connect the board and go to `tools >> port` to select the port which the board is connected to. On windows it is called `COM3` (the number may change), for linux users the port is called `“/dev/ttyUSB0”`.
* Install the libraries for MLX 90640. Go to `tools >> manage libraries`, in the library manager window search `"adafruit_mlx90640"`, click on install it will ask you if you want to install all or just mlx90640 libraries, click on `"install all"`.

## 2) Setup VScode  
* Install VScode from the following link https://code.visualstudio.com/.
* install python from the following link https://www.python.org/. If you are on LINUX you probably have it already installed, to check open the terminal and type `python3 --version`, the same code can be used on command window (cmd) on Windowns.
* Install pip:
    * On Windows run the following command on command line (cmd): `python -m ensurepip --upgrade`, then check if pip is installed by running `pip3 --version`
    * On LINUX run the following commands on terminal: `sudo apt update`, `sudo apt install python3-pip`. to check the version type `pip3 --version`.
* Open VScode, use the following shortcut to open the extension search bar `CTRL+Shift+X`, search `python`, if not installed install it (do not install python debugger), it will automatically install all the needed extensions.
* Install pyserial numpy and matplotlib, on Vs code open the terminal and type: `pip3 install pyserial numpy matplotlib`.

## 3) Program ESP32 on Arduino IDE
* Open Arduino IDE and create a sketch, use the script called `MLX90640_simpletest.ino` (it can be found in `Arduino folder >> libraries >> Adafruit_MLX90640 >> examples >> MLX90640_simpletest >> MLX90640_simpletest.ino`).

* upload the sketch on the ESP32, then open the serial monitor to verify that the ESP32 is functioning correctly, you shoud see a 32 x 24 matrix (with symbols or numbers depending on which line you commented between PRINT_TEMPERATURES or PRINT_ASCIIART). if this is not the case you have to change the BAUDRATE on the serial monitor to 115200, or whatever value is written in `Serial.begin(115200);`.
* Before going to Vscode be sure to close the serial monitor.

## 4) Plot real-time heatmap on VScode 
* On VScode create a new file. On the top left corner clock on `file >> New Text File` (choose python), use the file provided in this repository called `RT_heatmap_serial.py`.
*save the file in the desired location ad the run it by clicking the triangle shaped button on the top right side. You should see something like this:
<img width="1102" height="691" alt="heatmap_python" src="https://github.com/user-attachments/assets/a9a9f6ae-acb7-4677-9189-cf03deffa437" />
