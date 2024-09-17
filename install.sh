#!/bin/bash

start_bot() {
    SESSION_NAME="argbot"
    tmux new-session -d -s $SESSION_NAME
    tmux send-keys -t $SESSION_NAME 'python3 main.py' C-m
    tmux attach -t $SESSION_NAME
}

echo "You are about to download a discord bot at ./-/"
echo "Any files in ./-/ WILL BE DELETED PERMANENTLY"
echo "You may be prompted when the script is installing dependancies. Please answer with Y or the bot may not work"
echo "Press ENTER to continue with installation"
read

rm -rf ./-/
sudo apt update
sudo apt upgrade
sudo apt install tmux
sudo apt install git
sudo apt install python3
sudo apt install python3-pip -y
python3 -m pip config set global.break-system-packages true
pip3 install py-cord
pip3 install python-dotenv
pip3 install datetime
git clone http://github.com/4ll1nv41n/-/
cd ./-/
touch rate.json

echo ""
echo ""
echo "To change your secret, enter something below. To set it to default, press ENTER"
DEFAULTSECRET="maestrefi"
read -p "> " NEWSECRET
if [ -z "$NEWSECRET" ]; then
    $DEFAULTSECRET = $NEWSECRET
fi
echo "SECRET = $DEFAULTSECRET" >> ../.env
echo ""
echo ""
echo "Enter your discord bot token. This data will not be shared.\n"
echo "If you do not know what that is, refer to this guide: https://guide.pycord.dev/getting-started/creating-your-first-bot\n"
echo "If you do not want to ender your token now, press control c below.\n"
echo "Your token will be stored in ./.env, in the format 'TOKEN = YOUR_TOKEN_HERE'. You can change it if you reset your token.\n"
while true; do
    read -p "> " USER_DISCORD_TOKEN
    echo "TOKEN = $USER_DISCORD_TOKEN" >> ../.env

    if start_bot(); then
        echo "Bot started successfully"
        break
    else
        echo "Token incorrect"
        echo ""
    fi
done

