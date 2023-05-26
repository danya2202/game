import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))

fps = pygame.time.Clock()
#класи
class Pause:
    def __init__(self,filename):
        self.png = pygame.image.load(filename)
    def draw(self, screen):
        screen.blit(self.png, [0, 0, 0])

class Meny:
    def __init__(self,filename):
        self.png = pygame.image.load(filename)
    def draw(self, screen):
        screen.blit(self.png, [0, 0, 0])

class Platforma1:
    def __init__(self, x, y, w, h, filename, speed):
        self.png = pygame.image.load(filename)
        self.rect = pygame.Rect(x, y, w, h)
        self.speed = speed
    def draw(self, screen):
        screen.blit(self.png, [self.rect.x,self.rect.y])

class Platforma2:
    def __init__(self, x, y, w, h, filename, speed):
        self.png = pygame.image.load(filename)
        self.rect = pygame.Rect(x, y, w, h)
        self.speed = speed
    def draw(self, screen):
        screen.blit(self.png, [self.rect.x,self.rect.y])

class Ball:
    def __init__(self, x, y, w, h, filename, speedX, speedY):
        self.png = pygame.image.load(filename)
        self.rect = pygame.Rect(x, y, w, h)
        self.speedX = speedX
        self.speedY = speedY
    def draw(self, screen):
        screen.blit(self.png, [self.rect.x,self.rect.y])
class Phon:
    def __init__(self,filename):
        self.png = pygame.image.load(filename)
    def draw(self, screen):
        screen.blit(self.png, [0, 0])
meny = Meny("menys.png")
def menu(screen):
    fps = pygame.time.Clock()
    meny = Meny("menys.png")
    pauses = Pause("stop.png")
    while True:
        #Обробка події
        menytext = pygame.font.Font(None, 50).render("Нажми SPACE щоб почати", True, [255, 255, 255])
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return(True)    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    return(False)
                    


        #оновлення об'єктів
        
        #відмалювати об'єкти    
        meny.draw(screen)
        screen.blit(menytext, [100, 100])
        pygame.display.flip()
        fps.tick(60)





#надання характеристики
platforms1 = Platforma1(25, 125, 20, 85, "platform1.png", 1)

platforms2 = Platforma2(450, 125, 20, 85, "platform1.png", 1)

phons = Phon("phon.png")

balls = Ball(250, 125, 50, 50, "ball.png", 1, 1)

leftlable = pygame.font.Font(None, 50).render("Виграй другий гравець", True, (255, 255, 255))
rightlable = pygame.font.Font(None, 50).render("Виграй перший гравець", True, (255, 255, 255))

#програмування дії
game = menu(screen)
meny = Meny("menys.png")
while game:

    #обробка події
    
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                platforms2.speed = -5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                platforms2.speed = 5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                platforms1.speed = -5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                platforms1.speed = 5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                game = menu(screen)
                
    platforms2.rect.y +=  platforms2.speed
    if platforms2.rect.y > 270:
        platforms2.speed = -5
    if platforms2.rect.y < 0:
        platforms2.speed = 5

    #оновлення об'єктів
    

    #натискання клавіш першого гравця


    platforms1.rect.y +=  platforms1.speed
    
    if platforms1.rect.y > 270:
        platforms1.speed = -5
    if platforms1.rect.y < 0:
        platforms1.speed = 5
    
    #натискання клавіш другого гравця

    
    
    
    screen.fill((255, 1, 255))
    phons.draw(screen)
    balls.rect.x +=  balls.speedX
    balls.rect.y +=  balls.speedY
    #подія з м'ячем
    if balls.rect.y > 300:
        balls.speedY = -2
    if balls.rect.y < 0:
        balls.speedY = 2

    if balls.rect.x > 450:
        balls.speedX = -5
    if balls.rect.x < 0:
        balls.speedX = 5


    if balls.rect.colliderect(platforms1.rect):
        balls.speedX *= -1

    if balls.rect.colliderect(platforms2.rect):
        balls.speedX *= -1

    if balls.rect.x < 0:    
        meny.draw(screen)
        screen.blit(leftlable, [115, 160])
        pygame.display.flip()

        break

    if balls.rect.x > 450:    
        meny.draw(screen)
        screen.blit(rightlable, [115, 160])
        pygame.display.flip()

        break
    #відмалювати об'єкти    
    
    platforms1.draw(screen)
    platforms2.draw(screen)
    balls.draw(screen)
    

    pygame.display.flip()

    fps.tick(60)
