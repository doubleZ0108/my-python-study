from enum import Enum, unique
from math import sqrt
from random import randint
import pygame

@unique
class Color(Enum):
    '''颜色'''
    @staticmethod
    def random_color():
        '''获取随机颜色'''
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        return (r,g,b)

class Ball(object):
    '''球'''
    
    def __init__(self, x, y , radius, sx, sy, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        '''移动'''
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius < 0 or self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius < 0 or self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def eat(self, other):
        '''吃其他的球'''
        if self.alive and other.alive and self!=other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx**2 + dy**2)
            if distance < self.radius + other.radius and self.radius > other.radius:
                other.alive = False
                self.radius += int(other.radius * 0.146)

    def draw(self, screen):
        '''在窗口绘制球'''
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 0)

def main():
    balls = []

    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('大球吃小球')
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                radius = randint(10,100)
                sx, sy = randint(-10,10), randint(-10, 10)
                color = Color.random_color()
                ball = Ball(x,y,radius,sx,sy,color)
                balls.append(ball)
        screen.fill((255,255,255))
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        pygame.display.flip()

        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            for other in balls:
                ball.eat(other)

if __name__ == "__main__":
    main()