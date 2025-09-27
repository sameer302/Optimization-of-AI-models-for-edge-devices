# 1. to know the list of packages installed in any environment

pip list

# 2. to create a virtual environment, activate it, install any dependency and close the virtual environment

python -m venv venv
source venv/bin/activate # for linux
venv\Scripts\activate # for windows
pip install numpy # or whatever you need
deactivate

# 3. to create a requirements.txt to save all the dependencies of our project

pip freeze > requirements.txt

# 4. to install latest software on pi

sudo apt update \&\& sudo apt full-upgrade

# 5. to see what firmware is installed on pi

sudo rpi-eeprom-update

# 6. to know the the peripherals connected via PCI

lscpi

# 7. to open config.txt file

sudo nano /boot/firmware/config.txt

# 8. install the dependencies required to use the NPU and some checks to verify 

sudo apt install hailo-all
sudo reboot # this will disconnect pi 5 every time so that i will have to reconnect via entering password everytime
hailortcli fw-control identify
dmesg | grep -i hailo

# 9. display the system performance

htop

# 10. To run a jupyter notebook from virtual environment

python -m ipykernel install --user --name=rasp --display-name "Rasp Jupyter environment"

# 11. To know the network to which my pi 5 is connected to

iwgetid

# 12. to see all the available wifi networks

nmcli dev wifi list

# 13. to see all the saved network profiles

nmcli connection show

# 14. to add a new network and immediately connect to it

nmcli dev wifi connect "NEW_SSID" password "NEW_PASSWORD"

# 15. to start connection with Raspberry Pi Connect service from browser

rpi-connect on

# 16. to close connection with Raspberry Pi Connect service from browser

rpi-connect off

# 17. To open a text file in bash

nano filename

