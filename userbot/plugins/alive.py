import asyncio
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "CUSTOM ALIVE BY @Anony_server"

kraken = bot.uid

PM_IMG = "https://telegra.ph/file/59cde5d32cfb4ba9c0972.jpg"
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
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
