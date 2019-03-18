import time
import pygame

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
        pygame.draw.line(screen, (0, 0, 0), [k, 100], [k, 400], 3)


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

    
# инициализация pygame:
pygame.init()
# размеры окна: 
size = width, height = 1500, 600
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)

running = True
clock = pygame.time.Clock()
screen.fill((0, 0, 0))


a_radius = 5
a_pressed = False
w_radius = 5
w_pressed = False
s_radius = 5
s_pressed = False
e_radius = 5
e_pressed = False
d_radius = 5
d_pressed = False
f_radius = 5
f_pressed = False
t_radius = 5
t_pressed = False
g_radius = 5
g_pressed = False
y_radius = 5
y_pressed = False
h_radius = 5
h_pressed = False
u_radius = 5
u_pressed = False
j_radius = 5
j_pressed = False
radiuses = [a_radius, w_radius, s_radius, e_radius, d_radius, f_radius, t_radius ,\
            g_radius, y_radius, h_radius, u_radius, j_radius]
while running:
    draw_keyboard((100, 100))
    if a_pressed:
        if a_radius < 45:
            a_radius += 1
        else:
            a_radius = 5
        pygame.draw.circle(screen, (255, 255, 0), (150, 350), a_radius, 0)
        time.sleep(0.05)
    else:
        a_radius = 0
        pygame.draw.circle(screen, (255, 255, 0), (150, 350), a_radius, 0)
    if w_pressed:
        if w_radius < 45:
            w_radius += 1
        else:
            w_radius = 5
        pygame.draw.circle(screen, (255, 255, 0), (200, 270), w_radius, 0)
        time.sleep(0.05)
    else:
        w_radius = 0
        pygame.draw.circle(screen, (255, 255, 0), (200, 270), w_radius, 0)
    if s_pressed:
        if s_radius < 45:
            s_radius += 1
        else:
            s_radius = 5
        pygame.draw.circle(screen, (255, 255, 0), (250, 350), s_radius, 0)
        time.sleep(0.05)
    else:
        s_radius = 0
        pygame.draw.circle(screen, (255, 255, 0), (250, 350), s_radius, 0)
    if e_pressed:
        if e_radius < 45:
            e_radius += 1
        else:
            e_radius = 5
        pygame.draw.circle(screen, (255, 255, 0), (300, 270), e_radius, 0)
        time.sleep(0.05)
    else:
        e_radius = 0
        pygame.draw.circle(screen, (255, 255, 0), (300, 270), e_radius, 0)
    if d_pressed:
        if d_radius < 45:
            d_radius += 1
        else:
            d_radius = 5
        pygame.draw.circle(screen, (255, 255, 0), (350, 350), d_radius, 0)
        time.sleep(0.05)
    else:
        d_radius = 0
        pygame.draw.circle(screen, (255, 255, 0), (350, 350), d_radius, 0)
    if f_pressed:
        if f_radius < 45:
            f_radius += 1
        else:
            f_radius = 5
        pygame.draw.circle(screen, (255, 255, 0), (450, 350), f_radius, 0)
        time.sleep(0.05)
    else:
        f_radius = 0
        pygame.draw.circle(screen, (255, 255, 0), (450, 350), f_radius, 0)
    if t_pressed:
        if t_radius < 45:
            t_radius += 1
        else:
            t_radius = 5
        pygame.draw.circle(screen, (255, 255, 0), (500, 270), t_radius, 0)
        time.sleep(0.05)
    else:
        t_radius = 0
        pygame.draw.circle(screen, (255, 255, 0), (500, 270), t_radius, 0)
    if g_pressed:
        if g_radius < 45:
            g_radius += 1
        else:
            g_radius = 5
        pygame.draw.circle(screen, (255, 255, 0), (550, 350), g_radius, 0)
        time.sleep(0.05)
    else:
        g_radius = 0
        pygame.draw.circle(screen, (255, 255, 0), (550, 350), g_radius, 0)
    if y_pressed:
        if y_radius < 45:
            y_radius += 1
        else:
            y_radius = 5
        pygame.draw.circle(screen, (255, 255, 0), (600, 270), y_radius, 0)
        time.sleep(0.05)
    else:
        y_radius = 0
        pygame.draw.circle(screen, (255, 255, 0), (600, 270), y_radius, 0)
    if u_pressed:
        if u_radius < 45:
            u_radius += 1
        else:
            u_radius = 5
        pygame.draw.circle(screen, (255, 255, 0), (700, 270), u_radius, 0)
        time.sleep(0.05)
    else:
        u_radius = 0
        pygame.draw.circle(screen, (255, 255, 0), (700, 270), u_radius, 0)
    if h_pressed:
        if h_radius < 45:
            h_radius += 1
        else:
            h_radius = 5
        pygame.draw.circle(screen, (255, 255, 0), (650, 350), h_radius, 0)
        time.sleep(0.05)
    else:
        h_radius = 0
        pygame.draw.circle(screen, (255, 255, 0), (650, 350), h_radius, 0)
    if j_pressed:
        if j_radius < 45:
            j_radius += 1
        else:
            j_radius = 5
        pygame.draw.circle(screen, (255, 255, 0), (750, 350), j_radius, 0)
        time.sleep(0.05)
    else:
        j_radius = 0
        pygame.draw.circle(screen, (255, 255, 0), (750, 350), j_radius, 0)
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
                a_pressed = True
                a_radius = 5
            if event.key == pygame.K_w:
                pygame.mixer.music.load('c_sharp.mp3')
                pygame.mixer.music.play(-1)
                w_pressed = True
                w_radius = 5
            if event.key == pygame.K_e:
                pygame.mixer.music.load('d_sharp_2.mp3')
                pygame.mixer.music.play(-1)
                e_pressed = True
                e_radius = 5
            if event.key == pygame.K_s:
                pygame.mixer.music.load('d.wav')
                pygame.mixer.music.play(-1)
                s_pressed = True
                s_radius = 5
            if event.key == pygame.K_d:
                pygame.mixer.music.load('e.wav')
                pygame.mixer.music.play(-1)
                d_pressed = True
                d_radius = 5
            if event.key == pygame.K_f:
                pygame.mixer.music.load('f.wav')
                pygame.mixer.music.play(-1)
                f_pressed = True
                f_radius = 5
            if event.key == pygame.K_t:
                pygame.mixer.music.load('f_sharp_.mp3')
                pygame.mixer.music.play(-1)
                t_pressed = True
                t_radius = 5
            if event.key == pygame.K_g:
                pygame.mixer.music.load('g.wav')
                pygame.mixer.music.play(-1)
                g_pressed = True
                g_radius = 5
            if event.key == pygame.K_y:
                pygame.mixer.music.load('g_sharp_.wav')
                pygame.mixer.music.play(-1)
                y_pressed = True
                y_radius = 5
            if event.key == pygame.K_u:
                pygame.mixer.music.load('a_sharp_.mp3')
                pygame.mixer.music.play(-1)
                u_pressed = True
                u_radius = 5
            if event.key == pygame.K_h:
                pygame.mixer.music.load('a.wav')
                pygame.mixer.music.play(-1)
                h_pressed = True
                h_radius = 5
            if event.key == pygame.K_j:
                pygame.mixer.music.load('h.wav')
                pygame.mixer.music.play(-1)
                j_pressed = True
                j_radius = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                pygame.mixer.music.pause()
                a_pressed = False
            if event.key == pygame.K_w:
                pygame.mixer.music.pause()
                w_pressed = False
            if event.key == pygame.K_s:
                pygame.mixer.music.pause()
                s_pressed = False
            if event.key == pygame.K_e:
                pygame.mixer.music.pause()
                e_pressed = False
            if event.key == pygame.K_d:
                pygame.mixer.music.pause()
                d_pressed = False
            if event.key == pygame.K_f:
                pygame.mixer.music.pause()
                f_pressed = False
            if event.key == pygame.K_t:
                pygame.mixer.music.pause()
                t_pressed = False
            if event.key == pygame.K_g:
                pygame.mixer.music.pause()
                g_pressed = False
            if event.key == pygame.K_y:
                pygame.mixer.music.pause()
                y_pressed = False
            if event.key == pygame.K_u:
                pygame.mixer.music.pause()
                u_pressed = False
            if event.key == pygame.K_h:
                pygame.mixer.music.pause()
                h_pressed = False
            if event.key == pygame.K_j:
                pygame.mixer.music.pause()
                j_pressed = False
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
    pygame.display.flip()
# ...
pygame.quit()
