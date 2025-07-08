from pygame import*
import sys
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
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
class Enemy(GameSprite):
    def __init__(self, img, x, y, x_speed, width, height):
        GameSprite.__init__(self, img, x, y, width, height)
        self.x_speed = x_speed
    def update(self):
        if self.rect.x <= 420:
            self.rect.x += self.x_speed
        if self.rect.x >= width - 50:
            self.rect.x -= self.x_speed
player = Player('hero.png', 50, 50, 0,0, 50, 50)
walls = sprite.Group()
wall1 = GameSprite('platform_h.png', 200, 100, 300, 50)
walls.add(wall1)
wall2 = GameSprite('platform_v.png', 400, 200,50, 300)
walls.add(wall2)
wall3 = GameSprite('platform_h.png', 100, 400, 300, 50)
walls.add(wall3)
enemy = Enemy('enemy.png', width - 80, 150, 5, 80,80)
clock = time.Clock()
running = True
while running:
    window.fill((244, 0, 161))
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == KEYDOWN:
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
    enemy.update()
    for wall in walls:
        wall.reset()
    player.reset()
    enemy.reset()
    display.update()
    clock.tick(60)
quit()
sys.exit()






