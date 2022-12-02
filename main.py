import pygame
from controller import Controller
# import pygame_menu
#import your controller

def main():
    pygame.init()
    fishing = controller.Controller()
    fishing.mainloop()
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
