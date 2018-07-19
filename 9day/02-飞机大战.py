import pygame
from GameSprite import *
class PlanMain():
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        #设置定时器事件 - 每秒创建一架敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(CREATE_BULLET_EVENT,100)
        # 敌机组
        self.enemy_group = pygame.sprite.Group()
    def start_game(self):
        """开始游戏"""

        print("开始游戏...")
        while True:

            # 1. 设置刷新帧率
            self.clock.tick(60)

            # 2. 事件监听
            self.__event_handler()

            # 3. 碰撞检测
            self.__check_collide()

            # 4. 更新精灵组
            self.__update_sprites()

            # 5. 更新屏幕显示
            pygame.display.update()

    def __event_handler(self):
        """事件监听"""
        for event in pygame.event.get():
            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            # 监听子弹
            elif event.type == CREATE_BULLET_EVENT:
                self.hero.fire()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 5
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -5
        else:
            self.hero.speed = 0

    def __check_collide(self):
        """碰撞检测"""
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullet_group,self.enemy_group, True, True)
        # 2. 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            self.hero.kill()
            PlamMain.__game_over()

    def __update_sprites(self):
        """更新精灵组"""
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    def __create_sprites(self):
        '''创建精灵组'''
        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)    
        # 英雄组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    @staticmethod
    def __game_over():
       """游戏结束"""

       print("游戏结束")
       pygame.quit()
       exit()

planmain = PlanMain()
planmain.start_game()
