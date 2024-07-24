import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics, and a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Set the background color.
    bg_color = (230, 230, 230)

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    alien_bullets = Group() # Maximum number of alien bullets allowed.
    
    # Timing setup
    last_update_time = pygame.time.get_ticks()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        gf.check_events(
            ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, alien_bullets
        )

        current_time = pygame.time.get_ticks()
        time_since_last_update = current_time - last_update_time

        if stats.game_active:
            ship.update()
            gf.fire_alien_bullets(ai_settings, screen, aliens, alien_bullets)
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets)
            if time_since_last_update >= 1000:  # 1000 milliseconds = 1 second
               for alien in aliens:
                   gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
               last_update_time = current_time  # Reset the timer

        gf.update_screen(
            ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, alien_bullets
        )

run_game()