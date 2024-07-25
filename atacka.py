import pygame as pg
import random
import nenastroiki4



class Meteoritigryshka:
    def __init__(self,igra,x,y,yron,storona):
        self.chislo=random.randint(0,11)
        self.yron=yron
        self.igra=igra
        self.x=x
        self.y=y
        self.kartinka =pg.image.load("images/earth monk/magicball.png")
        self.kartinka=pg.transform.scale(self.kartinka,[100,100])
        shirina = 100
        visota = 100
        self.skorosty = storona
        self.poyavlnie=[self.x,self.y]
        self.pramoygolnik = pg.rect.Rect([x,y], [shirina, visota])
        self.pramoygolnikstolknovenie1 = pg.rect.Rect([x,y], [shirina/2 , visota/2  ])
    def otrisovka(self, okno):

        okno.blit(self.kartinka, self.pramoygolnik)

    def ypravlenie(self):

            self.pramoygolnik.x = self.pramoygolnik.x + self.skorosty
            self.pramoygolnikstolknovenie1.center=self.pramoygolnik.center


