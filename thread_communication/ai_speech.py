from __future__ import annotations
import asyncio
import random

turn: int = 0

async def listen() -> None:
    print("Listening...")
    await asyncio.sleep(random.randint(1,3))

async def think() -> None:
    print("Thinking...")
    await asyncio.sleep(random.randint(3, 6))

def say_something() -> str:
    i = random.randint(0, 5)
    match i:
        case 0:
            return "Move knight"
        case 1:
            return "Take bishop"
        case 2:
            return "En passant"
        case 3:
            return "Queen fork"
        case 4:
            return "Rook checkmate"
    return "Forget change clocks"

async def player(team: int, msgq: asyncio.Queue) -> None:
    global turn
    while True:
        while team != turn:
            await asyncio.sleep(0.1)
        print(f"Team {team}'s turn.")
        if not msgq.empty():
            await listen()
            msg = await msgq.get()
            print(f"Heard: {msg}")
        if team == 0:
            msg = input("Your message: ")
            await msgq.put(msg)
        else:
            await think()
            await msgq.put(say_something())
        turn = (turn + 1) % 3

async def main():
    msgq = asyncio.Queue()
    ais = [asyncio.create_task(player(i, msgq)) for i in range(3)]
    await asyncio.gather(*ais)

if __name__ == "__main__":
    asyncio.run(main())
