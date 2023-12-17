const int BralliePin1=7;
const int BralliePin2=6;
const int BralliePin3=5;
const int BralliePin4=4;
const int BralliePin5=3;
const int BralliePin6=2;

String chr = "";

void setup() {
  Serial.begin(115200);       // set the baud rate
  Serial.println("Ready");    // print "Ready" once
  pinMode(BralliePin1,OUTPUT);
  pinMode(BralliePin2,OUTPUT);
  pinMode(BralliePin3,OUTPUT);
  pinMode(BralliePin4,OUTPUT);
  pinMode(BralliePin5,OUTPUT);
  pinMode(BralliePin6,OUTPUT);
  digitalWrite(BralliePin1,LOW);
  digitalWrite(BralliePin2,LOW);
  digitalWrite(BralliePin3,LOW);
  digitalWrite(BralliePin4,LOW);
  digitalWrite(BralliePin5,LOW);
  digitalWrite(BralliePin6,LOW);
}

void loop() {
  if (Serial.available()) {
    chr = "";
    delay(1);
    chr += (char)Serial.read();
    Serial.println(chr);
    switch (chr[0]) {
      case 'a': PORTD=B01111111; break;
      case 'b': PORTD=B00111111; break;
      case 'c': PORTD=B01101111; break;
      case 'd': PORTD=B01100111; break;
      case 'e': PORTD=B01110111; break;
      case 'f': PORTD=B00101111; break;
      case 'g': PORTD=B00100111; break;
      case 'h': PORTD=B00110111; break;
      case 'i': PORTD=B10101111; break;
      case 'j': PORTD=B10100111; break;
      case 'k': PORTD=B01011111; break;
      case 'l': PORTD=B00011111; break;
      case 'm': PORTD=B01001111; break;
      case 'n': PORTD=B01000111; break;
      case 'o': PORTD=B01010111; break;
      case 'p': PORTD=B00001111; break;
      case 'q': PORTD=B00000111; break;
      case 'r': PORTD=B00010111; break;
      case 's': PORTD=B10001111; break;
      case 't': PORTD=B10000111; break;
      case 'u': PORTD=B01011011; break;
      case 'v': PORTD=B00011011; break;
      case 'w': PORTD=B10100011; break;
      case 'x': PORTD=B01001011; break;
      case 'y': PORTD=B01000011; break;
      case 'z': PORTD=B01010011; break;
      case ',': PORTD=B10111111; break;
      case ' ': PORTD=B11111111; break;
      case '\n': PORTD=B11111111; break;
      default:  PORTD=B11111111; break;
    }
    delay(1500);
    PORTD=B11111111;
    delay(500);
  }
}

/*
      case 'a': PORTD=B10000000; break;
      case 'b': PORTD=B11000000; break;
      case 'c': PORTD=B10010000; break;
      case 'd': PORTD=B10011000; break;
      case 'e': PORTD=B10001000; break;
      case 'f': PORTD=B11010000; break;
      case 'g': PORTD=B11011000; break;
      case 'h': PORTD=B11001000; break;
      case 'i': PORTD=B01010000; break;
      case 'j': PORTD=B01011000; break;
      case 'k': PORTD=B10100000; break;
      case 'l': PORTD=B11100000; break;
      case 'm': PORTD=B10110000; break;
      case 'n': PORTD=B10111000; break;
      case 'o': PORTD=B10101000; break;
      case 'p': PORTD=B11110000; break;
      case 'q': PORTD=B11111000; break;
      case 'r': PORTD=B11101000; break;
      case 's': PORTD=B01110000; break;
      case 't': PORTD=B01111000; break;
      case 'u': PORTD=B10100100; break;
      case 'v': PORTD=B11100100; break;
      case 'w': PORTD=B01011100; break;
      case 'x': PORTD=B10110100; break;
      case 'y': PORTD=B10111100; break;
      case 'z': PORTD=B10101100; break;
      case ' ': PORTD=B00000000; break;
      case '\n': PORTD=B00000000; break;
      default: PORTD=B00000000; break;
*/