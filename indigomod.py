import os
import pathlib
from dev.ucyt.indigomod.indigomod.print import *
from dev.ucyt.indigomod.indigomod.pip import *

log = 0
out("Welcome to Indigo Mod. We are making sure everything is setup correctly...")
if not os.path.isdir("plugins"):
    log += 1
    warn(f"Log #{log}: Plugins folder not found. Adding...")
    os.makedir("plugins")
try:
    from requests import get
except ModuleNotFoundError:
    log += 1
    modnotfound("requests", log)
    install("requests")
    from requests import get
ip = get('https://api.ipify.org').text
notif(f'Newer Versions: /connect {ip}\nOlder Versions: /wsserver {ip}')
try:
    from MinecraftWS import MinecraftWebSocket, Event, Command
except ModuleNotFoundError:
    log += 1
    modnotfound("MinecraftWS", log)
    install("MinecraftWS")
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
