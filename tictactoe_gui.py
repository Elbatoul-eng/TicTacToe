import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.joueur = "X"
        self.plateau = [["" for _ in range(3)] for _ in range(3)]

        self.fenetre = tk.Tk()
        self.fenetre.title("Tic-Tac-Toe")

        self.boutons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                bouton = tk.Button(self.fenetre, text="", font=("Arial", 32), width=5, height=2,
                                   command=lambda i=i, j=j: self.jouer(i, j))
                bouton.grid(row=i, column=j)
                self.boutons[i][j] = bouton

        self.label = tk.Label(self.fenetre, text=f"Tour du joueur {self.joueur}", font=("Arial", 16))
        self.label.grid(row=3, column=0, columnspan=3)

        self.fenetre.mainloop()

    def jouer(self, i, j):
        if self.plateau[i][j] == "":
            self.plateau[i][j] = self.joueur
            self.boutons[i][j].config(text=self.joueur)

            if self.victoire(self.joueur):
                messagebox.showinfo("Victoire", f"Le joueur {self.joueur} a gagné !")
                self.fenetre.quit()
            elif self.match_nul():
                messagebox.showinfo("Match nul", "Personne n'a gagné.")
                self.fenetre.quit()
            else:
                self.joueur = "O" if self.joueur == "X" else "X"
                self.label.config(text=f"Tour du joueur {self.joueur}")

    def victoire(self, joueur):
        for i in range(3):
            if all(self.plateau[i][j] == joueur for j in range(3)) or \
               all(self.plateau[j][i] == joueur for j in range(3)):
                return True
        if all(self.plateau[i][i] == joueur for i in range(3)) or \
           all(self.plateau[i][2 - i] == joueur for i in range(3)):
            return True
        return False

    def match_nul(self):
        return all(self.plateau[i][j] != "" for i in range(3) for j in range(3))

if __name__ == "__main__":
    TicTacToe()
