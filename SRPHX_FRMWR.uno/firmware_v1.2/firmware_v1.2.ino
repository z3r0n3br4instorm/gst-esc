//Zerone Laboratories - Designed for ztCC STARGATE Hardware Control Unit
#include <LiquidCrystal_I2C.h>
#include <Firmata.h>

LiquidCrystal_I2C lcd(0x27,20,4);  // set the LCD address to 0x27 for a 16 chars and 2 line display
int time = 2500;
int lastline = 1;
void stringDataCallback(char *stringData){
  if (lastline){
    lastline = 0;
    lcd.clear();
  } else {
    lastline = 1;
    lcd.setCursor(0,1);
  }
   if (strcmp(stringData, "sublight.on")==0){
    digitalWrite (8,LOW);
    }else if(strcmp(stringData, "sublight.off")==0){
    digitalWrite(8, HIGH);
    }else if(strcmp(stringData, "lightsys.off")==0){
      digitalWrite(9, HIGH);
    }else if(strcmp(stringData, "lightsys.on")==0){
      digitalWrite(9,LOW);
    }else if(strcmp(stringData,"fan.on")==0){
      digitalWrite(10,LOW);
    }else if(strcmp(stringData,"fan.off")==0){
      digitalWrite(10,HIGH);
    }else if(strcmp(stringData,"gpucool.on")==0){
      digitalWrite(11,LOW);
    }else if(strcmp(stringData,"gpucool.off")==0){
      digitalWrite(11,HIGH);
    }else if(strcmp(stringData,"sys.shutdown")==0){
      lcd.clear();
      lcd.setCursor(0,0);
      lcd.print("System Shutdown");
      lcd.setCursor(0,1);
      lcd.print("Sequance Running");
      delay(10000);
    }else if(strcmp(stringData,"chaos")==0){
        lcd.clear();
        lcd.print("CHAOS");
        for(int i = 0; i > -1; i++){
            digitalWrite(8,LOW);
            delay(100);
            digitalWrite(9,LOW);
            delay(100);
            digitalWrite(9,HIGH);
            delay(100);
            digitalWrite(8,HIGH);
            delay(100);
            digitalWrite(9,LOW);
            delay(100);
          }
    }else if(strcmp(stringData,"hardware.test")==0){
      //hardware systems testing sequance
              digitalWrite(8,HIGH);
              digitalWrite(9,HIGH);
              digitalWrite(10,HIGH);
              digitalWrite(11,HIGH);
              delay(time);
              lcd.clear();
              digitalWrite(8,LOW);
              digitalWrite(9,HIGH);
              lcd.setCursor(0,0);
              lcd.print("ztCC_M1");
              lcd.setCursor(0, 1);
              lcd.print("CntrlCmpterMARK1");
              digitalWrite(8,HIGH);
              delay(time);
              lcd.clear();
              digitalWrite(8,LOW);
              lcd.setCursor(0,0);
              lcd.print("CTRLCMPTBCKLT");
              lcd.setCursor(0,1);
              lcd.print(1,0);
              lcd.print("TESTING");
              digitalWrite(8,LOW);
              delay(time);
              lcd.clear();
              lcd.setCursor(0,0);
              lcd.print("LIGHT_SYS");
              lcd.setCursor(0,1);
              lcd.print(1,0);
              lcd.print("TESTING");
              digitalWrite(9,LOW);
              delay(time);
                  lcd.clear();
              lcd.setCursor(0,0);
              lcd.print("ROOM_FAN");
              lcd.setCursor(0,1);
              lcd.print(1,0);
              lcd.print("TESTING");
              digitalWrite(10,LOW);
              delay(time);
                      lcd.clear();
              lcd.setCursor(0,0);
              lcd.print("GPU_STABILIZER");
              lcd.setCursor(0,1);
              lcd.print(1,0);
              lcd.print("TESTING");
              digitalWrite(11,LOW);
              delay(time);
                  lcd.clear();
              lcd.setCursor(0,0);
              lcd.print("TURNING ALL");
              lcd.setCursor(0,1);
              lcd.print(1,0);
              lcd.print("SYSTEMS OFFLINE");
              digitalWrite(8,HIGH);
              digitalWrite(9,HIGH);
              digitalWrite(10,HIGH);
              digitalWrite(11,HIGH);
              delay(time);
                  lcd.clear();
                  lcd.setCursor(0,0);
              lcd.print("TURNING LIGHTSYS");
              lcd.setCursor(0,1);
              lcd.print(1,0);
              lcd.print("ONLINE");
              digitalWrite(9,LOW);
              delay(time);
          
    }
  lcd.print(stringData);
}
void setup()
{
  //HARDWARE_CONTROLLER_PINS_DEFINE
pinMode(8,OUTPUT);
pinMode(9,OUTPUT);
pinMode(10,OUTPUT);
pinMode(11,OUTPUT);
digitalWrite(11,HIGH);
  lcd.init();                      // initialize the lcd 
  lcd.backlight();
  Firmata.setFirmwareVersion( FIRMATA_MAJOR_VERSION, FIRMATA_MINOR_VERSION);
  Firmata.attach( STRING_DATA, stringDataCallback);
  Firmata.begin();
    lcd.setCursor(0,0);
    lcd.print("Zerone tech");
    lcd.setCursor(0,1);
    lcd.print("Central Computer");
    delay(200);

    digitalWrite(11,HIGH);
        lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("WAITING FOR");
    lcd.setCursor(0,1);
    lcd.print("ztOS C.O.R.E...");
    delay(time);
}


void loop()
{ 
  while (Firmata.available()) {
    Firmata.processInput();
  }

}
