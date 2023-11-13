from General import Estructura
from Entrenament import Vectors
import numpy as np
from random import randint
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


train = Estructura(0,5000)
train.estructura_peces()
vectors = Vectors(train, 2)
print(len(train.peces))
for peca in train.peces:
    peca.pos = vectors.peca_a_vector(peca)

codi_peca = input("Introduïu el codi de la primera peça de l'outfit: ")
#codi_peca = "41085800-02"
#for i in list(train.PECA.keys())[:20]: print(i)
peca_actual=train.PECA[codi_peca]

list_dist=[]
for peca in train.peces:
    dist = np.linalg.norm(peca.pos-peca_actual.pos)
    parella=[dist, peca]
    list_dist.append(parella)
list_dist.sort(key=lambda x: x[0], reverse=True)


# Generem l'outfit
outfit_final=[peca_actual]

# PART 1: TROBEM UNA PART DE DALT, UNA PART DE BAIX I UNES SABATES

if peca_actual.atributs['des_product_family'] in ('Trousers', 'Jeans', 'Skirts', 'Shorts', 'Jumpsuit', 'Leggins and joggers'):
    need_part_baix = False
    need_part_dalt = True
    need_sabates = True
elif peca_actual.atributs['des_product_family'] in ('Dresses', 'Shirt', 'Swetter', 'Tops', 'T-shirt', 'Bodysuits'):
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
    peca_i = parella_i[1]
    while ( (peca_i.atributs['des_product_family'] not in
            ('Trousers', 'Jeans', 'Skirts', 'Shorts', 'Jumpsuit', 'Leggins and joggers'))
            and (peca_actual.atributs['des_sex'] == peca_i.atributs['des_sex'])
            and (peca_actual.atributs['des_age'] == peca_i.atributs['des_age']) ):
                i+=1
                parella_i = list_dist[-i]
                peca_i = parella_i[1]
    outfit_final.append(peca_i)
    list_dist.pop(-i)

if need_part_dalt:
    i = 1
    parella_i = list_dist[-i]
    peca_i = parella_i[1]
    while ( (peca_i.atributs['des_product_family'] not in
           ('Dresses', 'Shirt', 'Swetter', 'Tops', 'T-shirt', 'Bodysuits'))
            and (peca_actual.atributs['des_sex'] == peca_i.atributs['des_sex'])
            and (peca_actual.atributs['des_age'] == peca_i.atributs['des_age']) ):
                i+=1
                parella_i = list_dist[-i]
                peca_i = parella_i[1]
    outfit_final.append(peca_i)
    list_dist.pop(-i)

if need_sabates:
    i = 1
    parella_i = list_dist[-i]
    peca_i = parella_i[1]
    while (peca_i.atributs['des_product_family'] != 'Footware') and (peca_actual.atributs['des_sex'] == peca_i.atributs['des_sex']) and (peca_actual.atributs['des_age'] == peca_i.atributs['des_age']):
        i+=1
        parella_i = list_dist[-i]
        peca_i = parella_i[1]
    outfit_final.append(peca_i)
    list_dist.pop(-i)

# JA TENIM PART DE DALT, PART DE BAIX I SABATES ;) (coincident en gènere i edat)

# PART 2: COMPLETEM AMB ITEMS QUE FALTEN

#suposem que acceptem com a màxim 4 items més
i = 1
rand = randint(1,4)
while i <= rand:
    parella_i = list_dist[-i]
    peca_i = parella_i[1]
    #if (mateixa edat)(mateix gènere)(no és part de dalt, ni de baix, ni sabates)
    if ( (peca_actual.atributs['des_sex'] == peca_i.atributs['des_sex'])
        and (peca_actual.atributs['des_age'] == peca_i.atributs['des_age'])
        and (peca_i.atributs['des_product_family'] not in ('Dresses', 'Shirt', 'Swetter', 'Tops', 'T-shirt', 'Bodysuits'))
        and (peca_i.atributs['des_product_family'] not in ('Trousers', 'Jeans', 'Skirts', 'Shorts', 'Jumpsuit', 'Leggins and joggers'))
        and (peca_i.atributs['des_product_family'] != 'Footware') ):
            repetit = False
            for product in outfit_final:
                if peca_i.atributs['des_product_family']==product.atributs['des_product_family']:
                    repetit = True
            if not repetit:
                outfit_final.append(peca_i)
                i+=1
            else:
                list_dist.pop(-i)
    else:
        list_dist.pop(-i)

"""
print("Codis de l'outfit generat:")
for peca in outfit_final:
    print(peca.atributs['cod_modelo_color'])
"""

imatges = []
for peca in outfit_final:
    image_path = "../"+peca.atributs["des_filename"]
    img = mpimg.imread(image_path)
    imatges.append(img)

fig = plt.figure(figsize=(5,5))
fig.add_subplot(2, 3, 2)
plt.imshow(imatges[0])
plt.axis('off')
for i in range(1, len(imatges)):
    fig.add_subplot(2, len(imatges)-1, len(imatges)-1+i)
    plt.imshow(imatges[i])
    plt.axis('off')
plt.show()
