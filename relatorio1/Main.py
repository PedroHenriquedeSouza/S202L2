from Elefante import Elefante

nome, idade, especie, cor, tamanho = input("Entre com o nome, idade, espécie, cor e tamanho do elefante: ").split()
som = "fuummm!"

elefante = Elefante(nome, idade, especie, cor, som, tamanho)
elefante.emitir_som()