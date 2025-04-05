const int analogPin = A1; // Аналоговий вхід
const int digitalPin = 3; // Цифровий вихід
const int threshold = 512; // Поріг перетворення

void setup() {
    pinMode(digitalPin, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    int analogValue = analogRead(analogPin); // Зчитуємо значення
    Serial.println(analogValue); // Вивід у монітор порту
    
    if (analogValue > threshold) {
        digitalWrite(digitalPin, HIGH); // Увімкнути вихід
    } else {
        digitalWrite(digitalPin, LOW); // Вимкнути вихід
    }
    delay(10); // Невелика пауза для стабільності
}
