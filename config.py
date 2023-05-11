from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "25711100"))
API_HASH = getenv("API_HASH", "0118cc1662da972d0206420a7886769a")
BOT_TOKEN = getenv("BOT_TOKEN", "6034374468:AAEnB8MuEres4zWPFWWrB898n3YNGN-lqq0")
SESSION_NAME = getenv("SESSION_NAME", "BACDtgfAbRPySB7Ab1IEp9SZsAHR6op-_vB_72_X3ZMEKZHQnY5WJk-sj86O9rT9cyBXY_WwyUaclQ0OI3vaW-l_TguqQ7GA0N7YkYbTB1OUgDu3fcUNS9VDG2Aa8knARAhhuZBZ6kdaXCHxQzBvNhML4HTfMAxo2yxbJlqiMLUYTa93n_6h-5fp-QsZ-ZFnWZ2mvd6Xuj9-K5btKA09AjrbU1gy3eqZM5qohrOyb-cK3-aQwi-2NKvuzl5-Rc83oypKdclAPPs4WbLlW0r4icauhi9IyS70oFCpepA3mU6uJkmBusQ5xQfqprYEPbIXrSvy95gK-sjA2-yFVNLwAo67ULf5dwA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "DAD_MIDO")
ALIVE_NAME = getenv("ALIVE_NAME", "🇲 🇮 🇩 🇴  🇧 🇦 🇸 🇭")
BOT_USERNAME = getenv("BOT_USERNAME", "B78_Bot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "DAD_MIDO")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Ad_mido")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "1354234231").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1354234231").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
