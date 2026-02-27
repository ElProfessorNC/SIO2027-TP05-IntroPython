def trier_nb():
    nb = []
    for i in range(5):
        n = int(input("Entrez un nombre : "))
        nb.append(n)
    nb.sort()
    print("Les nombres triés sont : ", nb)

trier_nb()
