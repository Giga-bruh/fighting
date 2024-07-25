import pygame
from nenastroiki4 import *
import atacka


class Baza:
    def __init__(self, igra, x, y,kartinka):
        super().__init__()
        self.kartinka=kartinka
        print(self.kartinka)
        self.igra = igra
        self.x = x
        self.y = y
        self.hp = 50
        self.hp_banner = self.hp
        self.atacka = 0
        self.vrema_atacki = 0
        self.spisokprised = []
        self.spisokstoitvprava = []
        self.spisokstoitvlevo = []
        self.spisokatack = []
        self.spisok_pozi_atacki = []
        self.spisok_pozi_atacki_vlevo = []
        self.spisokidetvpravo = []
        self.spisok_idetv_levo = []
        self.spisok_prised_vlevo = []
        self.atacka_ili_net = 0
        self.atackaa = 0
        self.spisok_saryada_vprava = []
        self.spisok_saryada_vlevo = []
        self.zagryzkaanimacii()
        self.indikator = 0
        self.image = self.spisokstoitvprava[0]

        self.prised = 0
        self.schet = 0
        self.vrema_poslednie_animacii = 0
        self.postoyanoe_vrema = 0
        self.skorost = 1
        self.kakoi_spisok = self.spisokstoitvprava
        shirina = self.image.get_width()
        visota = self.image.get_height()
        self.pramoygolnik = pg.rect.Rect([x, y], [shirina, visota])
        self.pramoygolnik_proverka = pg.rect.Rect([x, y], [shirina / 2.7, visota / 1.4])
        # self.rect = self.image.get_rect()
        # self.rect.center = (100, SCREEN_HEIGHT // 2)

    def zagryzkaanimacii(self):
        for zagryzka in range(1, 4):
            kartinka = load_image(f"images/{self.kartinka}/idle{zagryzka}.png", 400, 500)
            self.spisokstoitvprava.append(kartinka)
            kartinka = pygame.transform.flip(kartinka, 1, 0)
            self.spisokstoitvlevo.append(kartinka)
        kartinka = load_image(f"images/{self.kartinka}/charge.png", 400, 500)
        self.spisok_saryada_vprava.append(kartinka)
        kartinka = pygame.transform.flip(kartinka, 1, 0)
        self.spisok_saryada_vlevo.append(kartinka)
        for zagryzka in range(1, 5):
            kartinka = load_image(f"images/{self.kartinka}/move{zagryzka}.png", 400, 500)
            self.spisokidetvpravo.append(kartinka)
            kartinka = pygame.transform.flip(kartinka, 1, 0)
            self.spisok_idetv_levo.append(kartinka)

        kartinka = load_image(f"images/{self.kartinka}/down.png", 400, 500)
        self.spisokprised.append(kartinka)
        kartinka = pygame.transform.flip(kartinka, 1, 0)
        self.spisok_prised_vlevo.append(kartinka)
        kartinka = load_image(f"images/{self.kartinka}/attack.png", 400, 500)
        self.spisok_pozi_atacki.append(kartinka)
        kartinka = pygame.transform.flip(kartinka, 1, 0)
        self.spisok_pozi_atacki_vlevo.append(kartinka)

    def otrisovka(self):
        self.igra.screen.blit(self.image, self.pramoygolnik)

        pygame.draw.rect(self.igra.screen, [100, 200, 200],
                         [self.pramoygolnik.x + 60, self.pramoygolnik.y + 50, self.hp_banner + 10, 40], 5)
        pygame.draw.rect(self.igra.screen, [1, 1, 1], [self.pramoygolnik.x + 65, self.pramoygolnik.y + 55, self.hp, 30])

        for atacki in self.spisokatack:
            atacki.otrisovka(self.igra.screen)
        self.pramoygolnik_proverka.center = self.pramoygolnik.center

    def dvishenie(self):




        for atacki in self.spisokatack:
            atacki.ypravlenie()


    def animacia(self):

        if self.schet < len(self.kakoi_spisok) and self.postoyanoe_vrema - self.vrema_poslednie_animacii >= 100:
            self.vrema_poslednie_animacii = pg.time.get_ticks()

            self.image = self.kakoi_spisok[self.schet]
            self.schet = self.schet + 1

        elif self.postoyanoe_vrema - self.vrema_poslednie_animacii >= 100 or self.schet >= len(self.kakoi_spisok):
            self.schet = 0
        self.postoyanoe_vrema = pg.time.get_ticks()

    def update(self):
        self.dvishenie()
        self.animacia()
