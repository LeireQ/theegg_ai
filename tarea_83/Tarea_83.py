class Pokemon():
    def __init__(self,vida,ataque,turno):
        self.vida = vida
        self.ataque = ataque
        self.turno = turno

pikachu = Pokemon(100,55,1)
jigglypuff = Pokemon(100,45,0)
turno = 1

while pikachu.vida > 0 and jigglypuff.vida > 0:
    if turno == jigglypuff.turno:
        pikachu.vida = pikachu.vida - jigglypuff.ataque
        turno = 1
    else:
        jigglypuff.vida = jigglypuff.vida - pikachu.ataque
        turno = 0

if jigglypuff.vida <= 0:
    print("Ha ganado Pikachu!")
else:
    print("Ha ganado Jiglypuff!")