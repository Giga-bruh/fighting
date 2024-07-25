import random

import pygame

import bazoklass
from nenastroiki4 import *
import atacka
import player

class Bot(bazoklass.Baza):
    def __init__(self, igra, x, y,kartinka,ima):
        super().__init__(igra,x,y,kartinka)
        self.ima=ima
        self.time=0
        self.xodim_ili_net=0

        # self.rect = self.image.get_rect()
        # self.rect.center = (100, SCREEN_HEIGHT // 2)

    def dvishenie(self):
        super().dvishenie()

        if self.igra.igrok.pramoygolnik_proverka.centerx>self.pramoygolnik_proverka.centerx and self.xodim_ili_net!=1:
            self.kakaya_storona=1
        elif self.xodim_ili_net!=1:
            self.kakaya_storona=-1
        if self.xodim_ili_net!=1:
            randomwalk=random.randint(1,3000)
            if randomwalk<5 :
                self.xodim_ili_net=1
                self.rasstoyanie=random.randint(20,200)
                if self.igra.igrok.pramoygolnik_proverka.centerx - self.pramoygolnik_proverka.centerx>=100:
                    self.kakaya_storona = 1
                elif self.pramoygolnik_proverka.centerx - self.igra.igrok.pramoygolnik_proverka.centerx>=100 :
                    self.kakaya_storona = -1
        self.prised=0
        if self.atacka_ili_net!=1:
            self.kakoi_spisok = self.spisokstoitvprava if  self.kakaya_storona == 1 else self.spisokstoitvlevo
        self.random = random.randint(0, 2000)
        if self.random<5 and self.xodim_ili_net!=1:

            magicball = atacka.Meteoritigryshka(self.igra, self.pramoygolnik.centerx, self.pramoygolnik.centery - 100,
                                                random.randint(10,50),self.kakaya_storona*3)
            print("")
            self.spisokatack.append(magicball)
            self.time=pg.time.get_ticks()
            self.kakoi_spisok=self.spisok_pozi_atacki if self.kakaya_storona==1 else self.spisok_pozi_atacki_vlevo
            self.atacka_ili_net=1


        for atacki in self.igra.igrok.spisokatack:
           if abs(atacki.pramoygolnik.centerx-self.pramoygolnik_proverka.centerx)<=200:
               if atacki.chislo<6:
                   self.prised = 1
                   self.kakoi_spisok = self.spisokprised if self.kakaya_storona == 1 else self.spisok_prised_vlevo



           if atacki.pramoygolnik.colliderect(self.pramoygolnik_proverka) == True and self.prised!=1 and self.xodim_ili_net!=1:
                self.igra.igrok.spisokatack.remove(atacki)
                self.hp=self.hp-atacki.yron
        if self.xodim_ili_net==1:
            self.kakoi_spisok=self.spisok_idetv_levo if self.kakaya_storona==-1 else self.spisokidetvpravo

            self.pramoygolnik.x+=self.skorost*self.kakaya_storona

            self.rasstoyanie-=self.skorost
            if self.rasstoyanie==0 or self.pramoygolnik_proverka.right>SCREEN_WIDTH or self.pramoygolnik_proverka.left<0 :
                self.xodim_ili_net=0
        self.pramoygolnik_proverka.center=self.pramoygolnik.center
        if self.postoyanoe_vrema-self.time>=1000:
             self.atacka_ili_net=0

    def otrisovka(self):
        super().otrisovka()
        self.igra.screen.blit(self.image, self.pramoygolnik)
        if self.hp<=0:
            self.igra.pobeditel=f"{self.ima} победили"
