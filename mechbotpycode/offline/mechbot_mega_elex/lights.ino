void drive_mode(){

  if(Drive_mode== 'N'){

        digitalWrite(Neutral_pin,HIGH);
            digitalWrite(Reverse_pin,LOW);
  }
  else if(Drive_mode == 'F'){
        digitalWrite(Neutral_pin,HIGH);
            digitalWrite(Reverse_pin,HIGH);


  }
  else{

    digitalWrite(Neutral_pin,LOW);
        digitalWrite(Reverse_pin,HIGH);


  }
}

void relay_setup(){
  pinMode(all_light_pin, OUTPUT);
  pinMode(back_light_pin, OUTPUT);
  pinMode(side_light_pin[0], OUTPUT);
  pinMode(side_light_pin[1], OUTPUT);


}
