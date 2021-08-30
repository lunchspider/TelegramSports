import json
import logging
import requests

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

dice = "🎳⚽️🎯🏀🎲🎰"
with open("./config.json", "rt") as fobj:
    TOKEN = json.load(fobj)["token"]

update_fetcher_link = f"https://api.telegram.org/bot{TOKEN}/getUpdates?offset=OFFSET&allowed_updates=[\"message\"]"
dice_sender_link = f"https://api.telegram.org/bot{TOKEN}/sendDice?chat_id=SEND_TO&emoji="

def get_and_report():