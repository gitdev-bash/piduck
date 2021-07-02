# Piduck
Piduck is a program with which you can easily use your Raspberry Pi Zero as a USB HID keyboard. It uses the scripting language [Ducky-Script-v1].

The Project is in Beta and help is needed.
For now, only the US keyboard layout is available.

## Contributions
All contributions are welcome!
## Setup
### HID Setup
[Source1][Hid-setup-source1]
[Source2][Hid-setup-source2]  
All commands have to be run as root!
#### Modules & Drivers
`echo "dtoverlay=dwc2" >> /boot/config.txt`

`echo "dwc2" >> /etc/modules`

`echo "libcomposite" >> /etc/modules`
#### Configuration
`touch /usr/bin/virtusb`

`chmod +x /usr/bin/virtusb`

`cat > /usr/bin/virtusb`
```
#!/bin/bash
cd /sys/kernel/config/usb_gadget/
mkdir -p virtusb
cd virtusb
echo 0x1d6b > idVendor # Linux Foundation
echo 0x0104 > idProduct # Multifunction Composite Gadget
echo 0x0100 > bcdDevice # v1.0.0
echo 0x0200 > bcdUSB # USB2
mkdir -p strings/0x409
echo "virtusb638429573" > strings/0x409/serialnumber
echo "virtusb" > strings/0x409/manufacturer
echo "virtusb USB Device" > strings/0x409/product
mkdir -p configs/c.1/strings/0x409
echo "Config 1: ECM network" > configs/c.1/strings/0x409/configuration
echo 250 > configs/c.1/MaxPower

# Add functions here
mkdir -p functions/hid.usb0
echo 1 > functions/hid.usb0/protocol
echo 1 > functions/hid.usb0/subclass
echo 8 > functions/hid.usb0/report_length
echo -ne \\x05\\x01\\x09\\x06\\xa1\\x01\\x05\\x07\\x19\\xe0\\x29\\xe7\\x15\\x00\\x25\\x01\\x75\\x01\\x95\\x08\\x81\\x02\\x95\\x01\\x75\\x08\\x81\\x03\\x95\\x05\\x75\\x01\\x05\\x08\\x19\\x01\\x29\\x05\\x91\\x02\\x95\\x01\\x75\\x03\\x91\\x03\\x95\\x06\\x75\\x08\\x15\\x00\\x25\\x65\\x05\\x07\\x19\\x00\\x29\\x65\\x81\\x00\\xc0 > functions/hid.usb0/report_desc
ln -s functions/hid.usb0 configs/c.1/
# End functions

ls /sys/class/udc > UDC


```  
Press Ctrl-D to exit  
`reboot` reboot to activate the changes
### Install
Run these as a sudo user or root!

If you want to reinstall or update piduck, please rerun the script.

#### if you have curl

`curl -sSL https://raw.githubusercontent.com/gitdev-bash/piduck/master/install.sh | bash`

#### if you have wget  

`wget -q -O - https://raw.githubusercontent.com/gitdev-bash/piduck/master/install.sh | bash`

#### If you already have it locally

`chmod 755 install.sh`  
`./install.sh`

## Usage
Syntax of [Ducky-Script-v1][Ducky-Script-v1-Syntax]  
Root is needed (again)
### Using Script File
`piduck -i inject.txt`
### Input from standard input
`piduck`

Exit with `CTRL C` or `CTRL D`
### Set Layout
`piduck -l xx`
### Help
`piduck -h`
## Disclamer
This project may not be used illegally and i am not responsible for any damages made with or by this project.

[Ducky-Script-v1-Syntax]: https://github.com/hak5darren/USB-Rubber-Ducky/wiki/Duckyscript
[Ducky-Script-v1]: https://github.com/hak5darren/USB-Rubber-Ducky/wiki
[Hid-setup-source1]: https://randomnerdtutorials.com/raspberry-pi-zero-usb-keyboard-hid/
[Hid-setup-source2]: https://www.isticktoit.net/?p=1383
