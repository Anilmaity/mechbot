
  int S_DIR = 12;
  int S_PWM = 13;
  long int sterring_value = 1920;
  long int error =0;
  
  void setup() {
  // initialize serial communication at 115200 bits per second:
  Serial.begin(115200);
  ibus_setup();
  //set the resolution to 12 bits (0-4096)
  analogReadResolution(12);
  pinMode(S_DIR,OUTPUT);
  pinMode(S_PWM,OUTPUT);

  }

void loop() {
  // read the analog / millivolts value for pin 2:
  int analogValue = analogRead(2);
  int analogVolts = analogReadMilliVolts(2);
  int error = 0;

  ibus_loop();
  error = 0.3*(sterring_value -  analogValue)+0.7*error;

  // print out the values you read:
  Serial.println("Sensor Val = "+String(analogValue)+". Input Value = "+String(sterring_value) + " error " + String(error));
  // print out the values you read:
  if(abs(error)> 20){
if(error>0)
{
  digitalWrite(S_DIR,LOW);
  digitalWrite(S_PWM,HIGH);
}
else{

  digitalWrite(S_DIR,HIGH);
  digitalWrite(S_PWM,HIGH);
}

  }
else{
  digitalWrite(S_PWM,LOW);
}

  
  delay(2);  // delay in between reads for clear read from serial
}
