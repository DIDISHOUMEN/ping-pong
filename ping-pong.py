from pygame import *
from time import time as timer
class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
  # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# класс главного игрока
class Player(GameSprite):
    # метод для управления спрайтом стрелками клавиатуры
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


win_height = 500
win_width = 600
window = display.set_mode((win_width, win_height))
window.fill((200,255,255))
player_1 = Player('racket.png',30,200,50,150,4)
player_2 = Player('racket.png',520,200,50,150,4)
ball = GameSprite('tenis_ball.png',200,299,50,50,4)

score_1 = 0
score_2 = 0

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render(
    'PLAYER 1 LOSE!!!',True, (180, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE!!!', True,(180,0,0))
scor = font1.render(str(score_1) + ':' + str(score_2), True, (255, 255, 255))


game = True
finish = False
clock = time.Clock()
speed_x = 3
speed_y = 3
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:    
        window.fill((200,255,255))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height -50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(player_1, ball) or sprite.collide_rect(player_2, ball):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            score_2 += 1
            finishtime = timer()
            ball.rect.x = 200
            ball.rect.y = 200
            
        if ball.rect.x > 500:
            finish = True
            score_1 += 1
            finishtime = timer()
            ball.rect.x = 200
            ball.rect.y = 200
        player_1.update_l()
        player_2.update_r()
        player_1.reset()
        player_2.reset()
        ball.reset()
        scor = font1.render(str(score_1) + ':' + str(score_2), True, (255, 255, 255))
        window.blit(scor, (350, 0))
            
    else:
        
        if score_1 >= 3:
            window.blit(lose2, (200, 200))
        elif score_2 >= 3: 
            window.blit(lose1, (200, 200))
        else:
            notime = timer()
            if notime - finishtime > 3:
                finish = False
        
        
    display.update()
    clock.tick(60)

