import os
import pathlib
import cool.indigomod
from cool.indigomod.print import *

log = 0
out("Welcome to Indigo Mod\nWe are making sure everything is setup correctly...")
if not os.path.isdir("plugins"):
    log += 1
    warn(f"Log #{log}: Plugins folder not found. Adding...")
    os.makedir("plugins")
try:
    from requests import get
except ModuleNotFoundError:
    log += 1
    warn(f"Log #{log}: requests module not found. Adding...")
    os.system("pip install requests")
    from requests import get
ip = get('https://api.ipify.org').text
notif(f'Newer Versions: /connect {ip}\nOlder Versions: /wsserver {ip}')
try:
    from MinecraftWS import MinecraftWebSocket, Event, Command
except ModuleNotFoundError:
    log += 1
    warn(f"Log #{log}: MinecraftWS module not found. Adding...")
    os.system("pip install MinecraftWS")
    from MinecraftWS import MinecraftWebSocket, Event


class MWS(MinecraftWebSocket):
    async def on_connect(self):
        out('Connected to Minecraft')
        await self.add_event(Event.BlockBroken)

    async def on_disconnect(self):
        out('Disconnected. Reload Indigo Mod to reconnect.')

    async def on_event(self, event: str, properties: dict):
        if event == Event.BlockBroken:
            ...


out("Running websocket...")
MWS().run()
