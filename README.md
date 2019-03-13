# MicroPython NodeMCU (ESP8266) Memorandom

## Getting started with Arduino IDE on the NodeMCU
1. Install driver with Homebrew on OSX
    * `$ brew tap cask-driver`
    * `$ brew cask install silicon-labs-vcp-driver`
2. Install additional libraries for Arduino IDE
    * Arduino > Preference > Settings > Additional Boards Managers URLs
    * Input: [http://arduino.esp8266.com/stable/package_esp8266com_index.json](http://arduino.esp8266.com/stable/package_esp8266com_index.json)
    * Restart Arduino IDE
    * Tools > Board: NodeMCU 1.0 (ESP-12E Module)
    * Tools > Port: /dev/cu.SLAB_USBtoUART
3. Test hardware with blink program: **nodemcu_blink.ino**
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

## Getting started with MocroPython on the NodeMCU
1. Download Micropython firmware for ESP8266
    * [Micropython Download Page](http://micropython.org/download/#esp8266)
2. Install [esptool](https://github.com/espressif/esptool) for communicating with ESP chip
    * `$ brew install esptool`
3. Check the port name of nodeMCU
    * `$ esptool.py read_flash_status`
    ```console
    esptool.py v2.5.1
    Found 2 serial ports
    Serial port /dev/cu.SLAB_USBtoUART
    Connecting........_
    Detecting chip type... ESP8266
    Chip is ESP8266EX
    Features: WiFi
    MAC: 00:11:22:33:44:55
    Uploading stub...
    Running stub...
    Stub running...
    Status value: 0x0001
    Hard resetting via RTS pin...
    ```
4. Erase the flash on nodeMCU: 
    * `$ esptool.py -p /dev/cu.SLAB_USBtoUART erase_flash`
    ```console
    ...
    Erasing flash (this may take a while)...
    Chip erase completed successfully in 1.5s
    Hard resetting via RTS pin...
    ```
5. Deploy the frimware to nodeMCU
    * `$ esptool.py -p /dev/cu.SLAB_USBtoUART -b 460800 write_flash --flash_size=detect -fm dio 0 esp8266-20190125-v1.10.bin`
    ```console
    ...
    Changing baud rate to 460800
    Changed.
    Configuring flash size...
    Auto-detected Flash size: 4MB
    Flash params set to 0x0040
    Compressed 615388 bytes to 399928...
    Wrote 615388 bytes (399928 compressed) at 0x00000000 in 9.3 seconds (effective 528.9 kbit/s)...
    Hash of data verified.

    Leaving...
    Hard resetting via RTS pin...
    ```
6. Test the result of installation with REPL
    * `$ screen /dev/cu.SLAB_USBtoUART 115200`
    ```console
    OSError: [Errno 2] ENOENT

    MicroPython v1.10-8-g8b7039d7d on 2019-01-26; ESP module with ESP8266
    Type "help()" for more information.
    >>>
    ```
7. Program a simple function of blinking
    ```python
    from machine import Pin
    import time
    led = Pin(2, Pin.Out)
    for i in range(10):
        led.off()
        time.sleep(0.5)
        led.on()
        time.sleep(0.5)
    ```