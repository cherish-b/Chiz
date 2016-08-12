#include <Servo.h>

Servo Right;
Servo Left;

void setup() {
  // put your setup code here, to run once:
Left.attach(13);
Right.attach(12);
Left.writeMicroseconds(1500);
Right.writeMicroseconds(1500);
}

void cw()
{
Left.writeMicroseconds(1300); 
}

void ccw()
{
Right.writeMicroseconds(1700);
}
void fwd()
{
cw();
ccw();
}

void bwkd()
{
 Left.writeMicroseconds(1700);
 Right.writeMicroseconds(1300);
}
void lefty(){
  Left.writeMicroseconds(1700);
}
void righty(){
  Right.writeMicroseconds(1300);
}
void loop() {
  // put your main code here, to run repeatedly:
fwd();
delay(3000);
bwkd();
delay(3000);
lefty();
delay(3000);
righty();
delay(3000);


}
