import pygame
import time


pygame.init()


class player:
    dx = 0
    dy = 0

    def __init__(self, x, y, w, h, speed, shape) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
        self.shape = shape

    def move(self):
        if (
            self.x + self.dx * self.speed >= 0
            and self.x + self.dx * self.speed + self.w <= 800
        ):
            self.x += self.dx * self.speed

        if (
            self.y + self.dy * self.speed >= 0
            and self.y + self.dy * self.speed + self.h <= 800
        ):
            self.y += self.dy * self.speed

    def draw(self, window):
        if self.shape == "rect":
            pygame.draw.rect(
                window,
                pygame.Color("Blue"),
                pygame.Rect(self.x, self.y, self.w, self.h),
            )
        if self.shape == "circle":
            pygame.draw.circle(window, pygame.Color("Blue"), (self.x, self.y), self.w)


def checkCollison(igrac1, igrac2):
    gl = pygame.Vector2(igrac1.x, igrac1.y)
    gd = pygame.Vector2(igrac1.x + igrac1.w, igrac1.y)
    dl = pygame.Vector2(igrac1.x, igrac1.y + igrac1.h)
    dd = pygame.Vector2(igrac1.x + igrac1.w, igrac1.y + igrac1.h)

    mojaLista = [gl, gd, dl, dd]

    for tacka in mojaLista:
        if (
            tacka.x > igrac2.x
            and tacka.x < igrac2.x + igrac2.w
            and tacka.y > igrac2.y
            and tacka.y < igrac2.y + igrac2.h
        ):
            return True
    return False


window = pygame.display.set_mode((800, 800))
igrac = player(5, 5, 100, 100, 15, "rect")

igrac2 = player(200, 100, 100, 100, 20, "rect")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 200)
while True == True:
    # Resetovanje dx i dy da ne idu beskonacno
    igrac.dx = 0
    igrac.dy = 0
    igrac2.dx = 0
    igrac2.dy = 0

    # Resetujem ekran, jer se inace nikad nista nebi izbrisalo
    window.fill("Red")
    # Crtamo igrace
    igrac.draw(window)
    igrac2.draw(window)
    # Kretanje za igraca 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        igrac.dy = -1
    if keys[pygame.K_d]:
        igrac.dx = 1
    if keys[pygame.K_s]:
        igrac.dy = 1
    if keys[pygame.K_a]:
        igrac.dx = -1

    # Kretanje za Igraca 2
    if keys[pygame.K_LEFT]:
        igrac2.dx = -1
    if keys[pygame.K_RIGHT]:
        igrac2.dx = 1
    if keys[pygame.K_UP]:
        igrac2.dy = -1
    if keys[pygame.K_DOWN]:
        igrac2.dy = 1

    events = pygame.event.get()
    # Exit kada pritisnies x
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    # Updateovi
    igrac.move()
    igrac2.move()

    if checkCollison(igrac, igrac2) == True:
        text = font.render("Game over", True, pygame.Color("Black"))

        # Center the text on the screen
        text_rect = text.get_rect()
        text_rect.centerx = window.get_rect().centerx
        text_rect.centery = window.get_rect().centery
        window.blit(text, text_rect)
        pygame.display.flip()
        time.sleep(10)

    pygame.display.flip()
    clock.tick(60)
