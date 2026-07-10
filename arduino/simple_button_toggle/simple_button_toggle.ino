const int BUTTON=2;
const int LED=7;

int pred_state;
int led_bultin_state;


void setup() {
  pinMode(BUTTON,INPUT);
  pinMode(LED,OUTPUT);
  pinMode(LED_BUILTIN,OUTPUT);

  pred_state=LOW;
  //led_bultin_state=LOW;
  digitalWrite(LED,HIGH);
}

void loop() {
  int input=digitalRead(BUTTON);

  if(input==HIGH && pred_state==LOW){   //버튼을 눌렀을 때
    led_bultin_state=digitalRead(LED_BUILTIN);
    digitalWrite(LED,led_bultin_state);
    digitalWrite(LED_BUILTIN,!led_bultin_state);
    Serial.println("Toggle");
    
  }
  pred_state=input;
}
