def è_amico_di_harry(nome):
    amici = ["Ron", "Hermione", "Hagrid", "Silente"]
    if nome in amici:
        return True
    else:
        return False

lista_da_controllare = ["Voldemort", "Malfoy", "Hagrid"]

for elemento in lista_da_controllare:
    print(è_amico_di_harry(elemento))
