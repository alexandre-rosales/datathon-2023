import pandas as pd
import numpy as np


categories = ['cod_modelo_color',
              'des_color_specification_esp',
              'des_agrup_color_eng',
              'des_sex',
              'des_age',
              'des_fabric',
              'des_product_family',
              'des_product_type',
              'des_filename']

class Outfit():
    def __init__(self, cod_outfit):
        self.cod_outfit = cod_outfit
        self.cod_peces = []
    
    def afegir_cod_peca(self, cod_peca):
        self.cod_peces.append(cod_peca)

class Peca():
    def __init__(self, valors_categories, n):
        self.atributs = {}
        self.adjacents = {}
        self.pos = None
        self.n = n
        for i in range(len(categories)):
            self.atributs[categories[i]] = valors_categories[i]

    def connectar(self, peca):
        if not peca.n in self.adjacents: self.adjacents[peca.n] = 0
        self.adjacents[peca.n] += 1

    def distancia(self, peca):
        if not peca.n in self.adjacents: return -1
        return 100/self.adjacents[peca.n]

class Valor():
    def __init__(self, valor, n):
        self.textValor = valor
        self.adjacents = {}
        self.pos = None
        self.n = n

    def connectar(self, valor):
        if not valor.n in self.adjacents: self.adjacents[valor.n] = 0
        self.adjacents[valor.n] += 1

    def distancia(self, valor):
        if not valor.n in self.adjacents: return -1
        return 100/self.adjacents[valor.n]

csv_producte_path='../datathon/dataset_filtered/product_data_filtered.csv'
csv_outfit_path='../datathon/dataset_filtered/outfit_data_filtered.csv'
df_producte = pd.read_csv(csv_producte_path, sep=",")
df_outfit = pd.read_csv(csv_outfit_path, sep=",")

PECA = {}
for i in range(df_producte.shape[0]):
    PECA[df_producte["cod_modelo_color"][i]] = [df_producte[j][i] for j in categories]

class Estructura():
    #[a, b] és l'interval d'outfits que volem agafar
    def __init__(self, a, b):
        self.outfits = {}
        self.PECA = {}
        self.peces = []
        self.CATEGORIA = {}

        for i in range(df_outfit.shape[0]):
            cod = df_outfit['cod_outfit'][i]
            if a <= cod <= b:
                if not cod in self.outfits:
                    self.outfits[cod] = Outfit(cod)
                self.outfits[cod].afegir_cod_peca(df_outfit['cod_modelo_color'][i])

    def estructura_peces(self):
        for outfit in self.outfits.values():
            for cod in outfit.cod_peces:
                if not cod in self.PECA:
                    n = len(self.peces)
                    self.PECA[cod] = Peca(PECA[cod], n)

            for cod1 in outfit.cod_peces:
                for cod2 in outfit.cod_peces:
                    if cod1 != cod2: self.PECA[cod1].connectar(self.PECA[cod2])

    def estructura_valors(self, c):
        self.CATEGORIA[c] = {'DICT':{}, 'list':[]}
        for outfit in self.outfits.values():
            for cod in outfit.cod_peces:
                if not cod in self.CATEGORIA[c]['DICT']:
                    n = len(self.CATEGORIA[c]['list'])
                    self.CATEGORIA[c]['DICT'][cod] = Valor(PECA[cod][categories.index(c)], n)

            for cod1 in outfit.cod_peces:
                for cod2 in outfit.cod_peces:
                    if cod1 != cod2:
                        self.CATEGORIA[c]['DICT'][cod1].connectar(self.CATEGORIA[c]['DICT'][cod2])

    def obtenir_list(self, c):
        return self.CATEGORIA[c]['list']

    def obtenir_DICT(self, c):
        return self.CATEGORIA[c]['DICT']

