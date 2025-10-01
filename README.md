# PhotonWarrior28A2 - Examples to use the PW28A2 on Windows
Example code for using the PhotonWarrior28A2 on Windows various APIs and programming languages.


## What is a PhotonWarrior28A2
PhotonWarrior28A2 is a photo amplifier with USB interface with an selectable aplification. Aplification can be set in 6 steps from 10^3 to 10^8.
For more detailed information please visit the [product page](https://www.codemercs.com/en/sensors/pw28a2).


## Output format
The PhotonWarrior28A2 will send 6 bytes of data to the host every 2ms on interface 0. . The data format will be LSB first.

| B0 + B1 | B2 + B3 | B4 + B5  |
| ----------- | ----------- | ----------- |
| 12 bit data  | 16 bit Unused | 16 bit amplification factor |

To get the 12 or 16 Bit value using the following formula: 
```
(B1 << 8) | B0
```
Although the PhotonWarrior28A2 is a joystick device, the data will have no offset to center the axis, the output data will between 0 and 4095. The amplification factor abusing the joystick buttons.


## Bitfield for amplification factor (Byte 4+5)
The amplification factor is reported by abusing the joystick buttons. Buttons numbered 0 to 15
indicate the amplification factor as 10n. The actual bitmask for this is part of the manufacturing data programmed into the sensor during production testing to allow for models with various  mplification factors based on the same PhotonWarrior.

| Amplification | Bitfield |
| ----------- | ----------- |
| 10^0 | 0x0000 |
| 10^1 | 0x0001 |
| 10^2 | 0x0002 |
| 10^3 | 0x0004 |
| 10^? | 0x????  |
| 10^14 | 0x4000 |
| 10^15 | 0x8000 |



# Using 3rd party API and toolchains
For some of the example projecte we are using 3rd party software and API like LibUSB. Please take care about the license about each API.


### LibUSB
We provide some code examples for the JoyWarrior56FR1 by using the [LibUSB API](https://libusb.info/) for cummunication. You can find the repository [here](https://github.com/libusb/libusb).

## Links and further information
[Product site](https://www.codemercs.com/de/sensoren/pw28a2) for more informations, datasheets, and software/tools for the PhotonWarrior28 devices  
[Company site](https://www.codemercs.com) for information on more devices.

## Contact
If you have any questions about the IO-Warrior please contact **support@codemercs.com** or using the [issues](https://github.com/codemercs-com/pw28a2-win/issues) section in this repository. There is also a company [forum](https://forum.codemercs.com/) with many solved questions.

