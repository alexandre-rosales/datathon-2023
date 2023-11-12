from General import Estructura
import numpy as np
from scipy.optimize import minimize
from time import time



def distancia(p1, p2):
    return np.linalg.norm(p1 - p2)

def objective_function(positions, *args):
    total_error = 0.0

    for valor1 in valors:
        for valor2 in valors:
            # if adj < 1000:
            if valor1 != valor2:
                print(valor1.n, valor2.n)
                actual_distance = distancia(positions[valor1.n], positions[valor2.n])
                desired_distance = valor1.distancia(valor2)
                error = (actual_distance - desired_distance) ** 2
                total_error += error

    return total_error

def optimize_positions(n, d):
    initial_positions = np.random.rand(n, d)  # Initialize positions randomly
    print(initial_positions.shape)
    result = minimize(objective_function, initial_positions, args=(),
                      method='L-BFGS-B', options={'disp': True})

    optimized_positions = result.x.reshape((n, d))
    return optimized_positions

llista1 = ['des_color_specification_esp',
              'des_agrup_color_eng',
              'des_fabric',
              'des_product_family',
              'des_product_type']
llista2 = ['des_sex', 'des_age']

# Example usage:
train = Estructura(0, 5000)

for categoria in llista1:
    print(categoria)
    train.estructura_valors(categoria)
    valors = train.obtenir_list(categoria)
    d = 2
    t0 = time()

    optimized_positions = optimize_positions(len(valors), d)

    dt = time()-t0
    print("Optimized positions:\n", optimized_positions)
    print(dt)


