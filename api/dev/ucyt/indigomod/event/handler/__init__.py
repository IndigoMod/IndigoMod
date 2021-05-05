from MinecraftWS import Event

import api.dev.ucyt.indigomod.exc
from api.dev.ucyt.indigomod.short import throw


def handle(event):
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
    elif event == Event.AppSuspended:
        ...
    elif event == Event.BossKilled:
        ...
    elif event == Event.CameraUsed:
        ...
    elif event == Event.EndOfDay:
        ...
    elif event == Event.ConnectionFailed:
        ...
    elif event == Event.ChunkChanged:
        ...
    elif event == Event.ChunkLoaded:
        ...
    elif event == Event.ChunkUnloaded:
        ...
    elif event == Event.VehicleExited:
        ...
    elif event == Event.ConfigurationChanged:
        ...
    elif event == Event.MultiplayerRoundEnd:
        ...
    elif event == Event.WorldLoaded:
        ...
    elif event == Event.AwardAchievement:
        ...
    elif event == Event.CraftingSessionCompleted:
        ...
    elif event == Event.FileTransmissionCancelled:
        ...
    elif event == Event.FileTransmissionStarted:
        ...
    elif event == Event.FileTransmissionCompleted:
        ...
    elif event == Event.CauldronUsed:
        ...
    elif event == Event.UploadSkin:
        ...
    elif event == Event.TextToSpeechToggled:
        ...
    elif event == Event.BoardTextUpdated:
        ...
    elif event == Event.SignInToEdu:
        ...
    elif event == Event.SignInToXboxLive:
        ...
    elif event == Event.SignOutOfXboxLive:
        ...
    elif event == Event.LicenseCensus:
        ...
    elif event == Event.FirstTimeClientOpen:
        ...
    elif event == Event.FocusLost:
        ...
    elif event == Event.FocusGained:
        ...
    elif event == Event.HardwareInfo:
        ...
    elif event == Event.GameSessionStart:
        ...
    elif event == Event.GameSessionComplete:
        ...
    elif event == Event.StartClient:
        ...
    elif event == Event.ItemEnchanted:
        ...
    elif event == Event.ItemUsed:
        ...
    elif event == Event.ItemCrafted:
        ...
    elif event == Event.ItemDropped:
        ...
    elif event == Event.ItemSmelted:
        ...
    elif event == Event.ItemAcquired:
        ...
    elif event == Event.ItemDestroyed:
        ...
    elif event == Event.SpecialMobBuilt:
        ...
    elif event == Event.JukeboxUsed:
        ...
    else:
        throw(api.dev.ucyt.indigomod.exc.IndigoModGenericException("Unimplemented event triggered: " + event + ". IndigoMod will not continue."))