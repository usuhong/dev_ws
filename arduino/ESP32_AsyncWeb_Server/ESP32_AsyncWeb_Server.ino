#include <WiFi.h>
#include <AsyncTCP.h>
#include <ESPAsyncWebServer.h>
#include <ESP32Servo.h>

Servo servo;

const char *ssid="addinedu_201class_2-2.4G";
const char *pw="201class2!";


AsyncWebServer server(80);
const char *INPUT_PARAM1="degree";

const char html[] PROGMEM= R"rawliteral(
<!DOCTYPE html>
<html>
  <body>
    <center>
      <h1>Hello, ESP32 Async Web Server!</h1>
      <form action="/get">
        Servo Degree:
        <input type="text" name="degree">
        <input type="submit" value="Submit">
    </form>
    <div>
        Phtoresistor:
        <div id="sensor">None</div>
    </div>
    <center>
        <script>
            setInterval(updateSesnorValue,100);
            function updateSesnorValue(){
                var xhttp= new XMLHttpRequest();
                xhttp.onreadystatechange=function(){
                if(this.readyState==4 && this.status==200){
                    document.getElementById("sensor").innerHTML=this.responseText;
                }
            };
            xhttp.open("GET","/sensor",true);
            xhttp.send();
            }
        </script>
  </body>
</html>
)rawliteral";

String processor(const String& var){

  Serial.println(var);
  return var;
}

void setup() {
  
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

  server.on("/get",HTTP_GET, [] (AsyncWebServerRequest *req){
    String inputMessage=req->getParam(INPUT_PARAM1)->value();
    Serial.println(inputMessage);
    float degree=inputMessage.toFloat();
    servo.write(degree);
    req->send_P(200,"text_html",html,processor);
  });

  server.on("/sensor",HTTP_GET ,[](AsyncWebServerRequest *req){
    int sensor=analogRead(34);
    String value=String(sensor);
    Serial.println(value);
    req->send(200,"text/plain",value);
  });

  server.begin();

  Serial.println("HTTP Server Started!");
  delay(100);

}

void loop() {


}
