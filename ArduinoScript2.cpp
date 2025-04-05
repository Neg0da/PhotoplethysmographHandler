const int analogPin = A1; // Аналоговий вхід
const int digitalPin = 3; // Цифровий вихід
const int threshold = 512; // Поріг перетворення
const int maxIndex = 100; // Максимальне значення індексу

int index = 0;
unsigned long prevTime = 0;
const unsigned long interval = 2; // Інтервал у мілісекундах (0.002 секунди)

void setup() {
    pinMode(digitalPin, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    unsigned long currentTime = millis();
    if (currentTime - prevTime >= interval) {
        prevTime = currentTime;
        
        int analogValue = analogRead(analogPin); // Зчитуємо значення
        Serial.print("Index: ");
        Serial.print(index);
        Serial.print(" | Analog: ");
        Serial.println(analogValue); // Вивід у монітор порту
        
        if (analogValue > threshold) {
            digitalWrite(digitalPin, HIGH); // Увімкнути вихід
        } else {
            digitalWrite(digitalPin, LOW); // Вимкнути вихід
        }
        
        index++;
        if (index >= maxIndex) {
            index = 0; // Скидання індексу
        }
    }
}