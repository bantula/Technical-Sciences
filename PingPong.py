import pygame
import math
pygame.init()

win = pygame.display.set_mode((1000, 600))

pygame.display.set_caption("Pong")

WHITE = (255, 255, 255)

deb = 15
duz = 130
brz = 6
x1 = 50
y1 = 300
x2 = 950
y2 = 300
x = 500
y = 300
r = 8
vx = 5
vy = 5
ubrznanje = 1
red = 255
green = 255
blue = 255
red1 = 255
green1 = 255
blue1 = 255

score = 0

# def collision(rleft, rtop, width, height,
#               center_x, center_y, radius):
#
#     rright, rbottom = rleft + width/2, rtop + height/2
#
#     cleft, ctop     = center_x-radius, center_y-radius
#     cright, cbottom = center_x+radius, center_y+radius
#
#     if rright < cleft or rleft > cright or rbottom < ctop or rtop > cbottom:
#         return False
#
#     for x in (rleft, rleft+width):
#         for y in (rtop, rtop+height):
#             if math.hypot(x-center_x, y-center_y) <= radius:
#                 return True
#
#     if rleft <= center_x <= rright and rtop <= center_y <= rbottom:
#         return True
#
#     return False


font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect: object = text_surface.get_rect()
    text_rect.midtop = (x, y)
    win.blit(text_surface, text_rect)

run = True
while run:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()

    if  key[pygame.K_UP] and y2 > 0:
        y2 -= brz
    if key[pygame.K_DOWN] and y2 < 600-duz:
        y2 += brz
    if key[pygame.K_w] and y1 > 0:
        y1 -= brz
    if key[pygame.K_s] and y1 < 600-duz:
        y1 += brz

    if key[pygame.K_y]:
        ubrznanje = 5
        brz = 15
        duz = 160
        green = 0
        blue = 0

    # if collision (x1, y1, deb, duz, x, y, r):
    #     vx -= 2
    #     vy -= 2
    #     vx *= -1
    # if collision(x2, y2, deb, duz, x, y, r):
    #     vx += 2
    #     vy += 2
    #     vx *= -1

    if x <= x1+deb and y >= y1 and y <= y1+duz:
        score += 1
        vx -= ubrznanje
        vy -= ubrznanje
        vx *= -1
    if x >= x2 and y >= y2 and y <= y2+duz:
        score += 1
        vx += ubrznanje
        vy += ubrznanje
        vx *= -1
    if x <= 0:
        x = 500
        y = 300
        r = 8
        vx = 5
        vy = 5
        pygame.time.delay(1000)
    if x >= 1000:
        x = 500
        y = 300
        r = 8
        vx = 5
        vy = 5
        pygame.time.delay(1000)

    if y <= 0:
        vy *= -1
    if y >=600:
        vy *= -1

    x += vx
    y += vy

    draw_text(win, str(score), 18, 500, 10)
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (red, green, blue), (x1, y1, deb, duz))
    pygame.draw.rect(win, (red, green, blue), (x2, y2, deb, duz))
    pygame.draw.circle(win, (red1, green1, blue1), (x, y), r, 0)
    pygame.display.update()
pygame.quit()