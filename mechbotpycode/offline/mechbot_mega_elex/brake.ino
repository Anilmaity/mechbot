

void brake_setup()
{

  pinMode(B_DIR_pin[0], OUTPUT);
  pinMode(B_DIR_pin[1], OUTPUT);
  pinMode(B_PWM_pin[0], OUTPUT);
  pinMode(B_PWM_pin[1], OUTPUT);
  pinMode(B_ENC_A[0], INPUT_PULLUP);
  pinMode(B_ENC_B[0], INPUT_PULLUP);
  pinMode(B_ENC_A[1], INPUT_PULLUP);
  pinMode(B_ENC_B[1], INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(B_ENC_A[0]), decode_rotation_A_B0, RISING);
  attachInterrupt(digitalPinToInterrupt(B_ENC_B[0]), decode_rotation_B_B0, RISING);
  attachInterrupt(digitalPinToInterrupt(B_ENC_A[1]), decode_rotation_A_B1, RISING);
  attachInterrupt(digitalPinToInterrupt(B_ENC_B[1]), decode_rotation_B_B1, RISING);
  enable_encoder_0 = true;
  enable_encoder_1 = true;
}

void decode_rotation_A_B0() {
  int A = digitalRead(B_ENC_A[0]);
  int B = digitalRead(B_ENC_B[0]);


  if (A == 1 && B == 0) {
    B_Current_position_A[0] -= 1;

  }
  else if (A == 1 && B == 1) {
    B_Current_position_A[0] += 1;

  }
  Current_brake_position[0] = int((-B_Current_position_B[0] - B_Current_position_A[0]) / 2);


}
void decode_rotation_A_B1() {
  int A = digitalRead(B_ENC_A[1]);
  int  B = digitalRead(B_ENC_B[1]);


  if (A == 1 && B == 0) {
    B_Current_position_A[1] += 1;

  }
  else if (A == 1 && B == 1) {
    B_Current_position_A[1] -= 1;

  }
  Current_brake_position[1] = int((B_Current_position_B[1] + B_Current_position_A[1]) / 2);


}


void decode_rotation_B_B1() {
  int A = digitalRead(B_ENC_A[1]);
  int  B = digitalRead(B_ENC_B[1]);


  if (A == 0 && B == 1) {
    B_Current_position_B[1] -= 1;

  }
  else if (A == 1 && B == 1) {
    B_Current_position_B[1] += 1;

  }
  Current_brake_position[1] = int((B_Current_position_B[1] + B_Current_position_A[1]) / 2);


}

void decode_rotation_B_B0() {
  int A = digitalRead(B_ENC_A[0]);
  int  B = digitalRead(B_ENC_B[0]);


  if (A == 0 && B == 1) {
    B_Current_position_B[0] += 1;

  }
  else if (A == 1 && B == 1) {
    B_Current_position_B[0] -= 1;

  }
  Current_brake_position[0] = int((-B_Current_position_B[0] - B_Current_position_A[0]) / 2);


}

void braking() {

    if (abs(Brake) > 200)
      {
        digitalWrite(Brake_pin, LOW);
        digitalWrite(back_light_pin, LOW);

      }
      else {
        digitalWrite(Brake_pin, HIGH);
        digitalWrite(back_light_pin, HIGH);


      }

      B_position_error[0] = Brake - Current_brake_position[0];
      B_position_error[1] = Brake - Current_brake_position[1];


      if (B_position_error[0] > 50) {
        analogWrite(B_PWM_pin[0], 250);
        digitalWrite(B_DIR_pin[0], HIGH);

      }
      else if ((B_position_error[0] < -50)) {
        analogWrite(B_PWM_pin[0], 250);
        digitalWrite(B_DIR_pin[0], LOW);
      }
      else {
        analogWrite(B_PWM_pin[0], 0);

      }


      if (B_position_error[1] > 50) {
        analogWrite(B_PWM_pin[1], 250);
        digitalWrite(B_DIR_pin[1], LOW);

      }
      else if (B_position_error[1] < -50) {
        digitalWrite(B_DIR_pin[1], HIGH);
        analogWrite(B_PWM_pin[1], 250);
      }
      else {
        analogWrite(B_PWM_pin[1], 0);
      }
    }
