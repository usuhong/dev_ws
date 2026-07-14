
#include <SPI.h>
#include <MFRC522.h>

const int RST_PIN = 9;
const int SS_PIN = 10;

MFRC522 rc522(SS_PIN,RST_PIN);
struct TagData{
  char name[16];
  long total;
  long payment;
};
void setup() {
  Serial.begin(9600);

  SPI.begin();
  rc522.PCD_Init();

  Serial.println("Start!");  
}
void toBytes(byte* buffer, int data, int offset=0){
  buffer[offset]=data & 0xFF;
  buffer[offset+1]=(data>>8) & 0xFF;
}

MFRC522::StatusCode checkAuth(int index, MFRC522::MIFARE_Key key){

  MFRC522::StatusCode status=rc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, index, &key, &(rc522.uid));
  if(status!=MFRC522::STATUS_OK){
    Serial.print("Autentication Failed: ");
    Serial.println(rc522.GetStatusCodeName(status));
  }
  return status;
}

MFRC522::StatusCode writeString(int index,MFRC522::MIFARE_Key key, String data){

  MFRC522::StatusCode status=checkAuth(index,key);
  if(status!=MFRC522::STATUS_OK){
      return status;
  }
  char buffer[16];
  memset(buffer,0x00,sizeof(buffer));
  data.toCharArray(buffer,data.length()+1);

  status=rc522.MIFARE_Write(index,(byte *)buffer,16);
  if(status!=MFRC522::STATUS_OK){
    Serial.print("Write Failed : ");
    Serial.println(rc522.GetStatusCodeName(status));
  }

  return status;
}
MFRC522::StatusCode writeTagData(int index,MFRC522::MIFARE_Key key, TagData data){

  MFRC522::StatusCode status=checkAuth(index,key);
  if(status!=MFRC522::STATUS_OK){
      return status;
  }

  byte buffer[32];
  memset(buffer,0x00,sizeof(buffer));
  memcpy(buffer,&data,sizeof(data));

  for(int i=0;i<2;i++){
    status=rc522.MIFARE_Write(index+i,buffer+(i*16),16);
    if(status!=MFRC522::STATUS_OK){
      Serial.print("Write Failed : ");
      Serial.print(rc522.GetStatusCodeName(status));
    }
  }

  return status;

}

MFRC522::StatusCode writeInteger(int index,MFRC522::MIFARE_Key key, int data){
  MFRC522::StatusCode status=checkAuth(index,key);
  if(status!=MFRC522::STATUS_OK){
    return status;
  }

  byte buffer[16];
  memset(buffer,0x00,sizeof(buffer));
  toBytes(buffer,data);
}
MFRC522::StatusCode readString(int index,MFRC522::MIFARE_Key key, String &data){

  MFRC522::StatusCode status=checkAuth(index,key);
  if(status!=MFRC522::STATUS_OK){
    return status;
  }
  byte buffer[18];
  byte length=18;
  memset(buffer,0x00,sizeof(buffer));

  status=rc522.MIFARE_Read(index,buffer,&length);
  if(status!=MFRC522::STATUS_OK){
    Serial.print("Read Failed : ");
    Serial.println(rc522.GetStatusCodeName(status));
  }
  else{

    data=String((char *)buffer);
  }

  return status;

}
MFRC522::StatusCode readTagData(int index,MFRC522::MIFARE_Key key, TagData &data){

  MFRC522::StatusCode status=checkAuth(index,key);
  if(status!=MFRC522::STATUS_OK){
    return status;
  }
  byte buffer[34];
  memset(buffer,0x00,sizeof(buffer));
  byte length=18;

  for(int i=0;i<2;i++){
    status=rc522.MIFARE_Read(index+i,buffer+(i*16),&length);
    if(status!=MFRC522::STATUS_OK){
      Serial.print("Read Failed : ");
      Serial.println(rc522.GetStatusCodeName(status));
    }
  }
  memcpy(&data,buffer,sizeof(data));
  return status;
}
void loop() {
  
  String cmd="";
  TagData t_data;
  String s_temp;
  if(Serial.available()>0){
  cmd = Serial.readStringUntil('\n');
}

  const int index=61;
  MFRC522::MIFARE_Key key;
  MFRC522::StatusCode status;

  for(int i=0;i<6;i++){
    key.keyByte[i]=0xFF;
  }

  if(cmd.length()>0){

    if(!rc522.PICC_IsNewCardPresent()){
      Serial.println("No card");
      return;
  }
  if(!rc522.PICC_ReadCardSerial()){
    return;
  }
    Serial.print("cmd=[");
    Serial.print(cmd);
    Serial.println("]");
    switch(cmd.charAt(0)){
      case 'w':
        Serial.println("write");
        switch (cmd.charAt(1)){
          case 's':
            Serial.println("string");
            status=writeString(60,key,"nomaefg");
            rc522.PICC_DumpToSerial(&(rc522.uid));
            break;
          case 'i':
            Serial.println("integer");
            status=writeInteger(61,key,32767);
            rc522.PICC_DumpToSerial(&(rc522.uid));
            break;
          case 't':
            Serial.println("struct");
            s_temp="nomaefg";
            s_temp.toCharArray(t_data.name,s_temp.length()+1);
            t_data.total=2147483647;
            t_data.payment=20000000;
            status=writeTagData(56,key,t_data);
            rc522.PICC_DumpToSerial(&(rc522.uid));
          default:
            Serial.println("unknown type");
            status=MFRC522::STATUS_ERROR;
            break;
      }
      case 'r':
      {
        Serial.println("read");
        String data;
        status=readString(index,key,data);
        Serial.println(data);
        break;
        }
      default:
        Serial.println("unknown");
        status=MFRC522::STATUS_ERROR;
        break;
    }
    if(status==MFRC522::STATUS_OK){
      Serial.println("success!");
    }
  }
  rc522.PICC_HaltA();
  rc522.PCD_StopCrypto1();
 
}
