import turtle

turtle.hideturtle()

fen = turtle.Screen()
fen.setup(width=800, height=500)
fen.title("Projet de fin de session")
Image = turtle.Turtle()
fen.register_shape("bateau.gif")
Image.shape("bateau.gif")

écriture1 = turtle.Turtle()
écriture1.penup()
écriture1.hideturtle()
écriture1.goto(80, -240)
écriture1.write("Créé par Karl Racine et Maxime Guillemette", True, align="left", font=("Stencil", 10, "normal"))

écriture = turtle.Turtle()
écriture.penup()
écriture.hideturtle()
écriture.goto(0, 100)
écriture.write("Bataille navale", True, align="center", font=("Stencil", 60, "normal"))

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

b2 = bouton(0, -65, 45, 50)

b3 = bouton(0, -130, 45, 50)

def changerFenêtre(x, y):
    b1.onclick(changerFenêtre, btn=1)
    fen.clear()
    fen.setup(width=800, height=600)
    écriture = turtle.Turtle()
    écriture.hideturtle()
    écriture.penup()
    écriture.goto(-390, 280)
    écriture.write("Bataille navale", True, align="left", font=("Stencil", 12, "normal"))
b1.onclick(changerFenêtre, btn=1)
b1.écriture("Jouer", 16)

def changerFenêtre1(x, y):
    b2.onclick(changerFenêtre1, btn=1)
    fen.clear()
    image = turtle.Turtle()
    fen.register_shape("Doge.gif")
    fen.setup(width=800, height=600)
    image.shape("Doge.gif")
    écriture = turtle.Turtle()
    écriture.penup()
    écriture.hideturtle()
    écriture.goto(0, 130)
    écriture.write("Option", True, align="center", font=("Stencil", 60, "normal"))
b2.onclick(changerFenêtre1, btn=1)
b2.écriture("Option", 16)

def changerFenêtre2(x, y):
    b3.onclick(changerFenêtre2, btn=1)
    fen.clear()
    fen.setup(width=400, height=300)
    écriture1 = turtle.Turtle()
    écriture1.hideturtle()
    écriture1.penup()
    écriture1.goto(0, 25)
    écriture1. write("Aide", True, align="center", font=("Stencil", 60, "normal"))
    écriture.hideturtle()
    écriture.penup()
    écriture.goto(-180, -10)
    écriture. write("Les règles du jeu sont bien simples,..."
                    , True, align="left", font=("Stencil", 8, "normal"))  # à retravailler
b3.onclick(changerFenêtre2, btn=1)
b3.écriture("Aide", 16)

turtle.mainloop()

#turtle.getscreen()._root.mainloop()


