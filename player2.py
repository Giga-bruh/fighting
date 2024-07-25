import pygame

import bazoklass
from nenastroiki4 import *
import atacka


class Player2(bazoklass.Baza):
    def __init__(self, igra, x, y,kartinka,ima):
        super().__init__(igra,x,y,kartinka)
        self.kakaya_storona=-1
        self.ima=ima


    def otrisovka(self):

        super().otrisovka()
        if self.indikator > 0:
            pygame.draw.rect(self.igra.screen, [100, 200, 200],
                             [self.pramoygolnik.x + 95, self.pramoygolnik.y - 5, 300, 40], 5)
        pygame.draw.rect(self.igra.screen, [1, 1, 1],
                         [self.pramoygolnik.x + 100, self.pramoygolnik.y, self.indikator, 30])



    def dvishenie(self):
        super().dvishenie()
        for atacki in self.igra.igrok.spisokatack:
            if atacki.pramoygolnik.colliderect(self.pramoygolnik_proverka) == True and self.prised != 1:
                self.igra.igrok.spisokatack.remove(atacki)
                self.hp = self.hp - atacki.yron
        if self.atacka_ili_net == 0:
            self.kakoi_spisok = self.spisokstoitvprava if self.kakaya_storona == 1 else self.spisokstoitvlevo
        klavishi = pygame.key.get_pressed()
        if klavishi[pygame.K_LEFT] == True and self.pramoygolnik.x > - 100 and self.indikator == 0 and self.prised == 0:
            self.pramoygolnik.x = self.pramoygolnik.x - self.skorost
            self.kakoi_spisok = self.spisok_idetv_levo
            self.kakaya_storona = -1
        elif klavishi[
            pygame.K_RIGHT] == True and self.pramoygolnik.right < SCREEN_WIDTH + 150 and self.indikator == 0 and self.prised == 0:
            self.pramoygolnik.x = self.pramoygolnik.x + self.skorost
            self.kakoi_spisok = self.spisokidetvpravo
            self.kakaya_storona = 1
        elif klavishi[pygame.K_e] == True:
            self.kakoi_spisok = self.spisok_saryada_vprava if self.kakaya_storona == 1 else self.spisok_saryada_vlevo
            if self.indikator<=290:
                self.indikator = self.indikator + 1








        elif klavishi[pygame.K_x] == True and self.indikator == 0:
            self.prised = 1
            self.kakoi_spisok = self.spisokprised if self.kakaya_storona == 1 else self.spisok_prised_vlevo
        if klavishi[pygame.K_x] == False:
            self.prised = 0

        if klavishi[pygame.K_e] == False:
            if self.indikator > 100:
                magicball = atacka.Meteoritigryshka(self.igra, self.pramoygolnik.centerx,
                                                    self.pramoygolnik.centery - 100, self.indikator // 3,
                                                    self.kakaya_storona * 3)
                self.spisokatack.append(magicball)
                self.atacka_ili_net = 1

                self.kakoi_spisok = self.spisok_pozi_atacki if self.kakaya_storona == 1 else self.spisok_pozi_atacki_vlevo
                self.vrema_atacki = pg.time.get_ticks()
            self.indikator = 0

        if self.postoyanoe_vrema - self.vrema_atacki >= 1000:
            self.atacka_ili_net = 0


        if self.hp <= 0:
            self.igra.pobeditel = f"победил {self.ima}"
