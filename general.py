import logging, jsonhandlers, discord, asyncio
from datetime import datetime, timedelta, timezone


logger = logging.getLogger("logs")

async def handlesecret(message, YAP):
    try:
        await message.delete()
    except Exception as e:
        logger.error(f"Error deleting message: {e}")
    
    await message.author.send(YAP)

async def clearrate(clearingrates):
    now = datetime.now(timezone.utc)
    nexthour = now.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
    nexthoursecs = (nexthour - now).total_seconds()
    while True:
        await asyncio.sleep(nexthoursecs)
        if clearingrates:
            logger.info("Clearing rate limits.")
            data = jsonhandlers.loadjson("./rate.json")
            logger.info(data)
            for key in data:
                data[key] = 0
            jsonhandlers.savejson("./rate.json", data)
            logger.info("Rates cleared.")
        else:
            logger.info("Rate clearing is turned off.")