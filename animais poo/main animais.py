from donos import Dono
from tipo_animais import TiposAnimais

gato = TiposAnimais.Gato("Soluço", 3)
cachorro = TiposAnimais.Cao("Badu", 5)
passaro = TiposAnimais.Passaro("Amora", 2)

dono1 = Dono("João")
dono2 = Dono("Maria")
Dono3 = Dono("José")


dono1.chamar_animal(gato)
gato.fazer_som()
gato.alimentar()
gato.arranhar()

print()

dono2.chamar_animal(cachorro)
cachorro.fazer_som()
cachorro.alimentar()
cachorro.caçar()

print()

Dono3.chamar_animal(passaro)
passaro.fazer_som()
passaro.alimentar()
passaro.voar()