import time
from platform import python_version

from . import ALIVE_NAME, StartTime, catdef, mention, reply_id

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "CUSTOM ALIVE BY @Anony_server"

kraken = bot.uid

AK_IMG = Config.ALIVE_PIC

pm_caption = "__**𝘼𝙆 𝘾𝙍𝘼𝙕𝙔 𝙏𝙀𝘾𝙃 𝙐𝙎𝙀𝙍 𝘽𝙊𝙏 𝙄𝙎 𝙊𝙉𝙇𝙄𝙉𝙀**__\n\n"

pm_caption += f"               T̷̫͉̰͕̒́H̶̪͍̒ͥ͑̓E̸̖̪̱͚ͨ̀͜ K̦̖̙̱̮̐̌I̶̴̗̗̦͍ͨͭ̉͢͟N̰̜͉͔ͬ̽͢G̛͔͇̞̹̈̀͘͘͟ I̶̴̗̗̦͍ͨͭ̉͢͟S̵̶̮̬͖̄͑͟ H̶̪͍̒ͥ͑̓E̸̖̪̱͚ͨ̀͜Ŗ̴̪̈̄͞E̸̖̪̱͚ͨ̀͜\n**『[{DEFAULTUSER}](tg://user?id={kraken})』**\n\n"

pm_caption += "TELETHON : `1.15.0` \n"

pm_caption += f"sudo     : `[NO]`\n"

pm_caption += f"  𝘼𝙆 𝘾𝙍𝘼𝙕𝙔 𝙏𝙀𝘾𝙃 𝙐𝙎𝙀𝙍 𝘽𝙊𝙏 : `[ BOT IS ONLINE MASTER]`\n"

pm_caption += "CHANNEL   : [▁ ▂ ▄ ▅ ▆ ▇ █ ˢυвŜ¢𝐑ⓘв𝓔 █ ▇ ▆ ▅ ▄ ▂ ▁](www.youtube.com/c/akcrazytech)\n"

pm_caption += "CREATOR    : [MASTER HERE](https://t.me/AKSHAY9059)\n\n"
#@command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, AK_IMG, caption=pm_caption)
    await alive.delete() 
