# Leggi il file
infile = open("titles.txt", "r")
data = infile.read()
infile.close()

# Dividi i titoli a ogni ritorno a capo
titoli_cinematografici = data.split("\n")

# Ordina i titoli con sorted
titoli_ordinati = sorted(titoli_cinematografici)

# Scrivi l'output nel file sorted_titles.txt
outfile = open("sorted_titles.txt", "w")
for titolo in titoli_ordinati:
    outfile.write(titolo+"\n")
outfile.close()