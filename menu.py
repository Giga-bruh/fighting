import pygame_menu
import pygame as pg
import main
pg.init()


class Menu:
    def __init__(self):
        self.vibor=1
        self.text="igrok"
        self.text_2_igroka="bot"
        self.id_y_skina_y_igroka="earth monk"
        self.id_y_skina_y_protivnika="fire wizard"
        self.okno = pg.display.set_mode((900, 500))
        self.menu_protiv_bota = pygame_menu.Menu(width=900, height=500, theme=pygame_menu.themes.THEME_DARK, title="ФАЙТИНГ")
        self.nadpis = self.menu_protiv_bota.add.label("Битва магов")
        self.rezhimi = self.menu_protiv_bota.add.selector("режим", [("игрок vs бот", 1), ("игрок vs игрок", 2)],
                                                          onchange=self.funkcia_vibor_rezhima)
        self.funkcia_vibor_rezhima_dobavlenie()



        self.menu_protiv_bota.mainloop(self.okno)

    def funkcia_ima(self, text):
        self.text=text

    def funkcia_ima_2_igroka(self, text):
        self.text_2_igroka = text
    def funkcia_slozhonst(self,vibor,id):

        self.id_slozhnost=id


    def funkcia_vibor_rezhima(self,vibor,id):

        self.vibor=id
        self.text="igrok"
        self.text_2_igroka="bot"
        print(self.vibor)
        self.funkcia_vibor_rezhima_ydalenie()
        self.funkcia_vibor_rezhima_dobavlenie()


    def funkcia_vibor_rezhima_dobavlenie(self):



        self.ima = self.menu_protiv_bota.add.text_input("vedite ima: ",  onchange=self.funkcia_ima)

        if self.vibor==1 :
            self.slozhnost = self.knopka = self.menu_protiv_bota.add.selector("сложность",
                                                                             [("легкий", 1), ("средний", 2),
                                                                              ("сложный", 3)],
                                                                             onchange=self.funkcia_slozhonst)
        if self.vibor == 2:
            self.ima_2_igroka = self.menu_protiv_bota.add.text_input("vedite ima 2 igroka: ",
                                                                     onchange=self.funkcia_ima_2_igroka)
        self.igra = self.menu_protiv_bota.add.button("играть", self.funkcia_nazhatie, )
        self.vibran = self.menu_protiv_bota.add.selector("игрок 1",
                                                         [("маг земли", 1), ("маг огня", 2), ("маг молний", 3)],
                                                         onchange=self.vibor_skina_y_protivnika)
        if self.vibor == 2:
            self.skin = self.menu_protiv_bota.add.selector("игрок 2", [("маг земли", 1), ("маг огня", 2), ("маг молний", 3)],
                                                       onchange=self.vibor_skina_y_igroka)
        else:
            self.skin = self.menu_protiv_bota.add.selector("бот",
                                                           [("маг земли", 1), ("маг огня", 2), ("маг молний", 3)],
                                                           onchange=self.vibor_skina_y_igroka)
        self.vixod = self.menu_protiv_bota.add.button("выйти", pygame_menu.events.EXIT)

    def funkcia_vibor_rezhima_ydalenie(self):



        if self.vibor==2:
            self.menu_protiv_bota.remove_widget(self.slozhnost)
        if self.vibor==1:
            self.menu_protiv_bota.remove_widget(self.ima_2_igroka)

        self.menu_protiv_bota.remove_widget(self.ima)
        self.menu_protiv_bota.remove_widget(self.igra)
        self.menu_protiv_bota.remove_widget(self.vibran)
        self.menu_protiv_bota.remove_widget(self.skin)
        self.menu_protiv_bota.remove_widget(self.vixod)




    def vibor_skina_y_protivnika(self,vibor,id):
        if "маг земли" in vibor[0]:
            self.id_y_skina_y_protivnika="earth monk"
        if "маг огня" in vibor[0]:
            self.id_y_skina_y_protivnika = "fire wizard"
        if "маг молний" in vibor[0]:
            self.id_y_skina_y_protivnika = "lightning wizard"


    def vibor_skina_y_igroka(self,vibor,id):
        if "маг земли" in vibor[0]:
            self.id_y_skina_y_igroka="earth monk"
        if "маг огня" in vibor[0]:
            self.id_y_skina_y_igroka ="fire wizard"
        if "маг молний" in vibor[0]:
            self.id_y_skina_y_igroka ="lightning wizard"

    def funkcia_nazhatie(self):


        main.Game(self.vibor,self.id_y_skina_y_igroka,self.id_y_skina_y_protivnika,self.text,self.text_2_igroka)
        print(self.vibor)
        print(self.id_y_skina_y_igroka,self.id_y_skina_y_protivnika)

Menu()
