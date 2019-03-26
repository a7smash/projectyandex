import time
import pygame


LEFT_UPPER_CORNER_X = 100
LEFT_UPPER_CORNER_Y = 100


def draw_key(type_, left_upper_corner):
    x = left_upper_corner[0]
    y = left_upper_corner[1]
    if type_ == 'white_r':
        pygame.draw.polygon(screen, (255, 255, 255), [[x, y], [x + 70, y],
                                                [x + 70, y + 200], [x + 100, y + 200],
                                                [x + 100, y + 300], [x, y + 300]], 0)
    elif type_ == 'white_l':
        pygame.draw.polygon(screen, (255, 255, 255), [[x, y], [x + 70, y],
                                        [x + 70, y + 300], [x - 30, y + 300],
                                        [x - 30, y + 200], [x, y + 200]], 0)
    elif type_ == 'white_b':
        pygame.draw.polygon(screen, (255, 255, 255), [[x, y], [x + 40, y],
                                                [x + 40, y + 200], [x + 70, y + 200],
                                                [x + 70, y + 300], [x - 30, y + 300],
                                                [x - 30, y + 200], [x, y + 200]], 0)
    elif type_ == 'black':
        pygame.draw.polygon(screen, (0, 0, 0), [[x, y], [x + 60, y],
                                                [x + 60, y + 200], [x, y + 200]], 0) 


def draw_keyboard(left_upper_corner):
    x = left_upper_corner[0]
    y = left_upper_corner[1]
    left_upper_corners = [(x, y), (x + 70, y), (x + 130, y),
                          (x + 170, y), (x + 230, y), (x + 300, y),
                          (x + 370, y), (x + 430, y), (x + 470, y),
                          (x + 530, y), (x + 570, y), (x + 630, y)]
    types = ['white_r', 'black', 'white_b', 'black', 'white_l', 'white_r', 
             'black', 'white_b', 'black', 'white_b', 'black', 'white_l']
    for type_, luc in zip(types, left_upper_corners):
        draw_key(type_, luc)
    pygame.draw.line(screen, (250, 0, 0), [x, y], [x + 700, y], 3)
    for k in range(x + 100, x + 700, 100):
        pygame.draw.line(screen, (0, 0, 0), [k, 100], [k, 400], 2)


def draw_radiuses(screen, radiuses, press_statuses, centers):
    for radius_, press_status_, center in zip(enumerate(radiuses), enumerate(press_statuses), centers):
        radius = radius_[1]
        press_status = press_status_[1]
        if press_status:
            if radius < 45:
                radius += 1
            else:
                radius = 5
            radiuses[radius_[0]] = radius
            pygame.draw.circle(screen, (255, 255, 0), center, radius, 0)
            time.sleep(0.05)
        else:
            pass
    
# инициализация pygame:
pygame.init()
# размеры окна: 
size = width, height = 1500, 600
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)

running = True
clock = pygame.time.Clock()
screen.fill((0, 0, 0))



press_statuses = [False] * 12
radiuses = [5] * 12
centers = [(LEFT_UPPER_CORNER_X + 50, LEFT_UPPER_CORNER_Y + 250),\
           (LEFT_UPPER_CORNER_X + 100, LEFT_UPPER_CORNER_Y + 170),\
           (LEFT_UPPER_CORNER_X + 150, LEFT_UPPER_CORNER_Y + 250),\
           (LEFT_UPPER_CORNER_X + 200, LEFT_UPPER_CORNER_Y + 170),\
           (LEFT_UPPER_CORNER_X + 250, LEFT_UPPER_CORNER_Y + 250),\
           (LEFT_UPPER_CORNER_X + 350, LEFT_UPPER_CORNER_Y + 250),\
           (LEFT_UPPER_CORNER_X + 400, LEFT_UPPER_CORNER_Y + 170),\
           (LEFT_UPPER_CORNER_X + 450, LEFT_UPPER_CORNER_Y + 250),\
           (LEFT_UPPER_CORNER_X + 500, LEFT_UPPER_CORNER_Y + 170),\
           (LEFT_UPPER_CORNER_X + 550, LEFT_UPPER_CORNER_Y + 250),\
           (LEFT_UPPER_CORNER_X + 600, LEFT_UPPER_CORNER_Y + 170),\
           (LEFT_UPPER_CORNER_X + 650, LEFT_UPPER_CORNER_Y + 250)]

#запустим игру
while running:
    #нарисуем клавиатуру
    draw_keyboard((LEFT_UPPER_CORNER_X, LEFT_UPPER_CORNER_Y))
    #нарисуем на удерживаемых клавишах круги
    draw_radiuses(screen, radiuses, press_statuses, centers)
    
    # внутри игрового цикла ещё один цикл
    # приема и обработки сообщений
    for event in pygame.event.get():
         
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                pygame.mixer.music.load('c.wav')
                pygame.mixer.music.play(-1)
                press_statuses[0] = True
            if event.key == pygame.K_w:
                pygame.mixer.music.load('c_sharp.mp3')
                pygame.mixer.music.play(-1)
                press_statuses[1] = True
            if event.key == pygame.K_s:
                pygame.mixer.music.load('d.wav')
                pygame.mixer.music.play(-1)
                press_statuses[2] = True
            if event.key == pygame.K_e:
                pygame.mixer.music.load('d_sharp_2.mp3')
                pygame.mixer.music.play(-1)
                press_statuses[3] = True
            if event.key == pygame.K_d:
                pygame.mixer.music.load('e.wav')
                pygame.mixer.music.play(-1)
                press_statuses[4] = True
            if event.key == pygame.K_f:
                pygame.mixer.music.load('f.wav')
                pygame.mixer.music.play(-1)
                press_statuses[5] = True
            if event.key == pygame.K_t:
                pygame.mixer.music.load('f_sharp_.mp3')
                pygame.mixer.music.play(-1)
                press_statuses[6] = True
            if event.key == pygame.K_g:
                pygame.mixer.music.load('g.wav')
                pygame.mixer.music.play(-1)
                press_statuses[7] = True
            if event.key == pygame.K_y:
                pygame.mixer.music.load('g_sharp_.wav')
                pygame.mixer.music.play(-1)
                press_statuses[8] = True
            if event.key == pygame.K_h:
                pygame.mixer.music.load('a.wav')
                pygame.mixer.music.play(-1)
                press_statuses[9] = True
            if event.key == pygame.K_u:
                pygame.mixer.music.load('a_sharp_.mp3')
                pygame.mixer.music.play(-1)
                press_statuses[10] = True  
            if event.key == pygame.K_j:
                pygame.mixer.music.load('h.wav')
                pygame.mixer.music.play(-1)
                press_statuses[11] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                pygame.mixer.music.pause()
                press_statuses[0] = False
            if event.key == pygame.K_w:
                pygame.mixer.music.pause()
                press_statuses[1] = False
            if event.key == pygame.K_s:
                pygame.mixer.music.pause()
                press_statuses[2] = False
            if event.key == pygame.K_e:
                pygame.mixer.music.pause()
                press_statuses[3] = False
            if event.key == pygame.K_d:
                pygame.mixer.music.pause()
                press_statuses[4] = False
            if event.key == pygame.K_f:
                pygame.mixer.music.pause()
                press_statuses[5] = False
            if event.key == pygame.K_t:
                pygame.mixer.music.pause()
                press_statuses[6] = False
            if event.key == pygame.K_g:
                pygame.mixer.music.pause()
                press_statuses[7] = False
            if event.key == pygame.K_y:
                pygame.mixer.music.pause()
                press_statuses[8] = False
            if event.key == pygame.K_h:
                pygame.mixer.music.pause()
                press_statuses[9] = False
            if event.key == pygame.K_u:
                pygame.mixer.music.pause()
                press_statuses[10] = False
            if event.key == pygame.K_j:
                pygame.mixer.music.pause()
                press_statuses[11] = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if (x >= 100 and x <= 170 and y >= 100 and y <= 300) or\
            (x >= 100 and x <= 200 and y >= 300 and y <= 400):
                pygame.mixer.music.play(-1)
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            if (x >= 100 and x <= 170 and y >= 100 and y <= 300) or\
            (x >= 100 and x <= 200 and y >= 300 and y <= 400):
                pygame.mixer.music.pause()        
 
    # отрисовка и изменение свойств объектов
    # ...
    clock.tick(60)
    # обновление экрана
#    pygame.display.flip()
# ...
pygame.quit()
