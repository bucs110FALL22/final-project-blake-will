import pygame
from src.controller import Controller
# import pygame_menu
#import your controller

def main():
    pygame.init()
    fishing = Controller()
    fishing.mainloop()
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
