import asyncio
import random

HOST = '127.0.0.1'
PORT = 8888
MAX_BYTES = 1024

names = [
    'Reuben',
    'Simeon',
    'Levi',
    'Judah',
    'Dan',
    'Naphtali',
    'Gad',
    'Asher',
    'Issachar',
    'Zebulun',
    'Joseph',
    'Benjamin',
]

async def add_player(team: int, host: str, port: int):
    name = random.choice(names)
    reader, writer = await asyncio.open_connection(host, port)
    print(f'[client{team}] Sending: team={team},name={name}')
    writer.write(f'team={team},name={name}'.encode())
    while True:
        data = await reader.read(MAX_BYTES)
        print(f'[client{team}] Received: {data.decode()!r}')
        await asyncio.sleep(1)
    print(f'[client{team}] Close the connection')
    writer.close() 

async def handle_player(reader, writer):
    data = await reader.read(MAX_BYTES)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print(f'[server] Received {message!r} from {addr!r}')
    print(f'[server] Send: {message!r}')
    writer.write(data)
    await writer.drain()
    print('[server] Close the connection')
    writer.close()

async def main():
    server = await asyncio.start_server(handle_player, HOST, PORT)
    players = [await add_player(i, HOST, PORT) for i in range(3)]
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())
