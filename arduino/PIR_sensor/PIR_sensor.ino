const int PIR=2;

void setup() {
  Serial.begin(9600);
  pinMode(PIR,INPUT);
  
}

void loop() {
  int input=digitalRead(PIR);
  Serial.println(input);

  delay(100);
}
