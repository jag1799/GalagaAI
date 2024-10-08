import pygame
from pygame.sprite import Sprite

"""A class to represent a single alien in the fleet."""
class Alien(Sprite):
    

    """Initialize the alien, and set its starting position."""
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
    
        # Load the alien image.
        self.image = pygame.image.load("images/alien.bmp")
        
        # Assuming you have the width and height of the spaceship
        self.ship_width = 100
        self.ship_height = 100
    
        # Resize the alien image to match the spaceship size.
        self.image = pygame.transform.scale(self.image, (self.ship_width, self.ship_height))
        
        self.rect = self.image.get_rect()
    
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
    
        # Store the alien's exact position.
        self.x = float(self.rect.x)
        
        self.direction_change_count = 0  # Counts how many times the direction has changed


    """Return True if alien is at edge of screen."""
    def check_edges(self):
        
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


    """Move the alien right or left."""
    def update(self): 
        self.x += self.ai_settings.grid_size * self.ai_settings.fleet_direction
        self.rect.x = self.x  
        self.ai_settings.updated_this_iteration =True


    """Draw the alien at its current location."""
    def blitme(self):
        self.screen.blit(self.image, self.rect)
