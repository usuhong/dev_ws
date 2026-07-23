const int LED_BULITIN=2;

void setup() {
  
  pinMode(LED_BULITIN,OUTPUT);

}

void loop() {
  
  digitalWrite(LED_BULITIN,HIGH);
  delay(500);
  digitalWrite(LED_BULITIN,LOW);
  delay(500);


}
