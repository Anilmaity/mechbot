volatile int ch1[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
volatile int x[10];
volatile int ch[15];
int M1_DIR = 3;
int M1_PWM = 2;
int M2_DIR = 4;
int M2_PWM = 5;
int M3_DIR = 7;
int M3_PWM = 6;
int M4_DIR = 9;
int M4_PWM = 8;

int motor1_speed = 0;
int motor2_speed = 0;
int update_data = 0;

long int loopstart = 0;
long int loop_time = 0;
bool rc_connected = false;

int bot_speed = 0;
int bot_direction = 0;
long stop_time = 0;

volatile long int connection_time = 0;


void setup() {
  Serial.begin(115200);
  ppm_setup();
  motor_setup();
}

void loop() {
//   if(millis() - connection_time > 10000){
//   bot_speed = 0;
//   bot_direction = 0;
//   move_bot();

// }

}

void send_data() {
  Serial.print(" ");
  Serial.print(ch[1]);
  Serial.print(" ");
  Serial.print(ch[2]);
  Serial.print(" ");
  Serial.print(ch[3]);
  Serial.print(" ");
  Serial.print(ch[4]);
  Serial.print(" ");
  Serial.print(ch[5]);
  Serial.print("  .  ");
  // Serial.print(ch[8]);
  // Serial.print(" ");
  // Serial.print(ch[9]);
  // Serial.print(" ");
  // Serial.print(ch[10]);
  // Serial.print(" ");
  Serial.print(bot_speed);
  Serial.print(" ");
  Serial.print(bot_direction);
  Serial.print(" ");
   Serial.print(motor1_speed);
   Serial.print(" ");
   Serial.print(motor2_speed);
   Serial.print(" ");



  Serial.println();
}
