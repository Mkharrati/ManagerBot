#!/bin/bash

rm -r /root/ManagerBot

clear

echo
echo
echo "                Welcome to ManagerBot"
echo
echo

read -p "Enter the telegram bot token : " TELEGRAM_BOT_TOKEN
read -p "Enter the Telegram admin chat ids in *brocket. (like: [12345678]) : " TELEGRAM_ADMIN_CHAT_ID
read -p "Enter the panel url (like: https://sub.domain.com) : " PANEL_URL
read -p "Enter the panel api token : " PANEL_API_TOKEN

cat > /root/.env <<-EOM
TELEGRAM_BOT_TOKEN=$TELEGRAM_BOT_TOKEN
TELEGRAM_ADMIN_CHAT_ID=$TELEGRAM_ADMIN_CHAT_ID
PANEL_URL=$PANEL_URL
PANEL_API_TOKEN=$PANEL_API_TOKEN

EOM

sudo apt update && upgrade -y

sudo apt install python3 dotenv python3-venv python3-pip git -y

sudo cd /root

sudo git clone https://github.com/Mkharrati/ManagerBot.git && cd ManagerBot

sudo python3 -m venv Manager-venv

sudo source Manager-venv/bin/activate

sudo pip install -r requirements.txt

sudo mv /root/.env /root/ManagerBot/

sudo chmod +x main.py

sudo nohup python3 main.py & disown

clear

echo
echo
echo "                 Manager bot ruined successfully ✅"
echo
echo
