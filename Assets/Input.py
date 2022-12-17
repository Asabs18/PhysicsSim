import pygame, math, sys, time

pygame.init()

#Handles any user input to the program
class Input:
    def __init__(self, environment, floor, cannon, projectile, controller):
        #Relevant classes
        self.environment = environment
        self.floor = floor
        self.cannon = cannon
        self.projectile = projectile
        self.controller = controller

        #Define screen 
        self.screen = self.environment.screen

        #Define font
        self.font = pygame.font.SysFont('consolas', 20, True)

    #Exits the program if q or exit button is clicked
    def handleExit(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    #Updates angle and or shoots projectile based on click location
    def handleClick(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if not self.projectile.isShot() and not self.controller.getRect().collidepoint(pos):
                self.controller.setAngle(math.degrees(self.cannon.findAngle(pos)))
                self.projectile.shoot()
            elif not self.projectile.isShot() and self.controller.isClickedSB(pos):
                self.projectile.shoot()
            else:
                self.controller.isClickedRB(pos)

    def inputbox(self, events, pos, text, active):
        inputBox = pygame.Rect(pos, (200, 40))
        
        if pygame.mouse.get_pressed()[0]: # active the textbox by clicking on it
            if inputBox.collidepoint(pygame.mouse.get_pos()):
                active = True
            else:
                active = False
            
        for event in events:
            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1] # delete last character
                else:
                    try:
                        ord(event.unicode) # raise error if not a printable character (e.g. Ctrl)
                                        # so that no strange symbol is written instead
                        text += event.unicode
                    except:
                        pass
            
        self.screen.blit(pygame.Surface((200, 40)), pos)

        if active and int(time.time() * 2) % 2:
            blink = '_'
        else:
            blink = ''
        
        textSurf = self.font.render(text + blink, 0, (255, 255, 255))
        self.screen.blit(textSurf, (pos[0] + 12, pos[1] + 12))
        
        textWidth = self.font.render(text, 0, (0, 0, 0)).get_width()
        while textWidth > 176:
            text = text[:-1] # if the text is too long, remove last character
            textWidth = self.font.render(text, 0, (0, 0, 0)).get_width()
        return text, active