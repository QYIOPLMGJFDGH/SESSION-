from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "16457832"))
API_HASH = getenv("API_HASH", "3030874d0befdb5d05597deacc3e83ab")

BOT_TOKEN = getenv("BOT_TOKEN", "7445601741:AAGOF4X26GcQoUsAetuejmOloTBG05MxSPU")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Yash_607:Yash_607@cluster0.r3s9sbo.mongodb.net/?retryWrites=true&w=majority")

OWNER_ID = int(getenv("OWNER_ID", 1356469075))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/FallenAssociation")
