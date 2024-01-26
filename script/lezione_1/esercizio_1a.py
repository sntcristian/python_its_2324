def è_amico_di_harry(nome):
    amici = ["Ron", "Hermione", "Hagrid", "Silente"]
    if nome in amici:
        return True
    else:
        return False

è_amico_malfoy = è_amico_di_harry("Malfoy")
print(è_amico_malfoy)