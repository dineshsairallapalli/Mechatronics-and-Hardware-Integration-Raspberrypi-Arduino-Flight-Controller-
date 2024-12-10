#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;

const int servo1Pin = 3;
const int servo2Pin = 5;
const int servo3Pin = 6;
const int servo4Pin = 9;

int servo1Pos = 0;
int servo2Pos = 0;
int servo3Pos = 90;
int servo4Pos = 90;

bool isMovingForward = false;

void setup() {
  servo1.attach(servo1Pin);
  servo2.attach(servo2Pin);
  servo3.attach(servo3Pin);
  servo4.attach(servo4Pin);

  servo1.write(servo1Pos);
  servo2.write(servo2Pos);
  servo3.write(servo3Pos);
  servo4.write(servo4Pos);

  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char cmd = Serial.read();
    if (cmd == 'W') {
      if (!isMovingForward) {
        isMovingForward = true;
        moveMotors();
      }
    } else if (cmd == 'V') {
      if (isMovingForward) {
        isMovingForward = false;
        moveMotors();
      }
    }
  }
}

void moveMotors() {
  if (isMovingForward) {
    for (int pos = 0; pos <= 90; pos++) {
      servo1.write(pos);
      servo2.write(pos);
      servo3.write(90 - pos);
      servo4.write(90 - pos);
      delay(15);
    }
  } else {
    for (int pos = 90; pos >= 0; pos--) {
      servo1.write(pos);
      servo2.write(pos);
      servo3.write(90 - pos);
      servo4.write(90 - pos);
      delay(15);
    }
  }
}