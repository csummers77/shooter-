import pygame
from pygame.sprite import Group, groupcollide

from player import Player
from badg import Badg
from bullets import Bullets

pygame.init()


screen_size = (1000,800)
background_color = (82,111,53)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Night Hawk")

the_player = Player('hero.png',100,100,screen)

Badg = Badg(screen)

Badgs = Group()

Badgs.add(Badg)

bullets = Group()


game_on = True

while game_on: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_on = False
		elif event.type == pygame.KEYDOWN:
			print event.key
			if event.key == 273:
				the_player.should_move("up",True)
			elif event.key == 274:
				the_player.should_move("down",True)
			if event.key == 275:
				the_player.should_move("right",True)
			elif event.key == 276:
				the_player.should_move("left",True)
			elif event.key == 32:

				new_bullets = bullets(screen, the_player, 1)
				bulletss.add(new_bullets)
				new_bullets = bullets(screen, the_player, 3)
				bulletss.add(new_bullets)
		elif event.type == pygame.KEYUP:
			if event.key == 273:
				the_player.should_move("up",False)
			elif event.key == 274:
				the_player.should_move("down",False)
			if event.key == 275:
				the_player.should_move("right",False)
			elif event.key == 276:
				the_player.should_move("left",False)


	screen.fill(background_color)

	for Badg in Badgs:
		Badg.update_me(the_player)
		Badg.draw_me()


	the_player.draw_me()

	for bullets in bullets:
		bullets.update()
		bullets.draw_bullets()


	bullets_hit = groupcollide(bullets,Badgs,True,True)
	pygame.display.flip()
