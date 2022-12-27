#include <IBusBM.h>

int channel_data[10] = {0,0,0,0,0,0,0,0,0,0};

IBusBM IBus; // IBus object

void ibus_setup() {
  // Serial.begin(115200);   // remove comment from this line if you change the Serial port in the next line

  IBus.begin(Serial2);    // iBUS connected to Serial0 - change to Serial1 or Serial2 port when required

  Serial.println("Start IBus2PWM");
}


void ibus_loop() {
  // Getting values form all channel
  for (int i = 0; i <= 5 ; i++)
  {
    channel_data[i] = IBus.readChannel(i); // get latest value for servo channel 1
   Serial.print(channel_data[i]);
   Serial.print(" ");
  }
  //--------------------Sterring input mapping ------------------------------
     if (channel_data[0] <= 2000 && channel_data[0] >= 1510) {
      sterring_value = map(channel_data[0], 1500, 2000 , 1920 , 3000);//3200
    }
      else if (channel_data[0] <= 1490 && channel_data[0] >= 1000) {
      sterring_value = map(channel_data[0], 1000, 1500 , 900 , 1920);//700
    }
    else{
      sterring_value =1920;
    }







}
