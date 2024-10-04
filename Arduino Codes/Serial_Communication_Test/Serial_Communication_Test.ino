// This code is used to ensure Serial Communication between the Arduino and Python script by sending dummy data over Serial COM Port
int i = 0;
int x = 0;
char userInput;
void setup() {
  Serial.begin(115200);
}
bool flag = false;
const byte numChars = 80;
char receivedChars[numChars];
void loop(){
  if (Serial.available() > 0) {

    userInput = Serial.read();               // read user input

    if (userInput == 'g') {
      String string = "";
      string += String(random(10, 80)) + '.' + String(random(0, 75));
      string += '|';

      string += String(1000.125);
      string += '|';

      string += String(1000.128);
      string += '|';

      string += String(1000.58);
      string += '|';

      string += String(1000.577);
      string += '|';

      string += String(1000.67);
      string += '|';

      string += String(1);
      string += '|';
      string += String(1);
      string += '|';
      string += String(1);
      string += '|';
      string += String(x);
      string += '|';
      Serial.println(string);
      x++;
    }
  }
}
