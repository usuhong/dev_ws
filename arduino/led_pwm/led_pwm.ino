
const int LED=9;
int min,max;
void setup() {
  Serial.begin(9600);
  min=1023,max=0;
  pinMode(LED,OUTPUT);

}

void loop() {
  int light=analogRead(A0);
  if(light<min){
    min=light;
  }
  if(light>max){
    max=light;
  }
  //light=constrain(light,MIN,MAX);

  int output=map(light,min,max,255,0);
  analogWrite(LED,output);


  Serial.print(light);
  Serial.print(", ");
  Serial.println(output);
  delay(100);
  
}
