import pygame as py
import time
import random

py.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

dis = py.display.set_mode((dis_width, dis_height))
py.display.set_caption("Snake Game")

clock = py.time.Clock()

snake_block = 10
snake_speed = 15

font_style = py.font.SysFont("bahnschrift", 25)
score_font = py.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        py.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    game_over = False
    game_close = False
    
    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close == True:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            Your_score(Length_of_snake - 1)
            py.display.update()

            for event in py.event.get():
                if event.type == py.KEYDOWN:
                    if event.key == py.K_q:
                        game_over = True
                        game_close = False
                    if event.key == py.K_c:
                        gameLoop()

        for event in py.event.get():
            if event.type == py.QUIT:
                game_over = True
            if event.type == py.KEYDOWN:
                if event.key == py.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == py.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == py.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == py.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
             game_close = True

        x1 += x1_change
        y1 += y1_change
        
        #dis.fill(white)
        dis.fill(blue)
        
        #py.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        py.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        
        #py.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
       
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        py.display.update()

        if x1 == foodx and y1 == foody:
            #print("Yummy!!")
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        clock.tick(snake_speed)

    py.quit()
    quit()

gameLoop()

#snake_block = 10

#x1_change = 0
#y1_change = 0

#clock = py.time.Clock()
#snake_speed = 30

#font_style = py.font.SysFont(None, 50)
'''
def message(msg, color):
    msg = font_style.render(msg, True, color)
    dis.blit(msg, [dis_width / 2, dis_height / 2])

while not game_over:
    for event in py.event.get():
        if event.type == py.QUIT:
            game_over = True
        if event.type == py.KEYDOWN:
            if event.key == py.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == py.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == py.K_UP:
                x1_change = 0
                y1_change = -snake_block
            elif event.key == py.K_DOWN:
                x1_change = 0
                y1_change = snake_block
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True

    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    py.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
    py.display.update()

    clock.tick(snake_speed)

message('You lost', red)
py.display.update()
time.sleep(2)

py.quit()
quit()'''