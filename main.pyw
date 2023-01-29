import pygame
import random

width = 500
height = 700

size = 25

win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Tetris")

red = pygame.transform.scale(pygame.image.load("tiles/red.png"),(size,size))
cyan = pygame.transform.scale(pygame.image.load("tiles/cyan.png"),(size,size))
green = pygame.transform.scale(pygame.image.load("tiles/green.png"),(size,size))
yellow = pygame.transform.scale(pygame.image.load("tiles/yellow.png"),(size,size))
orange = pygame.transform.scale(pygame.image.load("tiles/orange.png"),(size,size))
blue = pygame.transform.scale(pygame.image.load("tiles/blue.png"),(size,size))
purple = pygame.transform.scale(pygame.image.load("tiles/purple.png"),(size,size))

colors = [red,cyan,green,yellow,orange,blue,purple]

class O_Block():
    def __init__(self,x,y,c):
        self.x = [x,x+1,x+1,x]
        if x + 1 == width//size:
            self.x = [x-1,x,x,x-1]
        self.y = [y,y,y+1,y+1]
        self.c = c
        self.type = "O"
        self.dead = False
        self.blocked = False
        self.dblocked = False
        self.lblocked = False
        self.rblocked = False
        self.ddblocked = False
        self.show = [1,1,1,1]
        self.id = random.randint(-100000000000000000000,100000000000000000000)

    def update(self,win,blocks):
        self.lblocked = False
        self.rblocked = False
        self.dblocked = False
        self.ddblocked = False
        if not self.dead:
            for block in blocks:
                if block.dead and self.id != block.id:
                    for i in range(4):
                        for j in range(4):
                            if self.y[i] + 1 == block.y[j] and self.x[i] == block.x[j]:
                                self.blocked = True
            
            if self.y[2] + 1 >= height//size:
                self.blocked = True

            if not self.blocked:
                self.y = [self.y[0]+1,self.y[1]+1,self.y[2]+1,self.y[3]+1]

            for block in blocks:
                if block.dead and self.id != block.id:
                    for i in range(4):
                        for j in range(4):
                            if self.y[i] + 1 == block.y[j] and self.x[i] == block.x[j] or self.y[2] + 1 >= height//size:
                                self.dblocked = True
                            if self.y[i] + 2 == block.y[j] and self.x[i] == block.x[j] or self.y[2] + 2 >= height//size:
                                self.ddblocked = True
                            if self.y[i] == block.y[j] and self.x[i] + 1 == block.x[j]:
                                self.rblocked = True
                            if self.y[i] == block.y[j] and self.x[i] - 1 == block.x[j]:
                                self.lblocked = True

            if not self.blocked:                      
                keys = pygame.key.get_pressed()
                if keys[pygame.K_d] and self.x[1] + 1 != width//size and not self.rblocked:
                    self.x = [self.x[0]+1,self.x[1]+1,self.x[2]+1,self.x[3]+1]
                if keys[pygame.K_a] and self.x[0] - 1 != -1  and not self.lblocked:
                    self.x = [self.x[0]-1,self.x[1]-1,self.x[2]-1,self.x[3]-1]
                if keys[pygame.K_s] and self.y[2] + 1 != height//size and not self.dblocked:
                    self.y = [self.y[0]+1,self.y[1]+1,self.y[2]+1,self.y[3]+1]
                    if not self.ddblocked:
                        self.y = [self.y[0]+1,self.y[1]+1,self.y[2]+1,self.y[3]+1]
            else:
                self.dead = True

        if self.dead:
            self.dblocked = False
            for block in blocks:
                if block.dead and self.id != block.id:
                    if self.show == [1,1,1,1]:
                        for i in range(4):
                            for j in range(4):
                                if self.y[i] + 1 == block.y[j] and self.x[i] == block.x[j]:
                                    self.dblocked = True
                    elif self.show == [1,1,0,0]:
                        for i in range(2):
                            for j in range(4):
                                if self.y[i] + 1 == block.y[j] and self.x[i] == block.x[j]:
                                    self.dblocked = True

            if self.show == [1,1,0,0]:
                if self.y[1] + 1 >= height//size:
                    self.dblocked = True
            elif self.show == [1,1,1,1]:
                if self.y[2] + 1 >= height//size:
                    self.dblocked = True

            if not self.dblocked:
                self.y = [self.y[0]+1,self.y[1]+1,self.y[2]+1,self.y[3]+1]

        for i in range(4):
            if self.show[i] == 1:
                win.blit(self.c,(self.x[i]*size,self.y[i]*size))



class I_Block():
    def __init__(self,x,y,c):
        self.x = [x,x+1,x+2,x+3]
        self.y = [y,y,y,y]
        self.c = c
        self.type = "I"
        self.dead = False
        self.blocked = False
        self.dblocked = False
        self.lblocked = False
        self.rblocked = False
        self.ddblocked = False
        self.show = [1,1,1,1]
        self.id = random.randint(-100000000000000000000,100000000000000000000)

    def update(self,win,blocks):
        self.lblocked = False
        self.rblocked = False
        self.dblocked = False
        self.ddblocked = False
        if not self.dead:
            for block in blocks:
                if block.dead and self.id != block.id:
                    for i in range(4):
                        for j in range(4):
                            if self.y[i] + 1 == block.y[j] and self.x[i] == block.x[j]:
                                self.blocked = True
            
            if self.y[2] + 1 >= height//size:
                self.blocked = True

            if not self.blocked:
                self.y = [self.y[0]+1,self.y[1]+1,self.y[2]+1,self.y[3]+1]

            for block in blocks:
                if block.dead and self.id != block.id:
                    for i in range(4):
                        for j in range(4):
                            if self.y[i] + 1 == block.y[j] and self.x[i] == block.x[j] or self.y[2] + 1 >= height//size:
                                self.dblocked = True
                            if self.y[i] + 2 == block.y[j] and self.x[i] == block.x[j] or self.y[2] + 2 >= height//size:
                                self.ddblocked = True
                            if self.y[i] == block.y[j] and self.x[i] + 1 == block.x[j]:
                                self.rblocked = True
                            if self.y[i] == block.y[j] and self.x[i] - 1 == block.x[j]:
                                self.lblocked = True

                            

            if not self.blocked:                      
                keys = pygame.key.get_pressed()
                if keys[pygame.K_d] and self.x[3] + 1 != width//size and not self.rblocked:
                    self.x = [self.x[0]+1,self.x[1]+1,self.x[2]+1,self.x[3]+1]
                if keys[pygame.K_a] and self.x[0] - 1 != -1  and not self.lblocked:
                    self.x = [self.x[0]-1,self.x[1]-1,self.x[2]-1,self.x[3]-1]
                if keys[pygame.K_s] and self.y[3] + 1 != height//size and not self.dblocked:
                    self.y = [self.y[0]+1,self.y[1]+1,self.y[2]+1,self.y[3]+1]
                    if not self.ddblocked:
                        self.y = [self.y[0]+1,self.y[1]+1,self.y[2]+1,self.y[3]+1]
            else:
                self.dead = True

        if self.dead:
            self.dblocked = False
            for block in blocks:
                if block.dead and self.id != block.id:
                    for i in range(4):
                        for j in range(4):
                            if self.y[i] + 1 == block.y[j] and self.x[i] == block.x[j]:
                                self.dblocked = True

            if self.y[2] + 1 == height//size:
                self.dblocked = True

            if not self.dblocked:
                self.y = [self.y[0]+1,self.y[1]+1,self.y[2]+1,self.y[3]+1]

        for i in range(4):
            if self.show[i] == 1:
                win.blit(self.c,(self.x[i]*size,self.y[i]*size))

def draw_win(win,blocks):
    win.fill((255,255,255))
    have = False
    for block in blocks:
        if block.dead:
            for y in block.y:
                if y == 0:
                    blocks.clear()
    for block in blocks:
        block.update(win,blocks)
        if not block.dead:
            have = True

    for i in range(height//size):
        line = 0
        for block in blocks:
            if block.dead:
                for y in block.y:
                    if y == i:
                        line += 1
        if line >= width//size:
            for block in blocks:
                if block.dead:
                    for k, y in enumerate(block.y):
                        if y == i and block.show[k] == 1:
                            block.show[k] = 0

    for block in blocks:
        if block.dead:
            if all(show == 0 for show in block.show):
                blocks.remove(block)
    if not have:
        choice = random.randint(1,2)
        if choice == 1:
            blocks.append(O_Block(random.randint(0,(width//size)-2),0,random.choice(colors)))
        elif choice == 2:
            blocks.append(I_Block(random.randint(0,(width//size)-4),0,random.choice(colors)))
    pygame.display.update()

blocks = []
blocks.append(O_Block(random.randint(0,(width//size)-1),0,random.choice(colors)))
run = True
clock = pygame.time.Clock()
while run:
    clock.tick(5)
    draw_win(win,blocks)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
exit()
