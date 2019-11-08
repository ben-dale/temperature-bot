#include <LiquidCrystal.h>

/**
 * https://en.wikipedia.org/wiki/Steinhart%E2%80%93Hart_equation
 */
const int THERMISTOR_PIN = 0;
const float KNOWN_RESISTOR_VALUE = 100000;
const float c1 = 1.009249522e-03;
const float c2 = 2.378405444e-04;
const float c3 = 2.019202697e-07;

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2);
}

void loop() {
  lcd.clear();
  float thermistorVoltage = analogRead(THERMISTOR_PIN);
  float thermistorResistance = KNOWN_RESISTOR_VALUE * (1023.0 / thermistorVoltage - 1.0);
  float logR2 = log(thermistorResistance);
  float temperatureInCelsius = (1.0 / (c1 + c2 * logR2 + c3 * logR2 * logR2 * logR2)) - 273.15;
  lcd.print(" fed.getTemp();");
  lcd.setCursor(5, 1);
  lcd.print(temperatureInCelsius);
  lcd.print("C");
  
  Serial.print(temperatureInCelsius);
  
  delay(5000); // Every 5 seconds
}
