import pygame

def main():
    # 初始化导入的pygame模块
    pygame.init()
    # 初始化显示窗口 + 设置尺寸
    screen = pygame.display.set_mode((800, 600))
    # 设置窗口标题
    pygame.display.set_caption('打球吃小球')
    # 设置窗口背景
    screen.fill((242,242,242))


    # drawCicle(screen)
    # loadImg(screen)

    x, y = 0, 0
    # 开启时间循环处理发生的事件
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 动画
        screen.fill((242,242,242))
        drawCicle(screen, x, y)
        pygame.time.delay(50)
        x, y = x + 5, y + 5


def drawCicle(screen, x, y):
    # 屏幕, 颜色, 圆心位置, 半径, 是否填充圆(0->是)
    pygame.draw.circle(screen, (255,0,0), (x,y),30,0)
    # 刷新当前窗口
    pygame.display.flip()

def loadImg(screen):
    img = pygame.image.load('icon.jpg')
    screen.blit(img, (50,50))   # 图片的左上左边为(50,50)
    pygame.display.flip()
    

if __name__ == "__main__":
    main()
