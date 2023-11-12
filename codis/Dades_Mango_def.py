import pandas as pd
pd.options.display.max_rows = 60 #màxim de files quepoden mostrar les taules

#LLegim les dades
csv_producte_path='../datathon/dataset/product_data.csv'
csv_outfit_path='../datathon/dataset/outfit_data.csv'
df_producte = pd.read_csv(csv_producte_path, sep=",")
df_outfit = pd.read_csv(csv_outfit_path, sep=",")

######### Product_data
# cod_modelo_color - A unique identifier for a particular fashion product based on its model and color.
# cod_color_code - A code indicating the specific color of the product.
# des_color_specification_esp - Description of the color in Spanish.
# des_agrup_color_eng - Grouped color description in English.
# des_sex - Gender for which the product is intended (e.g., "Unisex", "Female", "Male").
# des_age - Age group for which the product is intended (e.g., "Adult", "Child").
# des_line - The line or collection to which the product belongs.
# des_fabric - The fabric or material of the product.
# des_product_category - Broad category of the product (e.g., "Bottoms", "Tops").
# des_product_aggregated_family - An aggregated family description of the product (e.g., "Trousers & leggings").
# des_product_family - Family description of the product (e.g., "Trousers", "Shirts").
# des_product_type - Type of the product within its family (e.g., "Trousers", "Shirt").
# des_filename - File path of the product image associated with the cod_modelo_color.
#                Images can be found in the images folder. Image is always the frontal image of the product without a human model.

######### Outfit_data
# cod_outfit - A unique identifier for a particular outfit.
# cod_modelo_color - A unique identifier for a particular fashion product based on its model and color. This is used to relate the outfit with the actual product details.


# Mostrar les taules
df_producte
df_outfit


# Veiem les diferents categories i el nombre d'etiquetes diferents que tenen cada una
categories1 = ['cod_modelo_color',
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

for i in categories1:
    print()
    print(i, ": ", len(df_producte[i].unique()), " etiquetes diferents")
    print(df_producte[i].unique())


#### Eliminem les columnes innecessàries
columnes_borrar=['cod_color_code', 'des_line', 'des_product_category', 'des_product_aggregated_family']
df_producte_filtered1=df_producte.drop(columnes_borrar, axis=1)
df_producte_filtered1

#### Eliminem els tipus de roba que no formen outfits
families_eliminar= ['Card holder', 'Wallet', 'Umbrella', 'Bodymist', 'Basket', 'Cosmetic bag',
                    'Plaid', 'Duvet Covers', 'Beach Towel', 'Fragance', 'Case', 'Pillow Case',
                    'Cushion Case', 'Tumblers', 'Carpet Yarn', 'Jug', 'Gadget', 'Home Spray',
                    'Curtain', 'Candle', 'Keyring', 'Box', 'Glasses case', 'Bedspread', 'Quilt',
                    'Bed Cushion Case', 'Candle Holder', 'Organiser']

df_producte_filtered2 = df_producte_filtered1.loc[~df_producte_filtered1['des_product_type'].isin(families_eliminar)]
df_producte_filtered2

#### Creem el dataset a partir del dataframe df_producte_filtered2
df_producte_filtered2.to_csv('Product_data_filtered.csv', index=False)
print("\nDataFrame exported to 'output_file.csv'.")

## Outfit_data
# cod_outfit - A unique identifier for a particular outfit.
# cod_modelo_color - A unique identifier for a particular fashion product based on its model and color. This is used to relate the outfit with the actual product details.

df_outfit

#### Afegim una columna amb el tipus de roba de cada identificador
tipus=[]
for i in df_outfit.cod_modelo_color:
    row = df_producte.loc[df_producte['cod_modelo_color'] == i]
    tipus_i = row['des_product_aggregated_family'].values[0]
    tipus.append(tipus_i)


df_outfit['tipus'] = tipus
df_outfit

#### Esborrem els duplicats en cada outfit (excepte Accessories i l'altre)
df_filtered_o = df_outfit[df_outfit['tipus'] != 'Accessories']
df_filtered_1 = df_filtered_o[df_outfit['tipus'] != 'Sweaters and Cardigans']

df1 = df_filtered_1.drop_duplicates(subset=["cod_outfit", "tipus"], keep='first')
df2 = df_outfit[df_outfit['tipus'] == 'Accessories']
df3 = df_outfit[df_outfit['tipus'] == 'Sweaters and Cardigans']

df_concatenated = pd.concat([df1, df2, df3])
df_outfit_filtered_intermig = df_concatenated.sort_values('cod_outfit', ascending=True)
df_outfit_filtered_intermig

#### Eliminem la columna provisional i obtenim les dades filtrades
df_outfit_filtered = df_outfit_filtered_intermig.drop('tipus', axis=1)
df_outfit_filtered

indices_to_drop = []

for i in df_outfit_filtered.cod_modelo_color:
    no_hi_es = True
    for j in df_producte_filtered2.cod_modelo_color:
        if i == j:
            no_hi_es = False
    
    if no_hi_es == True:
        #eliminem la fila
        #df_outfit_filtered = df_outfit_filtered.loc[df_outfit_filtered['cod_modelo_color'] != i]
        index = df_outfit_filtered.loc[df_outfit_filtered['cod_modelo_color'] == i].index[0]
        indices_to_drop.append(index)
        
df_outfit_filtered = df_outfit_filtered.drop(indices_to_drop)

# Resulten les dues següents taules
df_producte_filtered2
df_outfit_filtered

### Exportem els dataframes filtrats en format .csv
#df_producte_filtered2.to_csv('product_data_filtered.csv', index=False)
#print("\nDataFrame exported to 'product_data_filtered.csv'.")
#df_outfit_filtered.to_csv('outfit_data_filtered.csv', index=False)
#print("\nDataFrame exported to 'outfit_data_filtered.csv'.")