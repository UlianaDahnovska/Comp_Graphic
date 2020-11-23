import pygame
screen = pygame.display.set_mode((540, 960))
screen.fill((255,255,255))

def dot(screen, color, pos):
    screen.fill(color, (pos, (1, 1)))

try:
	data = open('DS8.txt')
	for line in data:
		split_data = line.split()
		dot(screen, (0, 0, 0), (540 - int(split_data[0]),int(split_data[1])))
except:
	print('Нет доступа к файлу')

pygame.display.flip()
pygame.image.save(screen, 'lab_2.png')

run = True
while run:
	for event in pygame.event.get():
	    if event.type == pygame.QUIT:
	    	run = False
