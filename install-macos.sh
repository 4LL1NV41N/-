#!/bin/bash


GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'


python3 -m ensurepip
python3 -m pip config set global.break-system-packages true
pip3 install py-cord
pip3 install python-dotenv
git clone http://github.com/4ll1nv41n/-/
cd ./-/
echo ""
echo ""
printf "${GREEN}Enter your discord bot token. This data will not be shared."
printf "If you do not know what that is, refer to this guide: https://guide.pycord.dev/getting-started/creating-your-first-bot"
printf "If you do not want to ender your token now, press control c below."
printf "Your token will be stored in ./.env, in the format 'TOKEN = YOUR_TOKEN_HERE'. You can change it if you reset your token.${NC}"
while true; do
    read -p "> " USER_DISCORD_TOKEN
    echo "TOKEN = $USER_DISCORD_TOKEN" > .env

    if python3 main.py; then
        echo "Bot started successfully"
        break
    else
        printf "${RED}Token incorrect${NC}"
    fi
done
echo "installation complete, install.sh quitting"
