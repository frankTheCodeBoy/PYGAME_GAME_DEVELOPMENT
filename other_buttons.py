import pygame.font
from time import sleep

class HelpButton:
    """A class to store, define help button"""
    def __init__(self, first_play, msg):
        """Initialize button attributes"""
        self.screen = first_play.screen
        self.screen_rect = self.screen.get_rect()

        # Set dimensions and properties of the button.
        self.width, self.height = 75, 40
        self.button_color = (250,250,250)
        self.text_color = (60,60,60)
        self.font = pygame.font.SysFont('None', 30, italic=True)
        self.new_font = pygame.font.SysFont('arial',23, italic=False)
        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.left = self.screen_rect.left + 15
        self.rect.top = self.screen_rect.top + 60
        # Screen text attributes
        self.new_text_color = (250,0,0)
        self.new_button_color = (0,0,0)
        # The button message needs to be prepped only once.
        self._prep_help(msg)

    def _prep_help(self,msg):
        """Turn msg into a rendered image and center text on button"""
        self.msg_image = self.font.render(msg, True, 
            self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_help(self):
        """Draw blank button and then draw message"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def show_guide(self):
        """Show game instructions"""
        filename = "instructions.txt"
        with open(filename) as f:
            msg = f.read().strip()
        self.text_surface = self.new_font.render(msg, True,
         self.new_text_color, self.new_button_color) 
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.left = self.screen_rect.left + 50
        self.text_rect.top =  self.screen_rect.top + 130
        self.screen.blit(self.text_surface, self.text_rect)
        pygame.display.flip()
        sleep(4)
        