#!/bin/bash


sudo apt update
sudo apt upgrade
sudo apt install git
sudo apt install python3
sudo apt install python3-pip -y
python3 -m pip config set global.break-system-packages true
pip3 install py-cord
pip3 install python-dotenv
git clone http://github.com/4ll1nv41n/-/
cd ./-/
echo "Enter your discord bot token. This data will not be shared."
echo "If you do not know what that is, refer to this guide: https://guide.pycord.dev/getting-started/creating-your-first-bot"
echo "If you do not want to ender your token now, type 'no thanks' below."
echo "Your token will be stored in ./.env, in the format 'TOKEN = YOUR_TOKEN_HERE'. You can change it if you reset your token."
while true; do
    read -p "> " USER_DISCORD_TOKEN

    if [[ "$USER_DISCORD_TOKEN" == "no thanks" ]]; then
        echo "please add your token to ./.env before running the bot"
    fi 

    echo "TOKEN = $USER_DISCORD_TOKEN" > .env

    if python3 main.py; then
        echo "bot started successfully"
        break
    else
        echo "Token incorrect"
    fi
done