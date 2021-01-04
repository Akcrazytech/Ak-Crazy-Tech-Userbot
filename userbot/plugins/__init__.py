from userbot import topfunc
from userbot.Config import Config
from userbot.utils import admin_cmd
from var import Var

idgen = topfunc.id_generator
findnemo = topfunc.stark_finder
izmesudo = Config.SUDO_USERS
islogokay = Config.PRIVATE_GROUP_ID
isdbfine = Var.DB_URI
isherokuokay = Var.HEROKU_APP_NAME
gdrivenoice = Config.AUTH_TOKEN_DATA
wttrapi = Config.OPEN_WEATHER_MAP_APPID
rmbg = Config.REM_BG_API_KEY
hmmok = Config.LYDIA_API
currentversion = "1.0"
if issudousing:
    izmesudo = "Active ✅"
else:
    izmesudo = "Inactive ❌"

if islogokay:
    logchat = "Connected ✅"
else:
    logchat = "Dis-Connected ❌"

if isherokuokay:
    riplife = "Connected ✅"
else:
    riplife = "Not Connected ❌"

if gdrivenoice:
    sopro = "Active ✅"
else:
    sopro = "Inactive ❌"

if rmbg:
    gendu = "Added ✅"
else:
    gendu = "Not Added ❌"

if wttrapi:
    menuubxd = "Added ✅"
else:
    menuubxd = "Not Added ❌"

if hmmok:
    meiko = "Added ✅"
else:
    meiko = "Not Added ❌"

if isdbfine:
    dbstats = "Fine ✅"
else:
    dbstats = "Not Fine ❌"

inlinestats = (
    f"✘ SHOWING STATS ✘\n"
    f"VERSION = {currentversion} \n"
    f"DATABASE = {dbstats} \n"
    f"SUDO = {izmesudo} \n"
    f"LOG-CHAT = {logchat} \n"
    f"HEROKU = {riplife} \n"
    f"G-DRIVE = {sopro}"
)
