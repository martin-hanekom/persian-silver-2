import socket
import threading
from conf import g

# Server messages: S:<key>=<value>
# Player messages: <team>:<msg>

local_ip = socket.gethostbyname(socket.getfqdn())
port = 65432
name = ''
clients = []
current_client = None

# server 

def broadcast(client, message: str):
    for c in filter(lambda c: c != client, clients):
        c['client'].send(message.encode('ascii'))

def handle(client: dict):
    while g.running:
        try:
            message = client['client'].recv(1024).decode('ascii')
            broadcast(client, f"{client['team']}:{message}")
        except:
            clients.remove(clients.index(client))
            client['client'].close()
            g.error = f"Player {client['team'] + 1} disconnected"
            broadcast(None, g.error)
            print(g.error)
            g.paused = True
            break
    
def serve():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f'Binding to {local_ip}:{port}')
        s.settimeout(0.2)
        s.bind((local_ip, port))
        s.listen()
        
        while g.running:
            try:
                client, address = s.accept()
            except socket.timeout:
                pass
            except:
                return
            else:
                client.send('S:name=?'.encode('ascii'))
                name = client.recv(1024).decode('ascii')
                team = len(clients)
                client.send(f'S:team={team}'.encode('ascii'))
                clients.append({
                    'client': client,
                    'ip': address,
                    'name': name,
                    'team': team,
                })
                broadcast(None, f'S:len={len(clients)}')
                print(f'Connected to {name}@{address} (team {team + 1})')
                
                handle_thread = threading.Thread(target=handle, args=(clients[-1],))
                handle_thread.start()

                # join as client as well
                #join(local_ip, 'test')

def host():
    serve_thread = threading.Thread(target=serve)
    serve_thread.start()

# client

def write(message: str):
    current_client.send(message.encode('ascii'))
            
def client(ip: str, n: str):
    global name
    name = n
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        current_client = s
        s.connect((ip, port))
        while g.running:
            try:
                message = s.recv(1024).decode('ascii')
                print(message)
                col_pos = message.find(':')
                src = message[:col_pos]
                message = message[col_pos+1:]
                if src == 'S':
                    eq_pos = message.find('=')
                    key = message[:eq_pos]
                    value = message[eq_pos+1:]
                    print(f'Server sent {key}={value}')
                    match key:
                        case 'name':
                            s.send(name.encode('ascii'))
                        case 'team':
                            g.team = value
                else:
                    print(f'Player {src} sent {message}')
            except Exception as e:
                print(e)
                g.error = 'Disconnected'
                s.close()
                print(g.error)
                return

def join(ip: str, n: str):
    client_thread = threading.Thread(target=client, args=(ip, n))
    client_thread.start()
