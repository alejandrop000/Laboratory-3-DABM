int led = 10;
int ldr;


void setup() {
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  }

void loop() {
  ldr = analogRead(A0);
  Serial.println(ldr);

  if(Serial.available() > 0){
      int x = Serial.read();
      analogWrite(led, x);
  }
}
