from pygame.sprite import Sprite
import pygame


class Ghost(Sprite):

    def __init__(self, screen, x_offset, y_offset, file, name):
        super(Ghost, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.size = 30
        self.image = pygame.image.load(file)
        self.image_mode = 0
        self.name = name
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx + x_offset
        self.rect.centery = y_offset
        self.center = float(self.rect.centerx)
        self.last_update_time = 0
        self.cardinal = "West"
        self.current_destination_x = 26
        self.current_destination_y = 26

    def __str__(self):
        return self.name

    def adjust(self, pacman):  # TODO Refactor to 'AI'
        if self.name == "Blinky":
            if self.rect.centery < pacman.rect.centery:
                self.cardinal = "South"
            elif self.rect.centery > pacman.rect.centery:
                self.cardinal = "North"
            elif self.rect.centerx > pacman.rect.centerx:
                self.cardinal = "West"
            elif self.rect.centerx < pacman.rect.centerx:
                self.cardinal = "East"
        if self.name == "Pinky":
            if self.rect.centery < self.current_destination_y:
                self.cardinal = "South"
            elif self.rect.centery > self.current_destination_y:
                self.cardinal = "North"
            elif self.rect.centerx > self.current_destination_x:
                self.cardinal = "West"
            elif self.rect.centerx < self.current_destination_x:
                self.cardinal = "East"

    def blitme(self, settings):
        if pygame.time.get_ticks() - self.last_update_time > 100:
            self.animate()
            # Update cardinal orientation
            if self.cardinal == "North":
                self.move_north(settings)
            elif self.cardinal == "East":
                self.move_east(settings)
            elif self.cardinal == "South":
                self.move_south(settings)
            elif self.cardinal == "West":
                self.move_west(settings)
            elif self.cardinal == "Stopped":
                self.move_stop()

        self.screen.blit(self.image, self.rect)

    def animate(self):
        # Update mouth position
        if self.image_mode == 0:
            # self.image = pygame.image.load('images/pacman/pac1.png')
            self.image_mode = 1
        elif self.image_mode == 1:
            # self.image = pygame.image.load('images/pacman/pac2.png')
            self.image_mode = 2
        elif self.image_mode == 2:
            # self.image = pygame.image.load('images/pacman/pac3.png')
            self.image_mode = 3
        elif self.image_mode == 3:
            # self.image = pygame.image.load('images/pacman/pac0.png')
            self.image_mode = 0
        self.last_update_time = pygame.time.get_ticks()

    def move_north(self, settings):
        self.cardinal = "North"
        self.rect.y -= 1 * settings.speed_ghost

    def move_west(self, settings):
        self.cardinal = "West"
        self.rect.x -= 1 * settings.speed_ghost

    def move_south(self, settings):
        self.cardinal = "South"
        self.rect.y += 1 * settings.speed_ghost

    def move_east(self, settings):
        self.cardinal = "East"
        self.rect.x += 1 * settings.speed_ghost

    def move_stop(self):
        self.cardinal = "Stopped"
        self.rect.x += 0
        self.rect.y += 0
