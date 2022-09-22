g_var = None

def init(team: int):
    global g_var
    from client import Client
    g_var = Client(team, [])

def g():
    return g_var
