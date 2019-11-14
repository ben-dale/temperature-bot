#define SERIES_RESISTOR 100000    
#define THERMISTOR_PIN A0 
 
void setup(void) {
  Serial.begin(9600);
}
     
void loop(void) {
  float thermistorVoltageDrop = analogRead(THERMISTOR_PIN);
  float thermistorResistance = SERIES_RESISTOR * thermistorVoltageDrop / (1023 - thermistorVoltageDrop);
  float temperatureC = (1.0 / (log(thermistorResistance / 100000) / 3950 + (1.0 / (25 + 273.15)))) - 273.15;     
  Serial.println(temperatureC);
  delay(5000);
}