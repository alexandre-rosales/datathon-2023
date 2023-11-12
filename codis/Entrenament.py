from General import Estructura
import numpy as np
from scipy.optimize import minimize
from time import time
import json


def distancia(p1, p2):
    return np.linalg.norm(p1 - p2)

class Vectors():
    #mètode 1: calcular per descens del gradient
    #mètode 2: obtenir el guardat a json
    def __init__(self, t, d, metode=2):
        self.train = t
        for c in categories:
            self.train.estructura_valors(c)
        if metode == 1:
            self.vecsColor = self.vector(categories[0], d)
            self.vecsTela = self.vector(categories[1], d)
            self.vecsFamilia = self.vector(categories[2], d)
        if metode == 2:
            with open('vectors.json') as f:
                self.vecsColor, self.vecsTela, self.vecsFamilia = [np.array(i) for i in json.load(f)]

    def peca_a_vector(self, peca):
        c = categories[0]
        i = self.train.obtenir_DICT(c)[peca.atributs[c]].n
        v1 = self.vecsColor[i]

        c = categories[1]
        i = self.train.obtenir_DICT(c)[peca.atributs[c]].n
        v2 = self.vecsTela[i]
        
        c = categories[2]
        i = self.train.obtenir_DICT(c)[peca.atributs[c]].n
        v3 = self.vecsFamilia[i]

        return np.array([v1[0],v1[1],v2[0],v2[1],v3[0],v3[1]])
    
    def guardar_a_json(self):
        with open('vectors.json', 'w') as f:
            #data = [self.vecsColor, self.vecsTela, self.vecsFamilia]
            data = [self.vecsColor.tolist(),self.vecsTela.tolist(),self.vecsFamilia.tolist()]
            json.dump(data, f)

    def vector(self, c, d):
        self.valors = self.train.obtenir_list(c)
        n = len(self.valors)
        return self.optimize_positions(n, d)

    def objective_function(self, positions, *args):
        total_error = 0.0

        for v1 in range(len(self.valors)):
            for v2 in self.valors[v1].adjacents:
                actual_distance = distancia(positions[v1], positions[v2])
                desired_distance = self.valors[v1].distancia(self.valors[v2])
                error = (actual_distance - desired_distance) ** 2
                total_error += error

        return total_error

    def optimize_positions(self, n, d):
        initial_positions = np.random.rand(n, d)  # Initialize positions randomly
        #print(initial_positions.shape)
        result = minimize(self.objective_function, initial_positions, args=(),
                        method='L-BFGS-B', options={'disp': True})

        optimized_positions = result.x.reshape((n, d))
        return optimized_positions

categories = ['des_agrup_color_eng', 'des_fabric', 'des_product_family']
