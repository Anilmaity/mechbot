int DIR_pin = 2;
int PWM_pin =3;
int ENC_A = 9;
int ENC_B =6;

int current_position =0; 
int position_error = 0;
void motor_setup()
{
  
  pinMode(DIR_pin,OUTPUT);
  pinMode(PWM_pin,OUTPUT);
  pinMode(ENC_A, INPUT_PULLUP);
  pinMode(ENC_B, INPUT_PULLUP);

  attachInterrupt(ENC_A, decode_rotation, RISING); 
   
}

void motor_loop()
{
  position_error = Sterring_input - current_position;
  
  if(position_error > 10){
    analogWrite(PWM_pin , 50);
    digitalWrite(DIR_pin, HIGH);
  }
  else if(position_error < -10){
    analogWrite(PWM_pin , 50);
    digitalWrite(DIR_pin, LOW);
  }

 
}

void decode_rotation(){
  int A = digitalRead(ENC_A);
  int B = digitalRead(ENC_B);

if(A == 1 && B ==0){
  current_position +=1;
  
}
else if(A == 1 && B ==1){
    current_position -=1;

}
  
}