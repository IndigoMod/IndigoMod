from api.dev.ucyt.indigomod.pip import *
from api.dev.ucyt.indigomod.print import *
def installmodules(log):
    try:
        from requests import get
    except ModuleNotFoundError:
        log += 1
        modnotfound("requests", log)
        install("requests")
        from requests import get
    try:
        from colored import fore, back, style
    except ModuleNotFoundError:
        log += 1
        modnotfound("colored", log)
        install("colored")
        from colored import fore, back, style
    try:
        from MinecraftWS import MinecraftWebSocket, Event, Command
    except ModuleNotFoundError:
        log += 1
        modnotfound("MinecraftWS", log)
        install("MinecraftWS")
        from MinecraftWS import MinecraftWebSocket, Event

