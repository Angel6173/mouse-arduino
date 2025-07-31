#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

int16_t ax, ay, az;
int16_t gx, gy, gz;

void setup() {
  Serial.begin(9600);
  Wire.begin();
  mpu.initialize();

  if (!mpu.testConnection()) {
    Serial.println("MPU6050 no conectado");
    while (1);
  }

  Serial.println("MPU6050 listo");
}

void loop() {
  mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);

  int moveX = gy / 100; // horizontal
  int moveY = gx / 100; // vertical

  moveX = constrain(moveX, -10, 10);
  moveY = constrain(moveY, -10, 10);

  Serial.print(moveX);
  Serial.print(":");
  Serial.println(moveY);

  delay(10);
}
