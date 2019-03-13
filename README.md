# MicroPython NodeMCU (ESP8266) Memorandom

## Getting started with Arduino IDE on the NodeMCU
1. Install driver with Homebrew on OSX
    *  `$ brew tap cask-driver`
    * `$ brew cask install silicon-labs-vcp-driver`
2. Install additional libraries for Arduino IDE
    * Arduino > Preference > Settings > Additional Boards Managers URLs
    * Input: [http://arduino.esp8266.com/stable/package_esp8266com_index.json](http://arduino.esp8266.com/stable/package_esp8266com_index.json)
    * Restart Arduino IDE
    * Tools > Board: NodeMCU 1.0 (ESP-12E Module)
    * Tools > Port: /dev/cu.SLAB_USBtoUART
3. Test hardware with blink program
    **nodemcu_blink.ino**
    ```arudino
    #define LED 2
    #define DELAY 500

    void setup() {
    pinMode(LED, OUTPUT);  
    }

    void loop() {
    digitalWrite(LED, HIGH);
    delay(DELAY);
    digitalWrite(LED, LOW);
    delay(DELAY);
    }
    ```
