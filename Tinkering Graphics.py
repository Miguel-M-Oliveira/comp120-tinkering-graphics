import pygame
import os
pygame.init

screen = pygame.display.set_mode((300, 300))

print("Select a terrain texture:")


def option(x):
    print(x)


#listing all texture options

option("grass_light")
option("grass_dark")
option("dirt_smooth")
option("dirt_rocky")
option("dirt_wet")
option("dirt_dry")
option("leaves_hedge")
option("leaves_ivy")
option("leaves_autumn")
option("marble_1")
option("marble_2")
option("wood_1")
option("wood_2")
option("wood_3")
option("snow")
option("ice")

choice = input()

#user's selection being used to fetch correct image.
#couldn't think of way to make this simpler; couldn't fetch image when its name was stored in a variable.

if choice in "grass_light":
    picture = pygame.image.load('grass_light.png')
elif choice in "grass_dark":
    picture = pygame.image.load('grass_dark.png')
elif choice in "dirt_smooth":
    picture = pygame.image.load('dirt_smooth.png')
elif choice in "dirt_rocky":
    picture = pygame.image.load('dirt_rocky.png')
elif choice in "dirt_wet":
    picture = pygame.image.load('dirt_wet.png')
elif choice in "dirt_dry":
    picture = pygame.image.load('dirt_dry.png')
elif choice in "leaves_hedge":
    picture = pygame.image.load('leaves_hedge.png')
elif choice in "leaves_ivy":
    picture = pygame.image.load('leaves_ivy.png')
elif choice in "leaves_autumn":
    picture = pygame.image.load('leaves_autumn.png')
elif choice in "marble_1":
    picture = pygame.image.load('marble_1.png')
elif choice in "marble_2":
    picture = pygame.image.load('marble_2.png')
elif choice in "wood_1":
    picture = pygame.image.load('wood_1.png')
elif choice in "wood_2":
    picture = pygame.image.load('wood_2.png')
elif choice in "wood_3":
    picture = pygame.image.load('wood_3.png')
elif choice in "snow":
    picture = pygame.image.load('snow.png')
elif choice in "ice":
    picture = pygame.image.load('ice.png')
else:
    print("Incorrect input. Please make sure the name you enter is exactly equal to how it's spelt in the list above.")


while True:
    screen.blit(picture, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()

