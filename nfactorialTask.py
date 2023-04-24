import pygame
import math


class Circle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.color = (0, 255, 0)
        self.image = pygame.surface.Surface((20, 20), pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, self.color, self.rect.center, 10)
        self.rect.center = (1000, 1000)

    def draw(self, screen, x, y):
        self.rect.center = (x, y)
        screen.blit(self.image, (x - 10, y - 10))


class anotherCircle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.surface.Surface((10, 10), pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.center = (900, 900)

    def draw(self, screen, x, y, color):
        pygame.draw.circle(self.image, color, self.rect.center, 5)
        self.rect.center = (x, y)
        screen.blit(self.image, (x - 5, y - 5))


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Draw a Perfect Circle')

BLACK = ('black')
WHITE = ('white')
BLUE = ('blue')
RED = ('red')

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.surface.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

background.fill(BLACK)
pygame.draw.circle(background, BLUE, (400, 400), 20, 0)
screen.blit(background, (0, 0))

another_background = pygame.surface.Surface((69, 20))
another_background.fill(BLACK)
another_background_rect = another_background.get_rect().center

background_for_rule = pygame.surface.Surface((115, 34))
background_for_rule.fill(BLACK)
background_for_rule_rect = background_for_rule.get_rect().center

Radik = 0
Radik_temp = Radik
Geshka = 255
Geshka_temp = Geshka
color = (Radik, Geshka, 0)
radik = 0
radik_temp = 0
pref = 0
listochek = [255]
list_of_x_y = []
SCORE = 0
FINALSCORE = 0

CIRCLE = Circle()
sprites_for_circle = pygame.sprite.Group()
sprites_for_circle.add(CIRCLE)

another_circle = anotherCircle()
sprites_for_another_circle = pygame.sprite.Group()
sprites_for_another_circle.add(another_circle)

all_sprites = pygame.sprite.Group()
all_sprites.add([CIRCLE, another_circle])

TOO_CLOSE_TO_DOT = False
circle_is_close = False
SPACE = True

FONT = pygame.font.Font(None, 50)
font = pygame.font.Font(None, 30)

procent = font.render("{}%".format(100.0), True, "Green", "Black")
procent_rect = procent.get_rect().center
screen.blit(procent, (400 - procent_rect[0], 700 - procent_rect[1]))

tooclose_txt = font.render("Too close!", True, "Red")
tooclose_txt_rect = tooclose_txt.get_rect().center

too_slow_drawing = FONT.render("Too slow!", True, (227, 23, 94))
too_slow_drawing_rect = too_slow_drawing.get_rect().center

circle_is_not_close = FONT.render("Draw a full circle!", True, (227, 23, 94))
circle_is_not_close_rect = circle_is_not_close.get_rect().center

PRESS_SPACE = FONT.render("Press SPACE to try again", True, (27, 46, 133))
PRESS_SPACE_rect = PRESS_SPACE.get_rect().center

running = True
MOUSE_DOWN = False

TOO_SLOW_DRAWING = pygame.USEREVENT + 1

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            for sprite in all_sprites:
                sprite.kill()
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                for sprite in all_sprites:
                    sprite.kill()
                running = False
                pygame.quit()
            if event.key == pygame.K_SPACE:
                Radik = 0
                Geshka = 255
                Radik_temp = Radik
                Geshka_temp = Geshka
                color = (Radik, Geshka, 0)
                radik = 0
                radik_temp = 0
                pref = 0
                SCORE = 0
                too_close_to_dot = False
                circle_is_close = False
                MOUSE_DOWN = False
                SPACE = True
                FINALSCORE_TXT = FONT.render("{0:.1f}%".format(FINALSCORE), True,
                                            (int(255 * (1 - (FINALSCORE / 100))), int(255 * (FINALSCORE / 100)), 0),
                                            BLACK)
                background.blit(background_for_rule, (0, 0))
                background.blit(FINALSCORE_TXT, (0, 0))
                screen.blit(background, (0, 0))
                listochek = [255]
                list_of_x_y = []

        if event.type == pygame.MOUSEBUTTONDOWN and SPACE:
            x = event.pos[0]
            y = event.pos[1]
            radik = math.sqrt((abs(400 - x)) ** 2 + (abs(400 - y)) ** 2)
            if radik <= 50:
                TOO_CLOSE_TO_DOT = True
            CIRCLE.draw(screen, x, y)
            MOUSE_DOWN = True
            pygame.time.set_timer(TOO_SLOW_DRAWING, 8000, 1)

        if event.type == pygame.MOUSEBUTTONUP and SPACE:
            x = event.pos[0]
            y = event.pos[1]
            another_circle.draw(screen, x, y, color)
            is_mouse_down = False
            if pygame.sprite.spritecollideany(CIRCLE, sprites_for_another_circle) and len(list_of_x_y) > 75:
                circle_is_close = True
                SCORE = (sum(listochek) / len(listochek)) / 255 * 100
                if SCORE > FINALSCORE:
                    FINALSCORE = SCORE
                circle_is_close_txt = font.render("Your accuracy is {0:.1f}%".format(SCORE), True, WHITE)
                circle_is_close_txt_rect = circle_is_close_txt.get_rect().center
                screen.fill(BLACK)
                screen.blit(circle_is_close_txt, (400 - circle_is_close_txt_rect[0], 200 - circle_is_close_txt_rect[1]))
                screen.blit(PRESS_SPACE, (400 - PRESS_SPACE_rect[0], 235 - PRESS_SPACE_rect[1]))
                CIRCLE.rect.center = (1000, 1000)
                another_circle.rect.center = (900, 900)
                SPACE = False
            else:
                circle_is_close = False
                screen.fill(BLACK)
                screen.blit(circle_is_not_close, (400 - circle_is_not_close_rect[0], 200 - circle_is_not_close_rect[1]))
                screen.blit(PRESS_SPACE, (400 - PRESS_SPACE_rect[0], 235 - PRESS_SPACE_rect[1]))
                CIRCLE.rect.center = (1000, 1000)
                another_circle.rect.center = (900, 900)
                SPACE = False
            pygame.time.set_timer(TOO_SLOW_DRAWING, 0)

        if event.type == pygame.MOUSEMOTION and SPACE:
            if MOUSE_DOWN == True:
                x = event.pos[0]
                y = event.pos[1]
                if (x, y) not in list_of_x_y:
                    list_of_x_y.append((x, y))
                    radik_temp = math.sqrt((abs(400 - x)) ** 2 + (abs(400 - y)) ** 2)
                    if radik_temp <= 50:
                        TOO_CLOSE_TO_DOT = True
                    pref = (abs(radik_temp - radik)) / (radik / 2)
                    procent = FONT.render("{0:.1f}%".format((sum(listochek) / len(listochek)) / 255 * 100), True, (
                    int(255 * (1 - (sum(listochek) / len(listochek)) / 255)), int(255 * (sum(listochek) / len(listochek)) / 255), 0),
                                                       BLACK)
                    procent_rect = procent.get_rect().center
                    screen.blit(another_background, (400 - background_for_rule_rect[0], 700 - background_for_rule_rect[1]))
                    screen.blit(procent, (400 - procent_rect[0], 700 - procent_rect[1]))
                    pygame.draw.circle(screen, color, (x, y), 5)

        if event.type == TOO_SLOW_DRAWING:
            SPACE = False
            screen.fill(BLACK)
            screen.blit(too_slow_drawing, (400 - too_slow_drawing_rect[0], 200 - too_slow_drawing_rect[1]))
            screen.blit(PRESS_SPACE, (400 - PRESS_SPACE_rect[0], 235 - PRESS_SPACE_rect[1]))

    if radik_temp != radik:
        r_temp_prev = radik_temp
        Radik_temp = int(round(Geshka * (1.2 * pref)))
        Geshka_temp = int(round(Geshka * (1 - (1.2 * pref))))
        if Geshka_temp >= 0 and Geshka_temp <= 255 and Radik_temp >= 0 and Radik_temp <= 255:
            color = (Radik_temp, Geshka_temp, 0)
            listochek.append(Geshka_temp)
        else:
            color = (255, 0, 0)
            listochek.append(0)

    if TOO_CLOSE_TO_DOT:
        screen.fill(BLACK)
        screen.blit(tooclose_txt, (400 - tooclose_txt_rect[0], 200 - tooclose_txt_rect[1]))
        screen.blit(PRESS_SPACE, (400 - PRESS_SPACE_rect[0], 235 - PRESS_SPACE_rect[1]))
        SPACE = False

    pygame.display.update()
    clock.tick(144)
pygame.quit()
quit()
