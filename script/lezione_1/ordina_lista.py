def ordina_lista(lista):
    for indice1 in range(1, len(lista)):

        # itero sugli elementi della lista ignorando il primo
        elemento1 = lista[indice1]

        # itero sugli elementi della lista che precedono elemento 1
        for indice2 in range(indice1):

            # comparo elemento1 con i precedenti per cercare un elemento più piccolo
            elemento2 = lista[indice2]
            if elemento1 < elemento2:

                # rimuove dalla lista l'elemento in posizione: indice 1
                lista.pop(indice1)

                # inserisce nella lista elemento1 in posizione: indice 2
                lista.insert(indice2, elemento1)

                #interrompe il secondo ciclo non appena è trovato un elemento più piccolo
                break

lista_libri = [
    "Il Signore degli Anelli" ,
    "Coraline",
    "Ready Player One",
    "Dune",
    "Neuromante",
    "1984",
    "Il nome del vento",
    "Fondazione",
    "Guerra e pace",
    "Il cacciatore di androidi"
]

ordina_lista(lista_libri)
print(lista_libri)





