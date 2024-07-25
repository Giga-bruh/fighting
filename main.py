import pygame as pg
import player2
import atacka
from nenastroiki4 import *
pg.init()
import player
import protivnik
import pygame.freetype



class Game:
    def __init__(self,rezhim,kakyakartinka_y_igroka,kakayakartinka_y_protivnika,ima_1_igroka,ima_2_igroka,):

        # Создание окна

        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Битва магов")
        self.pobeditel="xz"
        self.rezhim=rezhim

        self.tekst=pygame.freetype.Font("images/comic-sans-ms.ttf", 80)
        self.igrok=player.Player(self,100,100,kakyakartinka_y_igroka,ima_2_igroka)

        self.background = load_image("images/background.png", SCREEN_WIDTH, SCREEN_HEIGHT)
        if rezhim==2:
            self.protivnik=player2.Player2(self, 500, 100, kakayakartinka_y_protivnika,ima_1_igroka)

        else:
            self.protivnik=protivnik.Bot(self, 500, 100, kakayakartinka_y_protivnika, ima_1_igroka)

        self.clock = pg.time.Clock()
        self.run()

    def run(self):
        while True:
            self.event()
            self.update()
            self.draw()
            self.clock.tick(FPS)


    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()


    def update(self):
        if self.pobeditel=="xz":
            self.igrok.update()
            self.protivnik.update()

    def draw(self):
        # Отрисовка интерфейса
        self.screen.blit(self.background, (0, 0))
        self.igrok.otrisovka()
        self.protivnik.otrisovka()

        if self.pobeditel!="xz":
            self.tekst.render_to(self.screen, [ 100, 19], self.pobeditel, [255, 255, 255])
        pg.display.flip()



if __name__ == "__main__":
    Game()