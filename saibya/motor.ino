
void motor_setup() {
  

  //TCCR0B = TCCR0B & B11111000 | B00000001; // for PWM frequency of 31372.55 Hz
  TCCR1B = TCCR1B & B11111000 | B00000001; // for PWM frequency of 31372.55 Hz
  TCCR2B = TCCR2B & B11111000 | B00000001; // for PWM frequency of 31372.55 Hz
  TCCR3B = TCCR3B & B11111000 | B00000001; // for PWM frequency of 31372.55 Hz
  TCCR4B = TCCR4B & B11111000 | B00000001; // for PWM frequency of 31372.55 Hz
  TCCR5B = TCCR5B & B11111000 | B00000001; // for PWM frequency of 31372.55 Hz




  pinMode(M1_DIR, OUTPUT);
  pinMode(M1_PWM, OUTPUT);
  pinMode(M2_DIR, OUTPUT);
  pinMode(M2_PWM, OUTPUT);
  pinMode(M3_DIR, OUTPUT);
  pinMode(M3_PWM, OUTPUT);
  pinMode(M4_DIR, OUTPUT);
  pinMode(M4_PWM, OUTPUT);
}



void move_bot() {
  motor1_speed = bot_speed + bot_direction;
  motor2_speed = bot_speed - bot_direction;

  motor1_speed = constrain(motor1_speed, -255, 255);
  motor2_speed = constrain(motor2_speed, -255, 255);

  if (abs(motor1_speed) > 10) {

    if (motor1_speed > 0) {

      analogWrite(M1_DIR, 255);
      analogWrite(M3_DIR, 0);

    } else {

      analogWrite(M1_DIR, 0);
      analogWrite(M3_DIR, 255);
    }


    analogWrite(M1_PWM, abs(motor1_speed));
    analogWrite(M3_PWM, abs(motor1_speed));

  } else {

    analogWrite(M1_PWM ,0);
    analogWrite(M3_PWM ,0);
  }



  if (abs(motor2_speed) > 10) {

    if (motor2_speed > 0) {

      analogWrite(M2_DIR, 255);
      analogWrite(M4_DIR, 0);

    } else {

      analogWrite(M2_DIR, 0);
      analogWrite(M4_DIR, 255);
    }  

   analogWrite(M2_PWM, abs(motor2_speed));
   analogWrite(M4_PWM, abs(motor2_speed));

  }
 else {

    analogWrite(M2_PWM ,0);
    analogWrite(M4_PWM ,0);
  }

}