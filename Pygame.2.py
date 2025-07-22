from pygame import*
import sys

from pygame.constants import K_SPACE

width = 800
height = 600
window = display.set_mode((width, height))
display.set_caption('Лабиринт')
window.fill((244, 0, 161))
class GameSprite(sprite.Sprite):
    def __init__(self, img, x,y, width, height):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(img),(width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self, img, x, y, x_speed, y_speed, width, height):
        GameSprite.__init__(self, img, x, y, width, height)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        if self.rect.x >= 0 and self.x_speed < 0 or self.rect.x <= width - 50 and self.x_speed >= 0:
            self.rect.x += self.x_speed
            platforms_touched = sprite.spritecollide(self, walls, False)
            if self.x_speed > 0 and platforms_touched:
                self.rect.x -= 5
            elif self.x_speed <= 0 and platforms_touched:
                self.rect.x += 5
        if self.rect.y >= 0 and self.y_speed < 0 or self.rect.y <= height - 50 and self.y_speed >= 0:
            self.rect.y += self.y_speed
            platforms_touched = sprite.spritecollide(self, walls, False)
            if self.y_speed > 0 and platforms_touched:
                self.rect.y -= 5
            elif self.y_speed <= 0 and platforms_touched:
                self.rect.y += 5
class Enemy(GameSprite):
    def __init__(self, img, x, y, x_speed, width, height):
        GameSprite.__init__(self, img, x, y, width, height)
        self.x_speed = x_speed
    def update(self):
        if self.rect.x <= 420:
            self.flag = True
        if self.rect.x > width - 50:
            self.flag = False
        if self.flag:
            self.rect.x += self.x_speed
        else:
            self.rect.x -= self.x_speed
class Bullet(GameSprite):
    def __init__(self, img, x, y, x_speed, width, height):
        GameSprite.__init__(self, img, x, y, width, height)
        self.x_speed = x_speed
    def update(self):
        self.rect.x += self.x_speed

dragon = GameSprite('dragon (1).png', 600, 400,100, 100)
player = Player('hero.png', 50, 50, 0,0, 50, 50)
walls = sprite.Group()
wall1 = GameSprite('platform_h.png', 200, 100, 300, 50)
walls.add(wall1)
wall2 = GameSprite('platform_v.png', 400, 210,50, 300)
walls.add(wall2)
wall3 = GameSprite('platform_h.png', 100, 400, 300, 50)
walls.add(wall3)
enemy = Enemy('enemy.png', 400, 150, 2, 50,50)
enemies = sprite.Group()
enemies.add(enemy)
clock = time.Clock()
running = True
bullets = sprite.Group()
while running:
    clock.tick(60)
    window.fill((244, 0, 161))
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                bullet = Bullet('dragon (2).png', player.rect.x + 55, player.rect.y + 5, 5,50,50)
                bullets.add(bullet)
                bullet1 = Bullet('dragon (2).png', player.rect.x + 58, player.rect.y + 7, 5,50,50)
                bullets.add(bullet1)
                sprite.groupcollide(enemies, bullets, True, True)
            if e.key == K_LEFT:
                player.x_speed = -5
            if e.key == K_RIGHT:
                player.x_speed = 5
            if e.key == K_UP:
                player.y_speed = -5
            if e.key == K_DOWN:
                player.y_speed = 5
        if e.type == KEYUP:
            if e.key in [K_LEFT, K_RIGHT]:
                player.x_speed = 0
            if e.key in [K_UP, K_DOWN]:
                player.y_speed = 0
    player.update()
    enemies.update()
    enemies.draw(window)
    walls.draw(window)
    bullets.update()
    bullets.draw(window)
    player.reset()
    dragon.reset()
    if sprite.collide_rect(player, dragon):
        window.blit(transform.scale(image.load('game.jpg'),(width, height)), (0,0))
        break
    if sprite.collide_rect(player, enemy):
        window.blit(transform.scale(image.load('game2.png'),(width, height)), (0,0))
        break
    display.update()
display.update()





