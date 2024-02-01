# Leggi la prima riga del file
titoli_cinematografici = list()
infile = open("titles.txt", "r")
titolo = infile.readline()

# Itera su tutti i titoli finché non termina il file
while titolo != "":
    # Aggiungi la riga letta alla lista dei titoli
    titoli_cinematografici.append(titolo.rstrip())
    # Leggi una nuova riga
    titolo = infile.readline()
infile.close()

# Ordina i titoli in ordine alfabetico crescente
titoli_ordinati = sorted(titoli_cinematografici)

# Scrivi l'output nel file sorted_titles.txt
outfile = open("sorted_titles.txt", "w")
for titolo in titoli_ordinati:
    outfile.write(titolo+"\n")
outfile.close()