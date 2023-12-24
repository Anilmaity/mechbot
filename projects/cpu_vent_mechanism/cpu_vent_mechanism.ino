#include <Wire.h>

#define MIN_TEMPERATURE 50
#define MAX_TEMPERATURE 100
#define MIN_ANGLE -90
#define MAX_ANGLE 0

// temperature sensor setup
#define TEMP_SENSOR_PIN 3  // Digital Pin for Temperature Sensor ALSO Make sure to add exter pull pu resistor

#include <OneWire.h>
#include <DallasTemperature.h>
OneWire oneWire(TEMP_SENSOR_PIN);
DallasTemperature sensors(&oneWire);


int current_temperature = 0 ;
int angle = 0;


// servo setup
#include "PCA9685.h"
PCA9685 pwmController(Wire);
const int numServos = 12;
PCA9685_ServoEval servoList[numServos];



void setup(void)
{
  // Start serial communication for debugging purposes
  Serial.begin(115200);

  sensors.begin();
  servosetup();

  sensors.requestTemperatures();
  current_temperature = sensors.getTempCByIndex(0);

  delay(500);
  Serial.println("Setup completed");

}



void loop(void) {
  get_temperature();
  angle = map(current_temperature, MIN_TEMPERATURE, MAX_TEMPERATURE, MIN_ANGLE, MAX_ANGLE);

  if(current_temperature <  MIN_TEMPERATURE){
    angle = MIN_ANGLE;
  }
  else if(current_temperature > MAX_TEMPERATURE ){
    angle = MAX_ANGLE;
  }
  
  for (int i = 0 ; i <= 5; i++) {
    for (int j = 0; j < numServos; ++j) {
      pwmController.setChannelPWM(j, servoList[j].pwmForAngle(angle));
    }
    delay(100);
  }

  Serial.print("Celsius temperature: ");
  Serial.print(sensors.getTempCByIndex(0));
  Serial.print(" Current Servo Angle : ");
  Serial.println(angle);
}

void get_temperature(void) {
  sensors.requestTemperatures();
  current_temperature = sensors.getTempCByIndex(0);
  delay(500);
}


void servosetup() {
  Wire.begin();
  pwmController.resetDevices();  // Resets all PCA9685 devices on i2c line
  pwmController.init();          // Initializes module using default totem-pole driver mode, and default disabled phase balancer
  pwmController.setPWMFreqServo();  // 50Hz provides standard 20ms servo phase length


}
