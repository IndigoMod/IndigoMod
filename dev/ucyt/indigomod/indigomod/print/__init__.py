def out(msg):
    print("[Indigo - Out] - " + msg)


def warn(msg):
    print("[Indigo - Warn] - " + msg)


def err(msg):
    print("[Indigo - Error] - " + msg)


def notif(msg):
    print("[Indigo - Message] - " + msg)


def modnotfound(mnf, log):
    warn(f"Log #{log}: {mnf} module not found. Adding...")
