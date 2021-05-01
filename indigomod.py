import os, pathlib

log = 0
print("Welcome to Indigo Mod\nWe are making sure everything is setup correctly...")
if not os.path.isdir("plugins"):
  log += 1
  print(f"Log #{log}: Plugins folder not found. Adding...")
  os.makedir("plugins")
try:
  from requests import get
except ModuleNotFoundError:
  log += 1
  print(f"Log #{log}: requests module not found. Adding...")
  os.system("pip install requests")
  from requests import get
ip = get('https://api.ipify.org').text
print(f'Newer Versions: /connect {ip}\nOlder Versions: /wsserver {ip}')
try:
  from MinecraftWS import MinecraftWebSocket, Event
except ModuleNotFoundError:
  log += 1
  print(f"Log #{log}: MinecraftWS module not found. Adding...")
  os.system("pip install MinecraftWS")
  from MinecraftWS import MinecraftWebSocket, Event

class MWS(MinecraftWebSocket):
  async def on_connect(self):
    print('Connected to Minecraft')
    await self.add_event(Event.BlockBroken)

  async def on_disconnect(self):
    print('Disconnected. Reload Indigo Mod to reconnect.')

  async def on_event(self, event: str, properties: dict):
    if event == Event.BlockBroken:
      ...

MWS().run()