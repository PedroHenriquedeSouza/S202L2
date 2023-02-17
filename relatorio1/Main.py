from Elefante import Elefante

nome, idade, especie, cor, tamanho = input("Entre com o nome, idade, espécie, cor e tamanho do elefante: ").split()
som = "fuummm!"

elefante = Elefante(nome, idade, especie, cor, som, tamanho)

elefante.emitir_som()

if elefante.especie == "Africano" and int(elefante.idade) < 10:
    elefante.mudar_tamanho("pequeno")
    elefante.som = "Paaah"
elif elefante.especie == "Africano" and int(elefante.idade) >= 10:
    elefante.mudar_tamanho("grande")
    elefante.som = "PAHHHHHH"

elefante.emitir_som()
print(elefante.tamanho)