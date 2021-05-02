<h1>IndigoMod</h1>
Indigo Mod is a Minecraft Bedrock modloader using web socket connections.
<h2>Installation</h2>
1. Download Python (**Python 3 recommended**) https://python.org
2. Download IndigoMod Zip (Not quite ready)
3. Unzip IndigoMod Zip
<h2>Usage</h2>
1. Open Minecraft Bedrock Edition
2. Create a new world with cheats enabled **or** use an existing world with cheats enabled.
3. Open <code>run.cmd</code>, **not <code>indigomod.py</code>**. *First time use may take a while to load.*
4. Open the chat window in Minecraft.
5. Enter <code>/connect (code)</code>. You can find your code in the window that opened when you ran <code>run.cmd</code>.
6. Open the chat window in Minecraft.
7. Type <code>.version</code> to verify that IndigoMod loaded properly.
<h2>Plugins</h2>
**Plugins do not change the way your game looks. Some plugin developers may pair a plugin with an addon.**
<h4>WARNING</h4>
IndigoMod is **not** responsible for harmful plugins. A list of approved plugins are coming soon.
<h4>Installation Instructions</h4>
1. To install a plugin, download the plugin file. It should look like `plugin.py`.
2. Locate the <code>indigomod/plugins</code> directory. If you have never ran IndigoMod before, the directory may not appear.
3. Place the plugin into the <code>indigomod/plugins</code> directory.
<h2>Developing Plugins</h2>
This is a tutorial for developers. You shoud have basic Python skills.
<h3>Imports</h3>
Your plugin should have one import, <code>from api import *</code>. This import is not required if you are not going to do anything ingame (for example, just using it to log actions)
IndigoMod just grabs variabled from your file, so there is no need for special naming or other imports.
<h3>Events</h3>
You can find a full list of events here. https://github.com/Beta5051/MinecraftWS/blob/master/MinecraftWS/event.py
<br><br>

 ```py
 def onAchivement(args): # You can set this to anything. args is a required argument, even if you are not going to use them.
   print("GG! You got an achivement!")
   events = {
     "AwardAchievement" : onAchivement # onAchivement not onAchivement()
   }
 ```
