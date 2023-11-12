from General import Estructura, categories
import numpy as np

train = Estructura(0,5000)
train.estructura_peces()
test = Estructura(5001,8000)

posicions_outfits = [[train.PECA[cod].pos for cod in outfit.cod_peces] for outfit in test.outfits.values()]

# Cada punt respecte els altres
mitjana_de_mitjanes = 0
for posicions in posicions_outfits:
    for i in posicions:
        suma_dist = 0
        for j in posicions:
            if i != j:
                suma_dist = suma_dist + np.linalg.norm(posicions[i]-posicions[j])
        dist_mitjana = suma_dist/(len(posicions)-1)
    mitjana_de_mitjanes += dist_mitjana

mitjana_de_mitjanes = mitjana_de_mitjanes/len(posicions_outfits)

# Centre geomètric
mitjana_de_mitjanes = 0
for posicions in posicions_outfits:
    #centre = ()
    #for i in posicions:
    #    centre = centre + posicions[i]
    #centre = centre/len(posicions)
    centre = sum(posicions)/len(posicions)

    suma_dist = 0
    for i in posicions:
        suma_dist = suma_dist + np.linalg.norm(posicions[i]-centre)
    dist_mitjana = suma_dist/len(posicions)

    mitjana_de_mitjanes += dist_mitjana

mitjana_de_mitjanes = mitjana_de_mitjanes/len(posicions_outfits)