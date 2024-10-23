
//specifing  arrays and variables to store values
long int a = 0;
long int b = 0;
long int c = 0;
int i = 0;
int rc_pin = 21;


void ppm_setup() {
  pinMode(rc_pin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(rc_pin), read_me, FALLING);
  // enabling interrupt at pin 2
}


void read_me() {

  a = micros();  //store time value a when pin value falling
  c = a - b;     //calculating  time inbetween two peaks
  b = a;         //
  x[i] = c;      //storing 15 value in  array
  i = i + 1;
  if (i == 15) {
    for (int j = 0; j < 15; j++) {
      if (x[j] > 0) {
        ch1[j] = x[j];
      }
    }
    read_rc();
    i = 0;
  }
}


void read_rc() {
  int i, j, k = 0;
  for (k = 14; k > -1; k--) {
    if (ch1[k] > 5500) { j = k; }
  }  //detecting separation  space 10000us in that another array
  for (i = 1; i <= 14 - j; i++) {
    if (ch1[i + j] >= 900 && ch1[i + j] <= 2100) {
      ch[i] = ch1[i + j];
    }
  }
  evaluteinputs();
  send_data();
  move_bot();
  connection_time = millis();

}






void evaluteinputs() {
  int speed = 0;
  if (ch[5] >= 1600) {
    if (ch[3] <= 2100 && ch[3] >= 1520) {
      speed = map(ch[3], 1500, 2000, 0, 255);
    } else if (ch[3] <= 1480 && ch[3] >= 900) {
      speed = map(ch[3], 1000, 1500, -255, 0);
    } else {
      speed = 0;
    }
    bot_speed = 0.3 * bot_speed + 0.7 * (speed);

    int direction = 0;

    if (ch[1] <= 2100 && ch[1] >= 1510) {
      direction = map(ch[1], 1500, 2000, 0, -255);
    } else if (ch[1] <= 1490 && ch[1] >= 900) {
      direction = map(ch[1], 1000, 1500, 255, 0);
    } else {
      direction = 0;
    }
    bot_direction = 0.3 * bot_direction + 0.7 * direction;
    stop_time = millis();
  }
  else {
    if (millis() - stop_time > 500) {
      bot_direction = 0;
      bot_speed = 0;
    }
  }
}
