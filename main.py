import pygame 
from random import *
pygame.init()

screen_w = 600
screen_h = 400
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('WINER')

    
red = (255, 0, 0)

file = open("record.txt", "r+")
record = file.read()

label = pygame.font.Font('font.ttf', 20)
score = 0
lab3 = label.render(f'SCORE {score}', 0, (193, 196, 199))
lose = label.render(f'record: {record}', 0, (193, 196, 199))
over = pygame.image.load('over.png').convert()
fon = pygame.image.load('fon.png').convert()
bom = pygame.image.load('bomb.png').convert_alpha()
sc = pygame.image.load('sc.png').convert_alpha()

labe = pygame.font.Font('font.ttf', 40)
black = (0, 0, 0)
lab = labe.render(f'To restart, press "R"', 0, (black))

lab2 = labe.render(f'To exit, press "Q"', 0, (black))


white = (255, 255, 255)
blue = (0, 255, 0)
x, y = screen_w//2, screen_h-20
ball_x, ball_y = randint(4, screen_w - 15), -16
t = 1;vin = 1;upd = 1;gold = 0


while upd:
    if vin:
        screen.blit(fon, [0, 0])
        screen.blit(bom, (ball_x, ball_y))
        screen.blit(label.render(f'SCORE {score}', 0, (193, 196, 199)), [10, 40])
        
        screen.blit(sc, [x, y])
        screen.blit(sc, [x+20, y])
        screen.blit(sc, [x+40, y])
        screen.blit(sc, [x+60, y])
        screen.blit(sc, [x+80, y])

        if ball_y < 0:t = 1

        if y == int(ball_y + 10) and (x - 10 <= ball_x and ball_x <= x + 90) and t == 1:
            score += 1;t = 0
            ball_y = -15
            ball_x = randint(4, screen_w - 20)

        
        screen.blit(lose, (10, 10))
        ball_y += 0.2
        
        vin = (y + 20 > int(ball_y))
    
    else:
        screen.blit(over, [0, 0])

        key = pygame.key.get_pressed()
        
        if key[pygame.K_r]:
            vin = 1;ball_y = -15
            ball_x = randint(4, screen_w - 20)
            score = 0
        elif key[pygame.K_q]:upd = False
        screen.blit(lab, (10, 10))
        screen.blit(lab2, (10, 70))
        if int(record) < score:
            screen.blit(labe.render(f'Wow, a new record! {score}', 0, (black)), (10, 130))
            gold = 1
            if key[pygame.K_r]:vin = 1;ball_y = -15;ball_x = randint(4, screen_w - 20);score = 0
    


    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
        
            pygame.quit();upd = 0
            
        if event.type == pygame.KEYDOWN and vin:
            if event.key == pygame.K_LEFT and x >= 30:x -= 30
            if event.key == pygame.K_RIGHT and x < screen_w - 120: x += 33

if gold:
    file.seek(0)
    file.truncate()
    file.write(str(score))
    file.close()
else:
 file.close()