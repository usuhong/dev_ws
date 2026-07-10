#include<Servo.h>

const int X_AXIS=A0, Y_AXIS=A1;
const int X_ZERO_POS=510, Y_ZERO_POS=505;
const int SERVO=9;

Servo servo;
void setup() {
  Serial.begin(9600);
  servo.attach(SERVO);

}

void loop() {
  int x=analogRead(X_AXIS);
  int y=analogRead(Y_AXIS);

  x=x-X_ZERO_POS;
  y=(y-Y_ZERO_POS)*-1;

  double degree=atan2(x,y)*180/PI;
  if(degree<0){
    degree=degree*-1;
  }
  degree=180-degree;
  Serial.println(degree);
  servo.write(degree);
  delay(100);

}
