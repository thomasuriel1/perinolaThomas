from Perinola import Perinola
from Apuesta import Apuesta
from Jugador import Jugador 

p = Perinola()
print(p)
p.tirar()
print(p)

a = Apuesta()
a.ponerFichas(5)
print(a)
jugador = Jugador("Tomás", 15) 
print(jugador) 