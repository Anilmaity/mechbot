#include "FastLED.h"
#define NUM_LEDS 60   
#define DATA_PIN 35
               
CRGB leds[NUM_LEDS];


char Drive_mode = 'N';
//------------------------------------
int Neutral_pin = 24;
int Reverse_pin =26;
int Brake_pin = 22;

int channel_data[10] = {0,0,0,0,0,0,0,0,0,0};

int Current_position_A =0;
int Current_position_B =0;
int Current_position = 0;

bool M_D_connected = true;
bool flysky_connected = true; 
long int Current_Speed;
long int loopstart = 0;
long int loop_time = 0;
long int motor_driver_start_time = 0;
long int Sterring_input = 0;

int throttle_pin = 3;
int throttle= 0;


// Variables for brake
int B_DIR_pin[2] = {7,9};
int B_PWM_pin[2] = {6,8};
int B_ENC_A[2] = {19,21};
int B_ENC_B[2] = {18,20};
int B_position_error[2] = {0,0};
int Brake_Speed = 0;
float B_Current_position_B[2] = {0,0};
float B_Current_position_A[2] = {0,0};
int Current_brake_position[2] = {0,0};
int enable_encoder_0 = false;
int enable_encoder_1 = false;
bool enable_encoder = true;
int Brake = 0;
int value_brake = 0;


//-----------------Lights----------------
int all_light_pin = 28;
int back_light_pin= 30;
int side_light_pin[2] = {32,34};

char Head_light_mode = 'L';
char left_side_light = 'N';
char right_side_light = 'F';
char back_light = 'F';
bool drive_mode_change = false;
char previous_drive_mode = 'N';
long int neutral_light_start = 0;
float value = 0;
bool fadding = true;

// sterring_value
int S_DIR = 5;
int S_PWM = 4;
int S_SEN = A0;
long int sterring_value = 512;
long int error =0;
long int sensorValue = 0;


// throttle
int initial_throttle = 36;
int max_limit = 147;


void setup(){
           
   Serial.begin(115200);
   Serial3.setTimeout(100);
   pinMode(Neutral_pin, OUTPUT);
   pinMode(Reverse_pin, OUTPUT);
   pinMode(Brake_pin, OUTPUT);
   digitalWrite(Brake_pin,HIGH);
   throttle_setup();
   brake_setup();
   ibus_setup();
   sterring_setup();
  //  light_setup();
   
   
  
}
void send_data(){
  Serial.print("@@#"+String(throttle)+"#"+String(Brake)+"#"+String(Drive_mode)
  +"#"+String(Current_brake_position[0])+" @ "+String(Current_position)+" @ "+String(Current_brake_position[1])+" #"+String(flysky_connected)
  +"#"+String(M_D_connected)+"#"+String(loop_time)+" "+String(Serial3.available())+" "+String(sterring_value)+" "+String(sensorValue)+" "+"#@@");
  Serial.println();
  
//   Serial.println(String(B_Current_position_B[0])+"  "+String(B_Current_position_B[1])+"   "+String(B_Current_position_A[0])+"   "+String(B_Current_position_A[1])+"  "+String(Current_position_B)+" "+ String(Current_position_A));

}

void loop(){
loopstart = millis();
ibus_loop();
braking();
drive_mode();
send_data();
throttling();
sterring_loop();
throttling();
// lights();

loop_time = millis() - loopstart;
}
