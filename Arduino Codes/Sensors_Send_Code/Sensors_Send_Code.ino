#include "max6675.h"

char userInput;
int tcCLK[]  = {10, 8, 42, 47, 34, 46};
int tcSO[]  = {11, 9, 40, 48, 32, 44};
int tcCS[]  = {28, 22, 26, 27, 24, 23};
int vibrationSensorPins[4] = {2, 4, 3, 5};
const int PIEZO_PIN = A0; // Piezo output
MAX6675 thermocouple[] = {
  MAX6675(tcCLK[0], tcCS[0], tcSO[0]),
  MAX6675(tcCLK[1], tcCS[1], tcSO[1]),
  MAX6675(tcCLK[2], tcCS[2], tcSO[2]),
  MAX6675(tcCLK[3], tcCS[3], tcSO[3]),
  MAX6675(tcCLK[4], tcCS[4], tcSO[4]),
  MAX6675(tcCLK[5], tcCS[5], tcSO[5]),
};

float temps[6] = {0};
void setup() {

  Serial.begin(115200);

  for (int i = 0; i < 4; i++) {
    pinMode(vibrationSensorPins[i], INPUT);
  }
}

void loop() {
  if (Serial.available() > 0) {

    userInput = Serial.read();               // read user input

    if (userInput == 'g') { 
      String string = "";
      for (int cs = 0; cs < 6; cs++) {
        if ((thermocouple[cs].readCelsius() == thermocouple[cs].readCelsius()) && thermocouple[cs].readCelsius() != 0.0)
          temps[cs] = thermocouple[cs].readCelsius();
      }
      for (int i = 0; i < 6; i++) {
        string += String(temps[i]);
        string += '|';
      }
      for (int i = 0; i < 4; ++i) {
        int vibrationSensorState = digitalRead(vibrationSensorPins[i]);
        string += String(vibrationSensorState);
        string += '|';
      }

      int piezoADC = analogRead(PIEZO_PIN);
      string += String(piezoADC);
      string += '|';
      Serial.println(string);
    }
  }
}
