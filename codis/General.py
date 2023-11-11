import pandas as pd


categories = ['cod_modelo_color',
              'cod_color_code',
              'des_color_specification_esp',
              'des_agrup_color_eng',
              'des_sex',
              'des_age',
              'des_line',
              'des_fabric',
              'des_product_category',
              'des_product_aggregated_family',
              'des_product_family',
              'des_product_type',
              'des_filename']

class Outfit():
    def __init__(self, cod_outfit):
        self.peces = []
        self.cod_outfit = cod_outfit
    
    def afegir_peca(self, cod_modelo_color):
        self.peces.append(peca[cod_modelo_color])

class Peca():
    def __init__(self, valors_categories):
        self.atributs = {}
        for i in range(len(categories)):
            self.atributs[categories[i]] = valors_categories[i]


csv_producte_path='../datathon/dataset/product_data.csv'
csv_outfit_path='../datathon/dataset/outfit_data.csv'
df_producte = pd.read_csv(csv_producte_path, sep=",")
df_outfit = pd.read_csv(csv_outfit_path, sep=",")


peca = {}
for i in range(df_producte.shape[0]):
    peca[df_producte["cod_modelo_color"][i]] = Peca([df_producte[j][i] for j in categories])

maxim = -1
for i in df_outfit["cod_outfit"]:
    if maxim == -1 or i > maxim: maxim = i
outfits = [Outfit(i+1) for i in range(maxim)]
for i in range(df_outfit.shape[0]):
    outfits[df_outfit['cod_outfit'][i]-1].afegir_peca(df_outfit["cod_modelo_color"][i])

#peca = {codi_de_la_peca : Peca()}
#outfits = [Outfit(), ...]
