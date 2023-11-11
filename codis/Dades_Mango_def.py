import pandas as pd
pd.options.display.max_rows = 60 #màxim de files quepoden mostrar les taules

#LLegim les dades
csv_producte_path='C:\Users\Joan Salazar\Desktop\datathon-2023\datathon\dataset\product_data'
csv_outfit_path='C:\Users\Joan Salazar\Desktop\datathon-2023\datathon\dataset\outfit_data'
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


# Filtrem les dades eliminant aquelles files que 
families_eliminar= ['Trousers', 'Jeans', 'Dresses', 'Shirt', 'Sweater', 'Skirts', 'Jewellery', 
           'Bags', 'Glasses', 'Wallets & cases', 'Shorts', 'Tops', 'Belts and Ties',
           'Jumpsuit', 'Jackets', 'Coats', 'Footwear', 'Hats, scarves and gloves',
           'T-shirt', 'Blazers', 'Gadgets', 'Swimwear', 'Vest', 'Fragances', 'Cardigans',
           'Trenchcoats', 'Puffer coats', 'Outer Vest', 'Leggings and joggers', 
           'Deco Accessories', 'Poloshirts', 'Intimate', 'Sweatshirts', 'Deco Textiles',
           'Bedding', 'Bodysuits', 'Leather jackets', 'Parkas', 'Glassware']

df_producte_filtered = df_producte.loc[~df_producte['des_product_family'].isin(families_eliminar)]
df_producte_filtered