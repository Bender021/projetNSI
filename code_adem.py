import pyxel
class jeu():    
    
        def __init__(self):

            # taille de la fenetre 128x128 pixels
            # ne pas modifier
        
            pyxel.init(128, 128)
        
            # position initiale du vaisseau
            # (origine des positions : coin haut gauche)
            self.vaisseau_x = 60
            self.vaisseau_y = 60
            self.vie = 3
            # initialisation des tirs
            self.tirs_liste = []

            pyxel.run(self.update, self.draw)


        def vaisseau_deplacement(self):
            """déplacement avec les touches de directions"""

            if pyxel.btn(pyxel.KEY_RIGHT) and self.vaisseau_x<128:
                self.vaisseau_x += 1
            if pyxel.btn(pyxel.KEY_LEFT) and self.vaisseau_x>0:
                self.vaisseau_x += -1
            if pyxel.btn(pyxel.KEY_DOWN) and self.vaisseau_y<128:
                self.vaisseau_y += 1
            if pyxel.btn(pyxel.KEY_UP) and self.vaisseau_y>0:
                self.vaisseau_y += -1
            if self.vaisseau_x+8>=128 or self.vaisseau_x<=0 or self.vaisseau_y+8>=128 or self.vaisseau_y<=0:
                self.vaisseau_x=60
                self.vaisseau_y=60
                self.vie -=1
            
        def tirs_creation(self):
            """création d'un tir avec la barre d'espace"""

            if pyxel.btn(pyxel.KEY_SPACE):
                """self.tirs_liste.append([self.vaisseau_x+4, self.vaisseau_y-4])
                self.tirs_liste.append([self.vaisseau_x-1, self.vaisseau_y+0])
                self.tirs_liste.append([self.vaisseau_x+8, self.vaisseau_y+0])"""
                self.tirs_liste.append([self.vaisseau_x-2, self.vaisseau_y+3])
            
            

        def tirs_deplacement(self):
            """déplacement des tirs vers le haut et suppression s'ils sortent du cadre"""

            for tir in  self.tirs_liste:
                tir[1] -= 2
                if  tir[1]<-8:
                    self.tirs_liste.remove(tir)


        # =====================================================
        # == UPDATE
        # =====================================================
        def update(self):
            """mise à jour des variables (30 fois par seconde)"""

            # deplacement du vaisseau
            self.vaisseau_deplacement()

            # creation des tirs en fonction de la position du vaisseau
            self.tirs_creation()

            # mise a jour des positions des tirs
            self.tirs_deplacement()


        # =====================================================
        # == DRAW
        # =====================================================
        def draw(self):
            """création et positionnement des objets (30 fois par seconde)"""

            # vide la fenetre
            pyxel.cls(0)

            # vaisseau (carre 8x8)
            pyxel.rect(self.vaisseau_x, self.vaisseau_y, 8, 8, 1)
            if self.vie ==0:
                pyxel.text(8 ,7 ,"GAME OVER" ,5)
                
            # tirs
            for tir in self.tirs_liste:
                pyxel.rect(tir[0], tir[1], 1, 4, 10)        

jeu()
