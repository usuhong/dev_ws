#include <Servo.h>
Servo servo;
const int BUTTON=7;
int prev_state;
int degree;
int dir;
void setup() {
  Serial.begin(9600);
  servo.attach(9);
  pinMode(BUTTON,INPUT);
  prev_state=LOW;
  degree=0;
  dir=20;
  
}

void loop() {
  
  int input=digitalRead(BUTTON);
  if(input==HIGH && prev_state==LOW){     //버튼이 눌리면
    degree+=dir;
    if(degree>=180){
      degree=180;
      dir=-20;
    }
    else if(degree<=0){
      degree=0;
      dir=20;
    }
    Serial.println(degree);
  }
  servo.write(degree);
  
  prev_state=input;
  delay(20);

}
