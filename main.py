import pygame
import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  Player.containers = (updatable, drawable)
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  asteroids = pygame.sprite.Group()
  Asteroid.containers = (asteroids, updatable, drawable)

  AsteroidField.containers = (updatable)

  asteroidField = AsteroidField()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    screen.fill("black")
    for obj in updatable:
      obj.update(dt)
    for obj in asteroids:
      if player.overlapping(obj):
        print("Game over!")
        sys.exit()

    for obj in drawable:
      obj.draw(screen)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()
