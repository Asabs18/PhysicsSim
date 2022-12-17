import pygame, time

pygame.init()

class InputBox:
    def __init__(self, pos, text, active):
        self.pos = pos
        self.text = text
        self.active = active

    #Activate the textbox by clicking on it
    def isClicked(self):
        inputBox = pygame.Rect(self.pos, (200, 40))

        if pygame.mouse.get_pressed()[0]: 
            if inputBox.collidepoint(pygame.mouse.get_pos()):
                return True
            else:
                return False

    def updateText(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1] # delete last character
                else:
                    #Raise error if not a printable character
                    try:
                        ord(event.unicode)
                        self.text += event.unicode
                    except:
                        pass

    def update(self, events):
        self.active = self.isClicked()

        self.updateText(events)

        #Display background box 
        self.screen.blit(pygame.Surface((200, 40)), self.pos)

        #Display cursor when active
        if self.active and int(time.time() * 2) % 2:
            blink = '_'
        else:
            blink = ''
        
        #Display Text
        textSurf = self.font.render(self.text + blink, 0, (255, 255, 255))
        self.screen.blit(textSurf, (self.pos[0] + 12, self.pos[1] + 12))
    
        # if the text is too long, remove last character
        textWidth = self.font.render(self.text, 0, (0, 0, 0)).get_width()
        while textWidth > 176:
            self.text = self.text[:-1] 
            textWidth = self.font.render(self.text, 0, (0, 0, 0)).get_width()