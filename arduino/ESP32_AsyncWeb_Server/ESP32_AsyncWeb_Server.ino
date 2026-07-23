#include <WiFi.h>
#include <AsyncTCP.h>
#include <ESPAsyncWebServer.h>


const char *ssid="addinedu_201class_2-2.4G";
const char *pw="201class2!";
const int LED1=21,LED2=22,LED3=23;

AsyncWebServer server(80);

const char html[] PROGMEM= R"rawliteral(
<!DOCTYPE html>
<html>
  <body>
    <center>
      <h1>Hello, ESP32 Async Web Server!</h1>
      <div> LED 21: <input type="checkbox" onchange="setLED(this, 1)" /></div>
      <div> LED 22: <input type="checkbox" onchange="setLED(this, 2)" /></div>
      <div> LED 23: <input type="checkbox" onchange="setLED(this, 3)" /></div>
      <script>
        function setLED(element, no){
            var req=new XMLHttpRequest();
            if (element.checked){
                req.open("GET", "/on" + no.toString(), true);
            }
            else{
                req.open("GET", "/off" + no.toString(), true);
            }
            req.send()
        }
      </script>
    <center>
  </body>
</html>
)rawliteral";

String processor(const String& var){

  Serial.println(var);
  return var;
}

void setup() {
  
  pinMode(LED1,OUTPUT);
  pinMode(LED2,OUTPUT);
  pinMode(LED3,OUTPUT);
  servo.attach(5);

  Serial.begin(115200);
  Serial.println("ESP32 Async Web Server Start");
  Serial.println(ssid);

  WiFi.begin(ssid,pw);

  while(WiFi.status() != WL_CONNECTED){
    delay(1000);
    Serial.println(".");
  }
  Serial.println();


  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  server.on("/",HTTP_GET, [] (AsyncWebServerRequest *req){
    req->send_P(200,"text_html",html,processor);
  });

  //led1 on off
  server.on("/on1",HTTP_GET, [] (AsyncWebServerRequest *req){
    digitalWrite(LED1,HIGH);
    Serial.println("HIGH");
    req->send_P(200,"text_html",html,processor);
  });

  server.on("/off1",HTTP_GET, [] (AsyncWebServerRequest *req){
    digitalWrite(LED1,LOW);
    Serial.println("LOW");
    req->send_P(200,"text_html",html,processor);
  });

  // led2 on off
  server.on("/on2",HTTP_GET, [] (AsyncWebServerRequest *req){
    digitalWrite(LED2,HIGH);
    Serial.println("HIGH");
    req->send_P(200,"text_html",html,processor);
  });

  server.on("/off2",HTTP_GET, [] (AsyncWebServerRequest *req){
    digitalWrite(LED2,LOW);
    Serial.println("LOW");
    req->send_P(200,"text_html",html,processor);
  });

  // led3 on off
  server.on("/on3",HTTP_GET, [] (AsyncWebServerRequest *req){
    digitalWrite(LED3,HIGH);
    Serial.println("HIGH");
    req->send_P(200,"text_html",html,processor);
  });

  server.on("/off3",HTTP_GET, [] (AsyncWebServerRequest *req){
    digitalWrite(LED3,LOW);
    Serial.println("LOW");
    req->send_P(200,"text_html",html,processor);
  });

  server.begin();

  Serial.println("HTTP Server Started!");
  delay(100);

}

void loop() {


}
