def è_amico_di_harry(nome):
    amici = ["Ron", "Hermione", "Hagrid", "Silente"]
    if nome in amici:
        return True
    else:
        return False

lista_da_controllare = ["Voldemort", "Malfoy", "Hagrid"]

amico_trovato = False
for elemento in lista_da_controllare:
    if è_amico_di_harry(elemento):
        amico_trovato=True

if amico_trovato == True:
    print("Harry ha un amico!")
else:
    print("Harry non ha amici")

