#include <IBusBM.h>


IBusBM IBus; // IBus object

void ibus_setup() {
  // Serial.begin(115200);   // remove comment from this line if you change the Serial port in the next line

  IBus.begin(Serial3);    // iBUS connected to Serial0 - change to Serial1 or Serial2 port when required


  Serial.println("Start IBus2PWM");
}   


void ibus_loop() {

  
  // Getting values form all channel
  for (int i = 0; i <= 8 ; i++)
  {
    channel_data[i] = IBus.readChannel(i); // get latest value for servo channel 1
   Serial.print(channel_data[i]);
    //Serial.print(Serial3.available());
   Serial.print(" ");
  }

  //--------------------Sterring input mapping ------------------------------
     if (channel_data[0] <= 2000 && channel_data[0] >= 1510) {
      sterring_value = map(channel_data[0], 1500, 2000 , 530, 860);
    }
      else if (channel_data[0] <= 1490 && channel_data[0] >= 1000) {
      sterring_value = map(channel_data[0], 1000, 1500 , 200 , 530);
    }
    else{
      sterring_value =530;
    }

// arduino has 8 bit resolution  0 ~ 0V  255 ~ 5V
// max throttle pwm value = 147 , min throttle pwm value = 40 fowrward
// max throttle pwm value = -147 , min throttle pwm value = -40 reverse
// max sterring_value pwm value = 120 , min brake pwm value = 0  right
// max sterring_value pwm value = -120 , min brake pwm value = 0  left

  //-------------------------Throttle---------------------
    if (channel_data[2] <= 2000 && channel_data[2] >= 1000) {
      throttle = map(channel_data[2], 1000, 2000 , initial_throttle , max_limit);
     // throttle = map(channel_data[1], 1600, 2000 , initial_throttle  , max_limit);
    }
    else{
      throttle=initial_throttle;
    }

        if (channel_data[6] == 2000) {
          max_limit = 190;
        }
        else{
          max_limit = 125;
        }
 



  //-------------------------Drive Mode---------------------
    if (channel_data[5] == 2000) {
      Drive_mode ='R';
    }
    else if(channel_data[5] == 1500){
      Drive_mode ='F';
    }
    else{
      Drive_mode ='N';
    }

    //  all lights
    if (channel_data[9] == 2000) {
       digitalWrite(all_light_pin, HIGH);
    }
    else
    {
       digitalWrite(all_light_pin, LOW);
    }

    // side lights
    if (channel_data[9] >= 1600) {
       digitalWrite(side_light_pin[0], HIGH);
       digitalWrite(side_light_pin[1], LOW);

    }
    else if(channel_data[9] <= 1400 )
    {
       digitalWrite(side_light_pin[1], HIGH);
       digitalWrite(side_light_pin[0], LOW);

    }
    else{
       digitalWrite(side_light_pin[0], LOW);
       digitalWrite(side_light_pin[1], LOW);
    }




  //-------------------------Brake---------------------
    if (channel_data[4] <= 1500 && channel_data[4] >= 1000) {
      Brake = map(channel_data[4], 1500, 1000 , 0 , 5000);
    }
    else{
      Brake = 0;
    }
    if(channel_data[4] <= 2000 && channel_data[4] >= 1500){
      value_brake = map(channel_data[4], 1500, 2000 , 0 , 250);
    }
    else{
      value_brake = 0;
    }




  delay(10);
}
