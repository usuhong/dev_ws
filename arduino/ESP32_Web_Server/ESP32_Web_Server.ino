#include <WiFi.h>
#include<WebServer.h>
#include<ESP32Servo.h>



const char *ssid="addinedu_201class_2-2.4G";
const char *pw="201class2!";
const int LED_BUILTIN=2;

WebServer server(80);
void handle_root();

const char html[] PROGMEM= R"rawliteral(
<!DOCTYPE html>
<html>
  <body>
    <center>
      <h1>Hello, ESP32 Web Server!</h1>
      <a href="on"><button>LED ON</button></a>
      <a href="off"><button>LED OFF</button></a>
    <center>
  </body>
</html>
)rawliteral";

void handle_root(){
  server.send(200,"text/html",html);
}

void ledOn(){
  Serial.println("On");
  digitalWrite(LED_BUILTIN,HIGH);
  server.send(200,"text/html",html);
}

void ledOff(){
  Serial.println("Off");
  digitalWrite(LED_BUILTIN,LOW);
  server.send(200,"text/html",html);
}

void setup() {
  pinMode(LED_BUILTIN,OUTPUT);

  Serial.begin(115200);
  Serial.println("ESP32 Web Server Start");
  Serial.println(ssid);

  WiFi.begin(ssid,pw);

  while(WiFi.status() != WL_CONNECTED){
    delay(1000);
    Serial.println(".");
  }
  Serial.println();


  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  server.on("/",handle_root);
  server.on("/on",HTTP_GET,ledOn);
  server.on("/off",HTTP_GET,ledOff);

  server.begin();

  Serial.println("HTTP Server Started!");
  delay(100);

}

void loop() {
  server.handleClient();

}
