# # image = np.zeros(len(Z)) #Z to ta tablica z wartościami
# # for i in range(len(image)):
# #      image[i] = Z[i]
# # image = image.reshape((n, n))
# # plt.matshow(image)
# # callback(proc_end, plt)
# # plt.close()

import matplotlib.pyplot as plt
import numpy as np            
import random
from statistics import mode
from statistics import StatisticsError

class Grain_grow:


    height = 50 #TODO: tkinter var
    width = 50 #TODO: tkinter var
    image = np.zeros((height, width), dtype=int)
    number_of_grains = 10 #TODO: tkinter var

    def __init__(self):

        # self.testa(self)
        self.seed_random_grains()
        self.update_status_of_grain()
        plt.matshow(self.image)
        plt.show()
        
    def seed_random_grains(self):

        """This fucntion takes matrix of height x width and 
        changes values of random values from 0 to natural number.""" 

        for i in range(self.number_of_grains):
            self.image[random.randint(0, self.height-1), random.randint(0, self.width-1)] = i+1
        # self.image[0, 0] = 11
        return self.image

    def update_status_of_grain(self):

        """This function iterates over every value in matrix and
        if value in 'cell' is equal 0, runs Rules.von_neumann()
        to count most occuring value around that cell using Von Neumann method
        then signs that value to the cell. """
        for i in range(10):
            for row, row_tab in enumerate(self.image):
                for col in range(len(row_tab)):
                    if self.image[row, col] == 0:
                        self.image[row, col] = Rules.von_neumann(self, row, col)

        return self.image

    def testa(self):
        pass
        # self.image[0, 0] = 1

class Rules:


    def von_neumann(self, row, col):

        self.values_of_neighbors = []
        self.cell_coordinates = []
        
        if Grain_grow.image[row, col] == 0:
            self.cell_coordinates.append([row, col])

        if (row-1) < 0: #top
            pass
        else: 
            self.values_of_neighbors.append(Grain_grow.image[row-1, col])

        if (row+1) > Grain_grow.height-2: #bottom
            pass
        else: 
            self.values_of_neighbors.append(Grain_grow.image[row+1, col])

        if (col-1) < 0: #left
            pass
        else: 
            self.values_of_neighbors.append(Grain_grow.image[row, col-1])

        if (col+1) > Grain_grow.width-2: #GeT_RiGhT
            pass
        else: 
            self.values_of_neighbors.append(Grain_grow.image[row, col+1])

        # print(self.values_of_neighbors)



        try:
            value = int(mode(self.values_of_neighbors))
            if value == 0:
                value = max(self.values_of_neighbors)
        

        except StatisticsError:
            value = int(max(self.values_of_neighbors)) 

        return value

if __name__ == '__main__':
    Grain_grow()

