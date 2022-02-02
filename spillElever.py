import tkinter as tk

#
#
# Her kommer koden som kobler oss til databasen
#
#

def lt_elev():
    elevNR = elevNummer.get()
    elevNA = elevNavn.get()
    elevSP = favorittSpill.get()
    #
    #
    # Her kommer koden din der du legger til en elev i databasen
    #
    #

def lt_spill():
    spillNR = spillNummer.get()
    spillNA = spillNavn.get()
    spillKA = spillKategori.get()
    #
    #
    # Her kommer koden din der du legger til ett spill i databasen
    #
    #

root = tk.Tk()
root.title("Program-SomLegger_tilELEVEReLLERspill! LeserNoenDETTEher egentlig??")

elevNummer = tk.Entry(root)
elevNummer.grid(row = 1, column = 1)
elevNavn = tk.Entry(root)
elevNavn.grid(row = 1, column = 2)
favorittSpill = tk.Entry(root)
favorittSpill.grid(row = 1, column = 3)

spillNummer = tk.Entry(root)
spillNummer.grid(row = 1, column = 6)
spillNavn = tk.Entry(root)
spillNavn.grid(row = 1, column = 7)
spillKategori = tk.Entry(root)
spillKategori.grid(row = 1, column = 8)


tk.Label(text = "ElevNummer").grid(row = 0, column = 1)
tk.Label(text = "Navn").grid(row = 0, column = 2)
tk.Label(text = "FavorittspillNummer").grid(row = 0, column = 3)
tk.Label(text = "SpillNummer").grid(row = 0, column = 6)
tk.Label(text = "Navn").grid(row = 0, column = 7)
tk.Label(text = "Kategori").grid(row = 0, column = 8)
tk.Label(text = "", width = 5).grid(row = 0, column = 4)

legg_til_elev = tk.Button(root, text = "Legg til elev", command = lt_elev)
legg_til_elev.grid(row = 1, column = 0)
legg_til_spill = tk.Button(root, text = "Legg til spill", command = lt_spill)
legg_til_spill.grid(row = 1, column = 5)
root.mainloop()
