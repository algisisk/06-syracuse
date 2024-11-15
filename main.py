#### Fonctions secondaires


# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = [ i for i in range(len(lsyr)) ]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
    return None
#######################

### Fonction tertiare
# fonction qui crée une liste de la suite de syracuse

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """

    l = [n]
    while n > 1:
        if n%2 == 0:
            n //= 2
        else:
            n = 3*n + 1
        l.append(n)
    return l

### Fonction secondaire
# affiche le temps de vol

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """
    #votre code ici
    return len(l)-1

### Fonction secondaire
# affiche le temps de vol en altitude

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """
    n = 0
    # votre code ici
    for i in range(1,len(l)):
        if l[i] < l[0]:
            return i-1
    return n

### Fonction secondaire
# affiche l'altitude max

def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """
    # votre code ici
    n = 0
    for i in l:
        if i > n:
            n = i
    return n


#### Fonction principale
# fonction qui fait tourner le code
# crée un liste de syracuse, et affiche son tps de vol, tps vol en attitude et altitude max

def main():
    """
    affiche le tps de vol, tps vol en attitude et altitude max de la suite de syracuse
    """
    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))


if __name__ == "__main__":
    main()