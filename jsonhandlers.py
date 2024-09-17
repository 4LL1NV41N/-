import json, logging

logger = logging.getLogger("logs")

# json handling
def loadjson(filepath, defaultval:dict={"default":0}) -> dict:
    try:
        with open(filepath, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        logger.warning(f"{filepath} does not exist")
        logger.info(f"initializing {filepath}")
        with open(filepath, "w") as file:
            json.dump(defaultval, file, indent=4)
        with open(filepath, "r") as file:
            return json.load(file)
    except json.decoder.JSONDecodeError:
        logger.warning(f"{filepath} does not have proper JSON")
        logger.info(f"initializing {filepath}")
        with open(filepath, "w") as file:
            json.dump(defaultval, file, indent=4)
        with open(filepath, "r") as file:
            return json.load(file)
    

def savejson(filepath, data):
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)