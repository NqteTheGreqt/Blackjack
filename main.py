from typing import Literal
import pygame
import random
import os

directory = 'Playing Cards'

delimiter = chr(92)

FileName = 'Id' + delimiter + 'TypeOfMachine' + delimiter + 'year' + '_' + 'month' + delimiter + 'year' + '_' + 'month' + '_' + 'day' + '.csv'

print(FileName)

# Setting up screen
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Blackjack")
icon = pygame.image.load(r'Playing Cards\JS.png')
pygame.display.set_icon(icon)

# Setting up card images
cards = []
for filename in os.listdir(directory):
    if filename.endswith(".png") and not filename.startswith("back"):

        image = os.path.join(directory, filename)

        cards.append(image)

random.shuffle(cards)
# Setting up player's cards
player_cards = []
player_cards.append(cards [0])
cards.pop(0)
player_cards.append(cards [0])
cards.pop(0)


print(player_cards)

card_img = pygame.image.load(r'Playing Cards\back.png')

player_money = 500
font = pygame.font.Font('freesansbold.ttf', 32)


def show_money():
    money_text = font.render("Stack: $" + str(player_money), True, (0, 0, 0))
    screen.blit(money_text, (30, 550))

def show_cards(player_cards):
    x = 100
    y = 100
    while player_cards:
        image = pygame.image.load(player_cards[0])
        player_cards.pop(0)
        screen.blit(image, (x, y))
        x += 200


running = True
while running:
    screen.fill((0, 153, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    show_money()
    show_cards(player_cards)
    pygame.display.update()