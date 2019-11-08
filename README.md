# Hydrotics

Python code for communication between Raspberry Pi's using NRF24L01+ (and [Newly Optimized RF24Network Layer](http://tmrh20.github.io/RF24Network/classRF24Network.html#ac8e9571bb3d2c20d00955b8f5c15b541)). The "Sender" reads the flow from a YS-201F Sensor and send to "Receiver" using NRF24L01+ transceiver.

## Installation

Install 

```bash
pip install foobar
```

## Usage


## Pins and Connections

###Flow Sensor Connections

Red ------------- 5V

           +----- 3V3
           |
          10K
           |
Yellow ----+----- GPIO23 (BCM Mode) or Pin 16 (BOARD Mode)

Black ----------- Ground

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/
