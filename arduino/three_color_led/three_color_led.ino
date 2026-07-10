const int RED=9,GREEN=10,BLUE=11;
const int BUTTON=7;

enum LEDState{
  OFF,
  LED_RED,
  LED_GREEN,
  LED_BLUE,
};

LEDState state;
int pre_state;

void setup() {
  Serial.begin(9600);
  pinMode(BUTTON,INPUT);
  pinMode(RED,OUTPUT);
  pinMode(GREEN,OUTPUT);
  pinMode(BLUE,OUTPUT);

  state=OFF;
  pre_state=LOW;

}

void loop() {
  int input=digitalRead(BUTTON);

  if(input==HIGH && pre_state==LOW){  //버튼이 눌렸을 때
    
    state=(LEDState)((state+1)%4);    //LEDState 타입으로 명시적 형 변환
  }

  switch(state){
  case OFF:
    digitalWrite(RED,LOW);
    digitalWrite(GREEN,LOW);
    digitalWrite(BLUE,LOW);
    break;
  
  case LED_RED:
    digitalWrite(RED,HIGH);
    digitalWrite(GREEN,LOW);
    digitalWrite(BLUE,LOW);
    break;
  
  case LED_GREEN:
    digitalWrite(RED,LOW);
    digitalWrite(GREEN,HIGH);
    digitalWrite(BLUE,LOW);
    break;
  case LED_BLUE:
    digitalWrite(RED,LOW);
    digitalWrite(GREEN,LOW);
    digitalWrite(BLUE,HIGH);
    break;
  default:
    break;
  }
  pre_state=input;
  delay(50);
}
