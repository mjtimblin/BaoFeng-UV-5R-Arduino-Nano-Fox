## BaoFeng UV-5R Arduino Nano Fox ##

#### Description ####
This project is adapted from Tim Giles's work ([https://github.com/timogiles/ArduFoxGPS](https://github.com/timogiles/ArduFoxGPS)). GPS functionality has been removed for simplicity. I use Ubuntu 16.04, so all instructions will be for Ubuntu 16.04. The python script is designed to be easy to use and will automatically upload the compiled program to an attached Arduino Nano. To use this project in the United States, you must be a licensed amateur radio operator. Follow laws and regulations in your area.

#### Dependencies ####
- python3
- python3-pip
- arduino-core
- libyaml-perl
- arduino-sketch

<br><br>
Ubuntu 16.04
```bash
sudo apt install python3 python4-pip arduino-core libyaml-perl  
sudo pip3 install arduino-sketch
```

#### Instructions ####
To use the project, simple run the python script.
```bash
cd BaoFeng-UV-5R-Arduino-Nano-Fox
./fox.py
```