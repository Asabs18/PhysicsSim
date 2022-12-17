import pygame.font

class Button:
	def __init__(self, screen, msg, rect, rgb):
		self.screen = screen
		self.screen_rect = self.screen.get_rect()

		self.width, self.height = rect[2], rect[3]
		self.button_color = rgb
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = (rect[0], rect[1])

		self._prep_msg(msg)

	def _prep_msg(self, msg):
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw(self):
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)

	def isClicked(self, cursorPos):
		return self.rect.collidepoint(cursorPos)