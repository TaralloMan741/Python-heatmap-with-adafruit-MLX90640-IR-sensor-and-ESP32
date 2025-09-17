#include <Adafruit_MLX90640.h>

Adafruit_MLX90640 mlx;
float frame[32*24];

void setup() {
  Serial.begin(460800); // baud rate
  delay(100);

  Wire.begin();
  Wire.setClock(1000000);

  if (!mlx.begin(MLX90640_I2CADDR_DEFAULT, &Wire)) {
    Serial.println("MLX90640 non trovato!");
    while (1) delay(10);
  }

  mlx.setMode(MLX90640_CHESS);
  mlx.setResolution(MLX90640_ADC_18BIT);
  mlx.setRefreshRate(MLX90640_32_HZ);
}

void loop() {
  if (mlx.getFrame(frame) != 0) return;

  for (int i = 0; i < 32*24; i++) {
    Serial.print(frame[i], 2); // 2 decimali
    if (i < 32*24 - 1) Serial.print(" "); // spazio come separatore
  }
  Serial.println();
  delay(10);
} 