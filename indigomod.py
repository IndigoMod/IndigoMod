from api.dev.ucyt.indigomod.event.handler import *
from api.dev.ucyt.indigomod.print import *
from api.dev.ucyt.indigomod.pip import *
from api.dev.ucyt.indigomod.net import *
from api.dev.ucyt.indigomod.utility import *
from api.dev.ucyt.indigomod.event import *
log = 0
installmodules(log)
from MinecraftWS import MinecraftWebSocket, Event

out("Welcome to Indigo Mod. We are making sure everything is setup correctly...")
if not os.path.isdir("plugins"):
    log += 1
    warn(f"Log #{log}: Plugins folder not found. Adding...")
    os.makedir("plugins")
ip = getip()
notif(f'Newer Versions: /connect {ip}. Older Versions: /wsserver {ip}')
class MWS(MinecraftWebSocket):
    async def on_connect(self):
        out('Connected to Minecraft!')
        await self.add_event(Event.BlockBroken)
    async def on_disconnect(self):
        out('Disconnected. Reload Indigo Mod to reconnect.')
    async def on_event(self, event: str, properties: dict):
        handle(event)
MWS().run()
