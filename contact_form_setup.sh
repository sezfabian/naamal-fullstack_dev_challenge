#!/bin/bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3
sudo apt-get install python3-pip
pip install Flask
pip install Flask-cors
pip install flask_mail
pip install sib-api-v3-sdk
pip install pymongo
sudo apt-get install mongodb-server
sudo wget https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh
bash install.sh
source ~/.bashrc
nvm -v
sudo nvm install v18
node -v
npm -v
nvm use 18
nvm alias default 18
sudo npm install -g @vue/cli
cd web_app
npm install
npm install -g serve
