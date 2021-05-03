import os
import pathlib
from dev.ucyt.indigomod.indigomod.print import *
from dev.ucyt.indigomod.indigomod.pip import *
from dev.ucyt.indigomod.indigomod.utility import *

log = 0
installmodules(log)
from MinecraftWS import MinecraftWebSocket, Event
from colored import fore, back, style
from requests import get
out("Welcome to Indigo Mod. We are making sure everything is setup correctly...")
if not os.path.isdir("plugins"):
    log += 1
    warn(f"Log #{log}: Plugins folder not found. Adding...")
    os.makedir("plugins")
ip = get('https://api.ipify.org').text
notif(f'Newer Versions: /connect {ip}. Older Versions: /wsserver {ip}')
class MWS(MinecraftWebSocket):
    async def on_connect(self):
        out('Connected to Minecraft!')
        await self.add_event(Event.BlockBroken)
    async def on_disconnect(self):
        out('Disconnected. Reload Indigo Mod to reconnect.')
    async def on_event(self, event: str, properties: dict):
        if event == Event.BlockBroken:
            ...
        elif event == Event.MenuShown:
            ...
        elif event == Event.BlockPlaced:
            ...
        elif event == Event.AdditionalContentLoaded:
            ...
        elif event == Event.AgentCommand:
            ...
        elif event == Event.WorldGenerated:
            ...
        elif event == Event.MultiplayerRoundStart:
            ...
        elif event == Event.ApiInit:
            ...
        elif event == Event.WorldUnloaded:
            ...
        elif event == Event.AppPaused:
            ...
        elif event == Event.AppResumed:
            ...
MWS().run()
