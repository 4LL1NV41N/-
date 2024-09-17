import logging, main
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

logger = logging.getLogger("logs")

async def on_message(client, message, limit, ratelimiting, __SECRET, YAP):
    if message.author == client.user:
        return
    logger.info(f'Message "{message.content}" sent by user {message.author}')
    data = main.loadjson("./rate.json")
    user_id = str(message.author.id)
    data[user_id] = data.get(user_id, 0) + 1
    main.savejson("./rate.json", data)
    if data[user_id] < limit and ratelimiting:
        if message.content.lower().strip() == __SECRET:
            try:
                await message.delete()
            except Exception as e:
                logger.error(f"Error deleting message: {e}")
            await message.author.send(YAP)
            logger.info("clue given")
        else:
            logger.info("Incorrect guess.")
    elif data[user_id] >= limit and ratelimiting:
        await message.author.send("You are sending requests too quickly.")
    elif not ratelimiting:
        logger.info("Rate limiting is off.")
        
async def on_ready(client):
    logger.info(f"Logged in as {client.user}")
    logger.info("Bot is running!! Have fun!! :3")
    client.loop.create_task(main.clearrate())