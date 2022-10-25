#include <EEPROM.h>
 
int a;
 
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(115200);
   
  for (uint16_t i = 0; i < EEPROM.length(); ++i) {
    EEPROM.update(i, 0);
  }
   
  for (uint16_t i = 0; i < EEPROM.length(); ++i) {
    a+=EEPROM.read(i);
  }
 
  if (a == 0){
    Serial.println("EEPROM is null! The process was successfull!");
  } else if (a > 0) {
    Serial.println("EEPROM is not null, please upload the code again!");
  }
}
 
void loop() {
  if (a == 0){
    digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(1000);                       // wait for a second
    digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
    delay(1000);
  }
}