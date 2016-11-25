#I have wached the tutorials form THEWEWBOSTON website
#And used Pygame documentation
#Here are links to the sites above
#https://thenewboston.com/videos.php?cat=120&video=21649
#http://www.pygame.org/docs/

arena = [['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w', 0],['w',0,'e1D',0,0,0,0,0,0,0,'m',0,0,0,0,'w',0,'e2D',0,'w',0],['w','a',0,0,0,0,0,0,0,0,0,0,0,0,0,'w','a',0,0,'w',0],['w','w',0,0,0,0,0,0,'w','w',0,0,0,0,0,'w','w','w',0,'w',0],['w','w','w','w','w',0,0,0,0,0,0,0,0,'w',0,0,0,0,0,'w'],['w',0,0,0,'w','w','w',0,0,0,0,0,0,'w',0,0,0,0,0,'w',0],['w',0,0,0,0,0,'w',0,0,0,'w',0,0,0,'m',0,0,0,0,'w',0],['w',0,0,0,0,0,0,0,0,0,'w',0,0,0,'w','w','w','w','w','w',0],['w','w','w','w',0,0,0,0,0,'a','w','m',0,0,0,0,0,0,0,'w',0],['w','a',0,0,0,0,0,'w','w','w','w','w','w','w',0,0,0,0,'a','w',0],['w',0,0,0,0,0,0,0,0,'m','w','a',0,0,0,0,0,0,0,'w'],['w',0,0,'w','w',0,0,0,0,0,'w',0,0,0,0,0,0,0,0,'w',0],['w',0,0,0,0,0,0,0,0,0,'w',0,0,0,0,0,'w','w','w','w',0],['w',0,0,0,'m',0,0,'w',0,0,0,0,0,0,0,0,0,0,0,'w',0],['w',0,0,0,0,0,0,'w',0,0,0,0,0,'w','w',0,0,0,0,'w',0],['w','w','w','w','w',0,0,'w',0,0,0,0,0,0,'w',0,0,0,0,'w',0],['w','a',0,0,0,0,0,'w',0,0,0,0,0,0,'w',0,0,0,0,'w',0],['w',0,0,0,0,0,0,'w',0,0,0,0,0,0,'w',0,0,0,0,'w',0],['w',0,'uF',0,0,0,0,'w',0,0,0,0,0,0,'w',0,0,'e3F',0,'w',0],['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w',0]]

import pygame
pygame.init()
#some important things that I have included
col_sound = pygame.mixer.Sound("collect.wav")
st_sound = pygame.mixer.Sound('stSound.wav')

AItankd = pygame.image.load('AItankd.bmp')
AItankf = pygame.image.load('AItankf.bmp')
AItankl = pygame.image.load('AItankl.bmp')
AItankr = pygame.image.load('AItankr.bmp')
ammo = pygame.image.load('ammo.bmp')
bg = pygame.image.load('bg.bmp')
bullet = pygame.image.load('bullet.bmp')
explosion = pygame.image.load('explosion.bmp')
mine = pygame.image.load('mine.bmp')
tankd = pygame.image.load('tankd.bmp')
tankf = pygame.image.load('tankf.bmp')
tankl = pygame.image.load('tankl.bmp')
tankr = pygame.image.load('tankr.bmp')
wall = pygame.image.load('wall.bmp')

size = (500,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tanks")

#I have changed the position of the line below to be more efficant in the whole code
clock = pygame.time.Clock()

userPosition = [3, 19]
e1Position = [2, 3]
e2Position = [2, 18]
e3Position = [18, 19]

def nextPosition(direction):
    if direction == 'f':
        tentativePosition = [userPosition[0], userPosition[1] - 1]
    elif direction == 'd':
        tentativePosition = [userPosition[0], userPosition[1] + 1]
    elif direction == 'l':
        tentativePosition = [userPosition[0] - 1, userPosition[1]]
    elif direction == 'r':
        tentativePosition = [userPosition[0] + 1, userPosition[1]]
    if tentativePosition[0] > 20 or tentativePosition[1] > 20 or arena[tentativePosition[1] - 1][tentativePosition[0] - 1] == 'w':
        return None
    else:
        return tentativePosition 
#my own code  
def ePos(direction):
    if direction == 'f':
        tentativePosition = [e3Position[0], e3Position[1] - 1] 
    elif direction == 'd':
        tentativePosition = [e3Position[0], e3Position[1] + 1] 
    elif direction == 'l':
        tentativePosition = [e3Position[0] - 1, e3Position[1]]
    elif direction == 'r': 
        tentativePosition = [e3Position[0] + 1, e3Position[1]] 
    if tentativePosition[0] > 20 or tentativePosition[1] > 20 or arena[tentativePosition[1] - 1][tentativePosition[0] - 1] == 'w': #if the position in either X or Y axises is bigger than 20 or if you are next to a wall
        return None 
    else: 
        return tentativePosition 
#end

def pixelPosition(x, y):
    xPixel = (x - 1)*25
    yPixel = (y - 1)*25
    return [xPixel, yPixel]

xCoord = 0
yCoord = 0
x = 0
y = 0
while x <= 19:
        while y <= 19:
            if arena[x][y] == 'e1D' or arena[x][y] == 'e2D' or arena[x][y] == 'e3D':
                screen.blit(AItankd,(xCoord, yCoord))
            elif arena[x][y] == 'e1F' or arena[x][y] == 'e2F' or arena[x][y] == 'e3F':
                screen.blit(AItankf,(xCoord, yCoord))
            elif arena[x][y] == 'e1L' or arena[x][y] == 'e2L' or arena[x][y] == 'e3L':
                screen.blit(AItankl,(xCoord, yCoord))
            elif arena[x][y] == 'e1R' or arena[x][y] == 'e2R' or arena[x][y] == 'e3R':
                screen.blit(AItankr,(xCoord, yCoord))
            elif arena[x][y] == 'a':
                screen.blit(ammo,(xCoord, yCoord))
            elif arena[x][y] == 0:
                screen.blit(bg,(xCoord, yCoord))
            elif arena[x][y] == 'b':
                screen.blit(bullet,(xCoord, yCoord)) and pygame.mixer.Sound.play(col_sound)
            elif arena[x][y] == 'e':
                screen.blit(explosion,(xCoord, yCoord))
            elif arena[x][y] == 'm':
                pygame.mixer.Sound.play(st_sound)
                screen.blit(mine,(xCoord, yCoord))
            elif arena[x][y] == 'uD':
                screen.blit(tankd,(xCoord, yCoord))
            elif arena[x][y] == 'uF':
                screen.blit(tankf,(xCoord, yCoord))
            elif arena[x][y] == 'uL':
                screen.blit(tankl,(xCoord, yCoord))
            elif arena[x][y] == 'uR':
                screen.blit(tankr,(xCoord, yCoord))
            elif arena[x][y] == 'w':
                screen.blit(wall,(xCoord, yCoord))
            xCoord = xCoord + 25
            if xCoord == 1000:
                xCoord = 0
            y = y + 1
            if y == 20:
                break
        xCoord = 0
        x = x + 1
        yCoord = yCoord + 25
        y = 0

running = True 
clock = pygame.time.Clock()
loop = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if nextPosition('f') == None:
                    pass
                else:
                    screen.blit(bg,(pixelPosition(userPosition[0], userPosition[1])[0], pixelPosition(userPosition[0], userPosition[1])[1]))
                    userPosition = nextPosition('f')
                    screen.blit(tankf,(pixelPosition(userPosition[0], userPosition[1])[0], pixelPosition(userPosition[0], userPosition[1])[1]))
            elif event.key == pygame.K_d:
                if nextPosition('r') == None:
                    pass
                else:
                    screen.blit(bg,(pixelPosition(userPosition[0], userPosition[1])[0], pixelPosition(userPosition[0], userPosition[1])[1]))
                    userPosition = nextPosition('r')
                    screen.blit(tankr,(pixelPosition(userPosition[0], userPosition[1])[0], pixelPosition(userPosition[0], userPosition[1])[1]))
            elif event.key == pygame.K_s:
                if nextPosition('d') == None:
                    pass
                else:
                    screen.blit(bg,(pixelPosition(userPosition[0], userPosition[1])[0], pixelPosition(userPosition[0], userPosition[1])[1]))
                    userPosition = nextPosition('d')
                    screen.blit(tankd,(pixelPosition(userPosition[0], userPosition[1])[0], pixelPosition(userPosition[0], userPosition[1])[1]))
            elif event.key == pygame.K_a:
                if nextPosition('l') == None:
                    pass
                else:
                    screen.blit(bg,(pixelPosition(userPosition[0], userPosition[1])[0], pixelPosition(userPosition[0], userPosition[1])[1]))
                    userPosition = nextPosition('l')
                    screen.blit(tankl,(pixelPosition(userPosition[0], userPosition[1])[0], pixelPosition(userPosition[0], userPosition[1])[1]))
                    #my own code

                if ePos('f') == None: 
                    pass 
                else: 
                    for i in range(5): 
                        screen.blit(bg,(pixelPosition(e3Position[0], e3Position[1])[0], pixelPosition(e3Position[0], e3Position[1])[1])) #we delete the blank space in the block we are moving onto
                        e3Position = ePos('f') 
                        screen.blit(AItankf,(pixelPosition(e3Position[0], e3Position[1])[0], pixelPosition(e3Position[0], e3Position[1])[1])) #we delete the tank on previous the position
                        pygame.display.update()
                        clock.tick(3)
                        if i == 4: 
                            for ia in range(6): 
                                screen.blit(bg,(pixelPosition(e3Position[0], e3Position[1])[0], pixelPosition(e3Position[0], e3Position[1])[1]))
                                e3Position = ePos('l')
                                screen.blit(AItankl,(pixelPosition(e3Position[0], e3Position[1])[0], pixelPosition(e3Position[0], e3Position[1])[1]))
                                pygame.display.update()
                                clock.tick(7)
                                if ia == 5:
                                    for ib in range(3):
                                        screen.blit(bg,(pixelPosition(e3Position[0], e3Position[1])[0], pixelPosition(e3Position[0], e3Position[1])[1]))
                                        e3Position = ePos('f')
                                        screen.blit(AItankf,(pixelPosition(e3Position[0], e3Position[1])[0], pixelPosition(e3Position[0], e3Position[1])[1]))
                                        pygame.display.update()
                                        clock.tick(10)
                                        if ib == 2:
                                            pygame.mixer.Sound.play(col_sound)
                    #end

    pygame.display.flip()
    clock.tick(60)

pygame.quit()





