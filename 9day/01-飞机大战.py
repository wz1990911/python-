import pygame
from GameSprite import *
pygame.init()
screen = pygame.display.set_mode((480,700))
bg = pygame.image.load("./images/background.png")
hero = pygame.image.load("./images/hero1.png")
rect = pygame.Rect(150,500,102,126)
enemy1 = GameSprite ("./images/enemy-1.gif")
enemy2 = GameSprite ("./images/enemy-1.gif",2)
enemy2.rect.x = 200
group = pygame.sprite.Group(enemy1,enemy2)#创建一个精灵组
#游戏时钟
clock = pygame.time.Clock()
while True:
    clock.tick(60)#一秒刷新60次
    rect.y-=2
    screen.blit(bg,(0,0))
    screen.blit(hero,rect)
    if rect.bottom == 0:
        rect.top = 700
    group.update()#群通知
    group.draw(screen)#绘制屏幕上
    for event in pygame.event.get(): #监听
        if event.type == pygame.QUIT:
            pygame.quit()
    #更新的意思
    pygame.display.update()
pygame.quit()
