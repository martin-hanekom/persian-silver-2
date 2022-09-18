import pygame
from client import Client
from conf import cc

def main():
    pygame.init()
    client = Client(0, [])
    client.run()
    pygame.quit()

if __name__ == "__main__":
    main()
