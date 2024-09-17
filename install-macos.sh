#!/bin/bash

echo "You are about to download a discord bot at ./-/"
echo "Any files in ./-/ WILL BE DELETED PERMANENTLY"
echo "You may be prompted when the script is installing dependancies. Please answer with Y or the bot may not work"
echo "Press ENTER to continue with installation"
read

rm -rf ./-/
python3 -m ensurepip
python3 -m pip config set global.break-system-packages true
pip3 install py-cord
pip3 install python-dotenv
git clone http://github.com/4ll1nv41n/-/
cd ./-/
touch rate.json
echo ""
echo ""
echo "Enter your discord bot token. This data will not be shared."
echo "If you do not know what that is, refer to this guide: https://guide.pycord.dev/getting-started/creating-your-first-bot"
echo "If you do not want to ender your token now, press control c below."
echo "Your token will be stored in ./.env, in the format 'TOKEN = YOUR_TOKEN_HERE'. You can change it if you reset your token."
while true; do
    read -p "> " USER_DISCORD_TOKEN
    echo "TOKEN = $USER_DISCORD_TOKEN" > .env

    if python3 main.py; then
        echo "Bot started successfully"
        break
    else
        echo "Token incorrect"
    fi
done
