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
rm -rf runbot, runbot.sh
echo "SESSION_NAME="argbot"" >> runbot
echo "tmux new-session -d -s $SESSION_NAME" >> runbot
echo "tmux send-keys -t $SESSION_NAME 'python3 main.py' C-m" >> runbot
echo "tmux attach -t $SESSION_NAME" >> runbot
chmod +x runbot.sh
cd ./-/
chmod +x changetoken
touch rate.json
echo ""

echo ""
echo ""
echo -e "To change your secret, enter something below. To set it to default, press \033[1mENTER\033[0m"
DEFAULTSECRET="maestrefi"
read -p "> " NEWSECRET
if [ -z "$NEWSECRET" ]; then
    NEWSECRET="$DEFAULTSECRET"
fi
echo "SECRET=$NEWSECRET" > ../.env
echo ""
echo ""
echo "Enter your discord bot token. This data will not be shared.\n"
echo "If you do not know what that is, refer to this guide: https://guide.pycord.dev/getting-started/creating-your-first-bot\n"
echo -e "If you do not want to ender your token now, press \033[1mctrl+c\033[0m below.\n"
echo "Your token will be stored in ./.env, in the format 'TOKEN = YOUR_TOKEN_HERE'. You can change it if you reset your token.\n"
read -p "> " USER_DISCORD_TOKEN
echo "TOKEN = $USER_DISCORD_TOKEN" >> ../.env
echo -e "type \033[1mrunbot\033[0m to run the bot"
echo -e "if you input the incorrect token, run \033[1mchangetoken CORRECT_TOKEN\033[0m to change it"

