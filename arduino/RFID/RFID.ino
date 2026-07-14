/*
 * --------------------------------------------------------------------------------------------------------------------
 * Example sketch/program showing how to read data from a PICC to serial.
 * --------------------------------------------------------------------------------------------------------------------
 * This is a MFRC522 library example; for further details and other examples see: https://github.com/miguelbalboa/rfid
 * 
 * Example sketch/program showing how to read data from a PICC (that is: a RFID Tag or Card) using a MFRC522 based RFID
 * Reader on the Arduino SPI interface.
 * 
 * When the Arduino and the MFRC522 module are connected (see the pin layout below), load this sketch into Arduino IDE
 * then verify/compile and upload it. To see the output: use Tools, Serial Monitor of the IDE (hit Ctrl+Shft+M). When
 * you present a PICC (that is: a RFID Tag or Card) at reading distance of the MFRC522 Reader/PCD, the serial output
 * will show the ID/UID, type and any data blocks it can read. Note: you may see "Timeout in communication" messages
 * when removing the PICC from reading distance too early.
 * 
 * If your reader supports it, this sketch/program will read all the PICCs presented (that is: multiple tag reading).
 * So if you stack two or more PICCs on top of each other and present them to the reader, it will first output all
 * details of the first and then the next PICC. Note that this may take some time as all data blocks are dumped, so
 * keep the PICCs at reading distance until complete.
 * 
 * @license Released into the public domain.
 * 
 * Typical pin layout used:
 * -----------------------------------------------------------------------------------------
 *             MFRC522      Arduino       Arduino   Arduino    Arduino          Arduino
 *             Reader/PCD   Uno/101       Mega      Nano v3    Leonardo/Micro   Pro Micro
 * Signal      Pin          Pin           Pin       Pin        Pin              Pin
 * -----------------------------------------------------------------------------------------
 * RST/Reset   RST          9             5         D9         RESET/ICSP-5     RST
 * SPI SS      SDA(SS)      10            53        D10        10               10
 * SPI MOSI    MOSI         11 / ICSP-4   51        D11        ICSP-4           16
 * SPI MISO    MISO         12 / ICSP-1   50        D12        ICSP-1           14
 * SPI SCK     SCK          13 / ICSP-3   52        D13        ICSP-3           15
 *
 * More pin layouts for other boards can be found here: https://github.com/miguelbalboa/rfid#pin-layout
 */

#include <SPI.h>
#include <MFRC522.h>
#include <List.hpp>

#define RST_PIN         9          // Configurable, see typical pin layout above
#define SS_PIN          10         // Configurable, see typical pin layout above

List<MFRC522::Uid> tag_list;
MFRC522 mfrc522(SS_PIN, RST_PIN);  // Create MFRC522 instance

const int BUTTON=2,RED=3,GREEN=5,BLUE=6;
unsigned long prevTime;
int pre_state,blinkcnt;
bool registerMode;
bool ledOn,blinkRed,blinkBlue;
void setup() {
	Serial.begin(9600);		// Initialize serial communications with the PC
	while (!Serial);		// Do nothing if no serial port is opened (added for Arduinos based on ATMEGA32U4)
	SPI.begin();			// Init SPI bus
	mfrc522.PCD_Init();		// Init MFRC522
	delay(4);				// Optional delay. Some board do need more time after init to be ready, see Readme
	mfrc522.PCD_DumpVersionToSerial();	// Show details of PCD - MFRC522 Card Reader details
	pinMode(BUTTON,INPUT);
  pinMode(RED,OUTPUT);
  pinMode(GREEN,OUTPUT);
  pinMode(BLUE,OUTPUT);
  analogWrite(RED,225);
  analogWrite(GREEN,225);
  analogWrite(BLUE,255);
  pre_state=LOW;
  registerMode=LOW;
	ledOn=false,blinkRed=false,blinkBlue=false;
	prevTime=0;
	blinkcnt=6;
	Serial.println(F("Scan PICC to see UID, SAK, type, and data blocks..."));
}
void resetBlink() {//중간에 led가 바꼈을 때 이전 led 상태에 대한 정보를 초기화
    blinkRed = false;
    blinkBlue = false;
    blinkcnt = 0;
		ledOn=false;
}
void RedOn(){
	analogWrite(RED, 255);
  analogWrite(GREEN, 0);
  analogWrite(BLUE, 0);
}
void BlueOn(){
	analogWrite(RED, 0);
  analogWrite(GREEN, 0);
  analogWrite(BLUE, 255);
}
void YellowOn(){
		analogWrite(RED,225);
    analogWrite(GREEN,225);
    analogWrite(BLUE,0);
}
void WhiteOn(){
	analogWrite(RED,225);
    analogWrite(GREEN,225);
    analogWrite(BLUE,225);
}
void ledOFF(){
		analogWrite(RED, 0);
  analogWrite(GREEN, 0);
  analogWrite(BLUE, 0);
}
bool isRegistered(const byte *uid){
		for(int i=0;i<tag_list.getSize();i++){
			if(memcmp(tag_list.get(i).uidByte,uid,4)==0){	
				return true;
			}
		}
		return false;
}
void loop() {
	// Reset the loop if no new card present on the sensor/reader. This saves the entire process when idle.

	int input=digitalRead(BUTTON);
  if(input==HIGH && pre_state==LOW){    //버튼이 눌리면
    registerMode=registerMode==1 ? 0 : 1;
  }
	pre_state=input;

	if(!registerMode && blinkRed){
		if (millis() - prevTime >= 500) {
				Serial.println(blinkcnt);
        prevTime = millis();
        ledOn = !ledOn;

        if (ledOn) {
            RedOn();
        }
				else {
            ledOFF();
        }
				blinkcnt--;
				if(blinkcnt==0){
					blinkRed=false;
				}
    }
	}
	else if(!registerMode && blinkBlue){
		if (millis() - prevTime >= 500) {
        prevTime = millis();
        ledOn = !ledOn;

        if (ledOn) {
            BlueOn();
        } else {
            ledOFF();
        }
				blinkcnt--;
				if(blinkcnt==0){
					blinkBlue=false;
				}
    }
	}
	//led가 깜빡이는 동안 다른 색이 켜지지 않기 위해 else if문으로 제어
	else if(registerMode){
		YellowOn();
	}
	else{
		WhiteOn();
	}
	
	if ( ! mfrc522.PICC_IsNewCardPresent()) {
		return;
	}
	// Select one of the cards
	if ( ! mfrc522.PICC_ReadCardSerial()) {
		return;
	}

  if(registerMode){   //등록 모드
		Serial.print("Read UID Tag : ");
		for (byte i=0;i<mfrc522.uid.size;i++){
			Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0": " ");
			Serial.print(mfrc522.uid.uidByte[i],HEX);
		}
		Serial.println();
		if(!isRegistered(mfrc522.uid.uidByte)){		//아직 등록되지 않은 id일때만 등록
			tag_list.addLast(mfrc522.uid);
		}
  }
  else{		//인식 모드
		if(!isRegistered(mfrc522.uid.uidByte)){ //등록되지 않았을 때-->led red x 3
			resetBlink();
			Serial.println("등록되지 않은 카드 입니다!");
			blinkRed=true;
			blinkcnt=6;
    }

		else{		// 등록된 카드--> led blue x 3
			resetBlink();
			Serial.println("등록된 카드 입니다!");
			blinkBlue=true;
			blinkcnt=6;
		}
    
  }
	delay(100);
}
