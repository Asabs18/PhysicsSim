import pygame, time
from Assets.constants import *

pygame.init()

#TODO: Change name to textbox not inputbox
class InputBox:
    def __init__(self, environment, textboxRect, text, unit, active, constant):
        self.screen = environment.getScreen()

        #Relevant classes
        self.environment = environment

        #Define text as blank
        self.text = text

        #Define rect, position, size, and activation status
        self.rect = textboxRect
        self.pos = (self.rect[0], self.rect[1])
        self.width = self.rect[2]
        self.height = self.rect[3]
        self.active = active

        #Define font and units
        self.font = DEFAULT_F
        self.unit = "   " + unit

        #Define if the Inputbox can be edited or not
        self.constant = constant

    #Activate the textbox by clicking on it
    def isClicked(self):
        inputBox = pygame.Rect(self.pos, (self.width, self.height))

        if pygame.mouse.get_pressed()[0] and not self.constant: 
            if inputBox.collidepoint(pygame.mouse.get_pos()):
                self.active = True
            else:
                self.active = False

    #Update text string based on key presses each time through loop
    def updateText(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and self.active:
                # delete last character
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif  event.unicode.isdigit():
                    #Raise error if not a printable character
                    try:
                        ord(event.unicode)
                        self.text += event.unicode
                    except:
                        pass

    #Display updated textbox on screen
    def update(self, events, text=""):
        if text != "":
            self.text = text

        self.isClicked()

        self.updateText(events)

        #Draw background box
        pygame.draw.rect(self.screen, BLACK, pygame.Rect(self.pos[0] - 4, self.pos[1] - 4, self.width + 8, self.height + 8))
        pygame.draw.rect(self.screen, WHITE, pygame.Rect(self.pos[0], self.pos[1], self.width, self.height))

        #Display cursor when active
        if self.active and int(time.time() * 2) % 2:
            blink = "_"
        else:
            blink = " "
        
        #Display Text
        textSurf = self.font.render(self.text + blink + self.unit, 0, BLACK)
        self.screen.blit(textSurf, (self.pos[0] + TEXT_OFFSET, self.pos[1] + TEXT_OFFSET))
    
        # if the text is too long, remove last character
        textWidth = self.font.render(self.text + self.unit, 0, BLUE).get_width()
        while textWidth > (self.width - TEXT_OFFSET * 2):
            self.text = self.text[:-1] 
            textWidth = self.font.render(self.text + self.unit, 0, BLUE).get_width()

    def deactivate(self):
        self.active = False
        
    #GETTERS

    def getRect(self):
        return self.rect

    def getText(self):
        return self.text

    def isActive(self):
        return self.active