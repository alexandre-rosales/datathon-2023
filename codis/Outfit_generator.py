from General import Estructura, categories
import numpy as np

peca_actual=() #canviar pel que sigui

train = Estructura(0,5000)
train.estructura_peces()


list_dist=[]
for peca in train.peces:
    dist = np.linalg.norm(peca.pos-peca_actual)
    parella=[dist, peca]
    list_dist.append(parella)
list_dist.sort(key=lambda x: x[0], reverse=True)


# Generem l'outfit
outfit_final=[peca_actual]

# PART 1: TROBEM UNA PART DE DALT, UNA PART DE BAIX I UNES SABATES

if peca_actual.atributs['des_product_family'] == 'Trousers' or 'Jeans' or 'Skirts' or 'Shorts' or 'Jumpsuit' or 'Leggins and joggers':
    need_part_baix = False
    need_part_dalt = True
    need_sabates = True
elif peca_actual.atributs['des_product_family'] == 'Dresses' or 'Shirt' or 'Swetter' or 'Tops' or 'T-shirt' or 'Bodysuits':
    need_part_baix = True
    need_part_dalt = False
    need_sabates = True
elif peca_actual.atributs['des_product_family'] == 'Footware':
    need_part_baix = True
    need_part_dalt = True
    need_sabates = False
else:
    need_part_baix = True
    need_part_dalt = True
    need_sabates = True

if need_part_baix:
    i = 1
    parella_i = list_dist[-i]
    peca_i = parella_i[2]
    while (peca_i.atributs['des_product_family'] != 'Trousers' or 'Jeans' or 'Skirts' or 'Shorts' or 'Jumpsuit' or 'Leggins and joggers') and (peca_actual.atributs['des_sex'] == peca_i.atributs['des_sex']) and (peca_actual.atributs['des_age'] == peca_i.atributs['des_age']):
        i+=1
        parella_i = list_dist[-i]
        peca_i = parella_i[2]
    outfit_final.append(peca_i)
    list_dist.pop(-i)

if need_part_dalt:
    i = 1
    parella_i = list_dist[-i]
    peca_i = parella_i[2]
    while (peca_i.atributs['des_product_family'] != 'Dresses' or 'Shirt' or 'Swetter' or 'Tops' or 'T-shirt' or 'Bodysuits') and (peca_actual.atributs['des_sex'] == peca_i.atributs['des_sex']) and (peca_actual.atributs['des_age'] == peca_i.atributs['des_age']):
        i+=1
        parella_i = list_dist[-i]
        peca_i = parella_i[2]
    outfit_final.append(peca_i)
    list_dist.pop(-i)

if need_sabates:
    i = 1
    parella_i = list_dist[-i]
    peca_i = parella_i[2]
    while (peca_i.atributs['des_product_family'] != 'Footware') and (peca_actual.atributs['des_sex'] == peca_i.atributs['des_sex']) and (peca_actual.atributs['des_age'] == peca_i.atributs['des_age']):
        i+=1
        parella_i = list_dist[-i]
        peca_i = parella_i[2]
    outfit_final.append(peca_i)
    list_dist.pop(-i)

# JA TENIM PART DE DALT, PART DE BAIX I SABATES ;) (coincident en gènere i edat)

# PART 2: COMPLETEM AMB ITEMS QUE FALTEN

#suposem que acceptem com a màxim 4 items més
i = 1
while i <= np.randint(1,4):
    parella_i = list_dist[-i]
    peca_i = parella_i[2]
    #if (mateixa edat)(mateix gènere)(no és part de dalt, ni de baix, ni sabates)
    if (peca_actual.atributs['des_sex'] == peca_i.atributs['des_sex']) and (peca_actual.atributs['des_age'] == peca_i.atributs['des_age']) and (peca_i.atributs['des_product_family'] != 'Dresses' or 'Shirt' or 'Swetter' or 'Tops' or 'T-shirt' or 'Bodysuits') and (peca_i.atributs['des_product_family'] != 'Trousers' or 'Jeans' or 'Skirts' or 'Shorts' or 'Jumpsuit' or 'Leggins and joggers') and (peca_i.atributs['des_product_family'] != 'Footware'):
        repetit = False
        for product in outfit_final:
            if peca_i.atributs['des_product_family']==product.atributs['des_product_family']
                repetit = True
        if not repetit:
            outfit_final.append(peca_i)
            i+=1
        else:
            list_dist.pop(-i)
    else:
        list_dist.pop(-i)