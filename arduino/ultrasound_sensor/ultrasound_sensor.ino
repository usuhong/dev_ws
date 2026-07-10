const int TRIG=9;
const int ECHO=8;
const int LED=4;

void setup() {
  Serial.begin(9600);
  pinMode(TRIG,OUTPUT);
  pinMode(ECHO,INPUT);
  pinMode(LED,OUTPUT);

}

void loop() {
  
  long duration, distance;

  digitalWrite(TRIG,LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG,HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG,LOW);

  //HIGH를 받을 때까지 걸리는 시간(ms)
  duration=pulseIn(ECHO,HIGH);

  // 거리를 cm로 계산(34000/1000000/2)
  distance=duration*17/1000;

  if(distance<30){
    digitalWrite(LED,HIGH);
  }
  else{
    digitalWrite(LED,LOW);
  }
  Serial.print("시간: ");
  Serial.print(duration);
  Serial.print(", ");
  Serial.print("거리: ");
  Serial.println(distance);
  

  delay(1000);


}
