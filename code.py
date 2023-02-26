import pyxel, random, time
if __name__ == "__main__":

 pyxel.init(128, 128, title="Nuit du c0de")
 t1 = time.time()

 vaisseau_x = 60
 vaisseau_y = 60
 boss_vies = 10
 vies = 4

 tirs_liste = []
 ennemis_liste = []
 explosions_liste = []
 boss_liste =[]


 def vaisseau_deplacement(x, y):


  if pyxel.btn(pyxel.KEY_RIGHT):
   if (x < 120):
    x = x + 1
  if pyxel.btn(pyxel.KEY_LEFT):
   if (x > 0):
    x = x - 1
  if pyxel.btn(pyxel.KEY_DOWN):
   if (y < 120):
    y = y + 1
  if pyxel.btn(pyxel.KEY_UP):
   if (y > 0):
    y = y - 1
  return x, y


 def tirs_creation(x, y, tirs_liste):

  if pyxel.btnr(pyxel.KEY_SPACE):
   tirs_liste.append([x + 4, y - 4])
  return tirs_liste


 def tirs_deplacement(tirs_liste):


  for tir in tirs_liste:
   tir[1] -= 1
   if tir[1] < -8:
    tirs_liste.remove(tir)
  return tirs_liste


 def ennemis_creation(ennemis_liste):
  t2 = time.time()

  if (pyxel.frame_count % random.randint(40, 60) == 0) and t2-t1 <= 60:
   ennemis_liste.append([random.randint(0, 120), 0])
  return ennemis_liste

 def ennemis_deplacement(ennemis_liste):
  for ennemi in ennemis_liste:
   ennemi[1] += 1
   if ennemi[1] > 128:
    ennemis_liste.remove(ennemi)
  return ennemis_liste

 def boss_creation(boss_liste):
     pass

 def vaisseau_suppression(vies):

  for ennemi in ennemis_liste:
   if ennemi[0] <= vaisseau_x + 8 and ennemi[1] <= vaisseau_y + 8 and ennemi[0] + 8 >= vaisseau_x and ennemi[
    1] + 8 >= vaisseau_y:
    ennemis_liste.remove(ennemi)
    vies -= 1
    explosions_creation(vaisseau_x, vaisseau_y)
  return vies


 def ennemis_suppression():

  for ennemi in ennemis_liste:
   for tir in tirs_liste:
    if ennemi[0] <= tir[0] + 1 and ennemi[0] + 8 >= tir[0] and ennemi[1] + 8 >= tir[1]:
     ennemis_liste.remove(ennemi)
     tirs_liste.remove(tir)

     explosions_creation(ennemi[0], ennemi[1])


 def explosions_creation(x, y):

  explosions_liste.append([x, y, 0])


 def explosions_animation():

  for explosion in explosions_liste:
   explosion[2] += 1
   if explosion[2] == 12:
    explosions_liste.remove(explosion)


 def update():

  global vaisseau_x, vaisseau_y, tirs_liste, ennemis_liste, vies, explosions_liste

  vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)

  tirs_liste = tirs_creation(vaisseau_x, vaisseau_y, tirs_liste)

  tirs_liste = tirs_deplacement(tirs_liste)

  ennemis_liste = ennemis_creation(ennemis_liste)

  ennemis_liste = ennemis_deplacement(ennemis_liste)

  ennemis_suppression()

  vies = vaisseau_suppression(vies)

  explosions_animation()

 def draw():

  pyxel.cls(0)

  if vies > 0:

   pyxel.text(5, 5, 'VIES:' + str(vies), 7)

   pyxel.rect(vaisseau_x, vaisseau_y, 8, 8, 1)

   for tir in tirs_liste:
    pyxel.rect(tir[0], tir[1], 1, 4, 11)

   t2 = time.time()
   for ennemi in ennemis_liste:
    if t2-t1 < 20:
     pyxel.rect(ennemi[0], ennemi[1], 8, 8, 6)
    elif t2-t1 >= 20 and t2-t1 <=40:
     pyxel.rect(ennemi[0], ennemi[1], 8, 8, 3)
    elif t2-t1 >= 40 and t2-t1<=60:
     pyxel.rect(ennemi[0], ennemi[1], 8, 8, 4)
    elif t2-t1 >= 60:
        break
    
   if t2-t1 >= 60:
     pyxel.text(80, 5, 'BOSSVIES:' + str(boss_vies), 7)
   if t2-t1 >= 60:
      pyxel.rect(60, 20, 20, 20, 6)

   for explosion in explosions_liste:
    pyxel.circb(explosion[0] + 4, explosion[1] + 4, 2 * (explosion[2] // 4), 8 + explosion[2] % 3)

  else:

   pyxel.text(50, 64, 'GAME OVER', 7)

