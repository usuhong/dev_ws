#include <Servo.h>
Servo servo;
const int threshold=62;
int cnt;
unsigned long jump_delayTime;

void jump1(){
  for(int i=65;i<92;i++){
    servo.write(i);
    delay(7);
  }
  servo.write(65);
  if(cnt>=4){
    for(int i=65;i>33;i--){
      servo.write(i);
      delay(7);
    }
  servo.write(65);
  }

  cnt++;
}
void jump(){
   servo.write(15);
  for(int i=15;i<45;i++){
    servo.write(i);
    delay(10);
  }
}
void setup() {
  Serial.begin(9600);
  servo.attach(9);
  servo.write(25);
  cnt=0;
                                      
}

void loop() {

  int light=analogRead(A0);
  if(light<=threshold){    //점프 기준값보다 조도센서 값이 작으면
    jump();
  }
  Serial.print(light);
  Serial.print(",\t");
  Serial.println(cnt);
  delay(50);
}
