import pygame
import time
import random
pygame.init()

dis_width=800
dis_height=600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.update()
pygame.display.set_caption('Snake igra by Teo')


white=(255,255,255)
blue=(50, 168, 162)
red=(168, 50, 50)
black=(0,0,0)

clock=pygame.time.Clock()
snake_speed=15
snake_block=10

font_style=pygame.font.SysFont(None,25)
score_font=pygame.font.SysFont("comicsansms",35)

def our_snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,black,[x[0],x[1],snake_block,snake_block])


def message(msg,color):
    mesg=font_style.render(msg,True,color)
    dis.blit(mesg,[dis_width/5, dis_height/2])

def gameLoop():
    game_over = False
    game_close = False
    x1_change = 0
    y1_change = 0
    x1 = dis_width / 2
    y1 = dis_height / 2
    snake_list = []
    length_of_snake = 1
    foodx = round(random.randrange(0, dis_width-snake_block) / 10.0) * 10
    foody = round(random.randrange(0, dis_width-snake_block) / 10.0) * 10

    while not game_over:
        while game_close == True:
            dis.fill(white)
            message("Izgubio si stisni Q da izades iz igrice ili C da igras opet!!!",red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                if event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                if event.key == pygame.K_RIGHT:
                    y1_change = 0
                    x1_change = snake_block
                if event.key == pygame.K_LEFT:
                    y1_change = 0
                    x1_change = -snake_block
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            print("Pojedeno!!")
        clock.tick(snake_speed)
        #message("A jebiga", red)
        #pygame.display.update()
        #time.sleep(2)
    pygame.quit()
    quit()

gameLoop()