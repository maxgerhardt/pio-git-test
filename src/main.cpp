#include <Arduino.h>

void setup() {
    Serial.begin(9600);
}

void loop() {
    Serial.println("Version: " + String(VERSION));
    Serial.println("Revision: " + String(PIO_SRC_REV));
}