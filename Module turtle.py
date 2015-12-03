import turtle

turtle.hideturtle()

#fen = turtle.Screen()
#fen.setup(width=800, height=600)
#fen.title("Projet de fin de session")
#Image = turtle.Turtle()
#fen.register_shape("Doge.gif")
#Image.shape("Doge.gif")
#écriture = turtle.Turtle()
#écriture1 = turtle.Turtle()
#écriture.write("Bataille Doge", True, align="center", font=("Stencil", 60, "normal"))
#écriture.goto(0, 130)
#écriture1.write("Créé par Karl Racine et Maxime Guillemette", True, align="left", font=("Stencil", 8, "normal"))
#écriture1.goto(-395, -290)

class batailleNavale:
    def __init__(self, hauteur, largeur, image):
    # Définit la fenêtre d'affichage du jeu
        fen = turtle.Screen()
        fen.setup(width=largeur, height=hauteur)
        fen.title("Projet de fin de session")
        Image = turtle.Turtle()
        fen.register_shape(image)
        Image.shape(image)

    def écritures(self, nom, emplacement, taille, x, y):
        écritures = turtle.Turtle()
        écritures.hideturtle()
        écritures.penup()
        écritures.goto(x, y)
        écritures.write(nom, True, align=emplacement, font=("Stencil", taille, "normal"))

fen = batailleNavale(600, 800, "Doge.gif")
fen.écritures("Bataille Doge", "center", 60, 0, 130)
fen.écritures("Créé par Karl Racine et Maxime Guillemette", "left", 9, -395, -290)

class bouton(turtle.Turtle):  # class qui permet de créer des boutons
    def __init__(self, x, y, hauteur, largeur):
        super(bouton, self).__init__()
        self.x = x
        self.y = y
        self.forme(hauteur, largeur)
        self.goto(self.x, self.y)

    def forme(self, hauteur, largeur):  # crée un polygone ayant une certaine largeur et hauteur
        forme = ((0, 0), (-hauteur, 0), (-hauteur, -largeur), (0, -largeur),
                 (0, 0), (-hauteur, 0), (-hauteur, largeur), (0, largeur))
        turtle.addshape("forme",forme)
        self.color('gray')
        self.fillcolor('gray')
        self.shape("forme")
        self.penup()

    def écriture(self, nom, taille):  # Permet de mettre des noms sur les boutons
        écriture = turtle.Turtle()
        écriture.hideturtle()
        écriture.penup()
        écriture.goto(0, self.y + 10)
        écriture.write(nom, True, align="center", font=("stencil", taille, "normal"))

    def déplacement(self):  # déplace le polygone (la tortue) à l'endroit voulu
        self.goto(self.x, self.y)

    def changerFenêtre(self, y, z):
        pass
        # quand on clique sur le bouton,
        # la page devient blanche (nouvelle page)

b1 = bouton(0, 0, 45, 50)
b1.écriture("Jouer", 16)

b2 = bouton(0, -65, 45, 50)
b2.écriture("Option", 16)

b3 = bouton(0, -130, 45, 50)
b3.écriture("Aide", 16)

#def changerFenêtre(x, y):
    #b1.onclick(None, btn=1)
    #fen.clear()
    #b1.onclick(changerFenêtre, btn=1)
#b1.onclick(changerFenêtre, btn=1)

#def changerFenêtre1(x, y):
    #b2.onclick(None, btn=1)
    #fen.clear()
    #b2.onclick(changerFenêtre1, btn=1)
#b2.onclick(changerFenêtre1, btn=1)

turtle.mainloop()

#turtle.getscreen()._root.mainloop()


