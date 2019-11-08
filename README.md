# Hydrotics

Python code for communication between Raspberry Pi's using NRF24L01+ using [Newly Optimized RF24Network Layer](http://tmrh20.github.io/RF24Network/classRF24Network.html#ac8e9571bb3d2c20d00955b8f5c15b541). The "Sender" reads the flow from a YS-201F Sensor and sends to "Receiver" using NRF24L01+ transceiver.

## Installation

Install 

```bash
pip install foobar
```

## Usage


## Pins and Connections

*YS-201F Connections* (Change to Fritizing)

Red ------------- 5V
           +----- 3V3
           |
          10K
           |
Yellow ----+----- GPIO23 (BCM Mode) or Pin 16 (BOARD Mode)
Black ----------- Ground

*NRF24L01+ Connections* (Draw with Fritizin)

| NRF24L01 | Raspberry Pin (BCM Mode)|
| --- | --- |
| 01 - GND | Pin 25 |
| 02 - VCC | Pin 17 |
| 03 - CE | Pin 15 |
| 04 - CSN | Pin 24 |
| 05 - SCK | Pin 23 |
| 06 - MOSI | Pin 19 |
| 07 - MISO | Pin 21 |
| 08 - IRQ | - |


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/
