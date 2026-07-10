const int BUTTON=2;
const int LED=7;
int pre_state;


void setup() {
  Serial.begin(9600);   
  pinMode(LED_BUILTIN,OUTPUT);
  pinMode(LED,OUTPUT);
  pinMode(BUTTON,INPUT);
  pre_state=LOW;
  digitalWrite(LED,HIGH);
}


void loop() { 
  int input=digitalRead(BUTTON);

  if(input==HIGH && pre_state==LOW){  //버튼을 누를 때

    digitalWrite(LED_BUILTIN,HIGH);
    digitalWrite(LED,LOW);
    Serial.println("버튼 눌림");
  }
  else if(input==LOW && pre_state==HIGH){ //버튼을 땔 때

    digitalWrite(LED_BUILTIN,LOW);
    digitalWrite(LED,HIGH);
  }
  else{
    return;
  }
  pre_state=input;

}
