const int ledPins[8]={13,12,11,10,9,8,7,6};
const int max=989,min=33;
unsigned long ledTime;

int cur_level;
void setup() {
  Serial.begin(9600);
  for(int i=0;i<8;i++){
    pinMode(ledPins[i],OUTPUT);
    digitalWrite(ledPins[i],LOW);
  }
  ledTime=0;
  cur_level=0;
}

void loop() {
  int volume=analogRead(A0);
  volume=constrain(volume,min,max);

  int target_level=map(volume,min,max,0,8);

  if(target_level>cur_level){
    cur_level=target_level;
  }
  else{
    if(millis()-ledTime>10 && cur_level!=0){
      ledTime=millis();
      cur_level--;
    }
  }
  
  for(int i=0;i<8;i++){
    if(i<cur_level){
      digitalWrite(ledPins[i],HIGH);  
    }
    else{
      digitalWrite(ledPins[i],LOW);
    }
  }
  Serial.print("TargetLevel:");
  Serial.print(target_level);
  Serial.print("\t");
  Serial.print("display:");
  Serial.println(cur_level);
  
}
