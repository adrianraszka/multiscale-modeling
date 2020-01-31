import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.backends.backend_qt4agg
import numpy as np            
import random
from statistics import mode
from statistics import StatisticsError
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import gui
import math

class Grain_grow():    

    def draw_1st_phase(self, draw1:int, draw2:int, width :int, height :int, number_of_grains :int, von_neumann :bool, moore :bool):
        self.draw1 = draw1
        self.draw2 = draw2
        self.width = width
        self.height = height
        self.number_of_grains = number_of_grains
        self.von_neumann = von_neumann
        self.moore = moore

        self.image = np.zeros((self.width, self.height,), dtype=int)
        self.image_old = np.zeros((self.width, self.height), dtype=int)
        self.seed_random_grains()

        for i in range(0, self.width): 
            for j in range(0, self.height):
                if self.image[i, j] == 0:
                    self.update_status_of_grain()
                else:
                    pass   

        #merge cells into 1 phase
        self.change_to_rgb()
        for g in range(self.draw1):
            print(g)
            for i in range(0, self.width): 
                for j in range(0, self.height):
                    if self.image[i, j] == int(g):
                        self.image[i, j] = 1

        #leave only 1 phase, rest goes white
        for i in range(0, self.width): 
            for j in range(0, self.height):
                if self.image[i, j] != 1:
                    self.copy_of_image[i, j] = [1., 1., 1.]
                else:
                    self.copy_of_image[i, j] = [1., 0., 0.]

        self.start(self.width, self.height, self.draw2, self.von_neumann, self.moore)
        self.phase_image = self.copy_of_image
        self.phase_image = self.phase_image.tolist()
        self.copy_of_image = self.copy_of_image.tolist()
        self.change_to_rgb()
        # for i in range(0, self.width): 
        #     for j in range(0, self.height):

        for i in range(0, self.width): 
            for j in range(0, self.height):
                if self.phase_image[i][j] == [1., 0., 0.]:
                    self.copy_of_image[i][j] = [1., 0., 0.]
                else:
                    pass

        plt.matshow(self.copy_of_image)
        plt.matshow(self.phase_image)
                    
        plt.show()

    def draw_2nd_phase(self):
        pass

    def validate_vals(self, number_of_inclusions_draw:int, size_of_inclusions_draw:int, shape_square_check_bool:bool, shape_circular_check_bool:bool,  width :int, height :int, number_of_grains :int, von_neumann :bool, moore :bool):
        self.number_of_inclusions = number_of_inclusions_draw
        self.size_of_inclusions = size_of_inclusions_draw
        self.shape_square_check = shape_square_check_bool
        self.shape_circular_check = shape_circular_check_bool
        self.width = width
        self.height = height
        self.number_of_grains = number_of_grains
        self.von_neumann = von_neumann
        self.moore = moore

        self.image = np.zeros((self.width, self.height,), dtype=int)
        self.image_old = np.zeros((self.width, self.height), dtype=int)
        self.seed_random_grains()

        for i in range(0, self.width): 
            for j in range(0, self.height):
                if self.image[i, j] == 0:
                    self.update_status_of_grain()
                else:
                    pass   

        self.change_to_rgb()

        if self.shape_circular_check:
            self.circular_inclusions()  
        else:
            self.square_inclusions()

        plt.matshow(self.copy_of_image)
        plt.show()

        # print(self.random_adjacent_cells())

        return self.copy_of_image


    def draw_inc_before(self, number_of_inclusions_draw:int, size_of_inclusions_draw:int, shape_square_check_bool:bool, shape_circular_check_bool:bool,  width :int, height :int, number_of_grains :int, von_neumann :bool, moore :bool):
        self.number_of_inclusions = number_of_inclusions_draw
        self.size_of_inclusions = size_of_inclusions_draw
        self.shape_square_check = shape_square_check_bool
        self.shape_circular_check = shape_circular_check_bool
        self.width = width
        self.height = height
        self.number_of_grains = number_of_grains
        self.von_neumann = von_neumann
        self.moore = moore

        self.image = np.zeros((self.width, self.height,), dtype=int)
        self.image_old = np.zeros((self.width, self.height), dtype=int)
        self.seed_random_grains()

        for i in range(0, self.width): 
            for j in range(0, self.height):
                if self.image[i, j] == 0:
                    self.update_status_of_grain()
                else:
                    pass   

        self.change_to_rgb()

        if self.shape_circular_check:
            self.circular_inclusions_before()  
        else:
            self.square_inclusions_before()

        plt.matshow(self.copy_of_image)
        plt.show()

        # print(self.random_adjacent_cells())

        return self.copy_of_image
    

    def draw_after_before(self, number_of_inclusions_draw:int, size_of_inclusions_draw:int, shape_square_check_bool:bool, shape_circular_check_bool:bool,  width :int, height :int, number_of_grains :int, von_neumann :bool, moore :bool):
        self.number_of_inclusions = number_of_inclusions_draw
        self.size_of_inclusions = size_of_inclusions_draw
        self.shape_square_check = shape_square_check_bool
        self.shape_circular_check = shape_circular_check_bool
        self.width = width
        self.height = height
        self.number_of_grains = number_of_grains
        self.von_neumann = von_neumann
        self.moore = moore

        self.image = np.zeros((self.width, self.height,), dtype=int)
        self.image_old = np.zeros((self.width, self.height), dtype=int)
        self.seed_random_grains()

        for i in range(0, self.width): 
            for j in range(0, self.height):
                if self.image[i, j] == 0:
                    self.update_status_of_grain()
                else:
                    pass   
        

        self.change_to_rgb()

        if self.shape_circular_check:
            self.circular_inclusions_before()  
        else:
            self.square_inclusions_before()

        plt.matshow(self.copy_of_image)
        plt.show()

        return self.copy_of_image
    

    def random_adjacent_cells(self):
        self.adjacent_cells_coords = []
        self.update_status_of_grain()
        for i in range(0, self.width): 
            for j in range(0, self.height):
                ac_temp = []
                try:
                    if self.image[i,j] != self.image[i, j+1]:
                        # print(self.image[i,j], self.image[i, j+1])
                        self.adjacent_cells_coords.append([i,j])
                    else:
                        pass
                except:
                    pass

        # print(self.adjacent_cells)
        return self.adjacent_cells_coords


    def start(self, width :int, height :int, draw2 :int, von_neumann :bool, moore :bool):
        """returns self.image"""
        self.width = width
        self.height = height
        self.number_of_grains = draw2
        self.von_neumann = von_neumann
        self.moore = moore
        
        self.image = np.zeros((self.width, self.height,), dtype=float)
        self.image_old = np.zeros((self.width, self.height), dtype=float)
        self.seed_random_grains()

        for i in range(0, self.width): 
            for j in range(0, self.height):
                if self.image[i, j] == 0:
                    self.update_status_of_grain()
                else:
                    pass   

        # self.change_to_rgb()

        # plt.matshow(self.image)
        return self.image



    def final_image_lab2(self):
        
        if shape_circular_check:
            self.circular_inclusions()  
        else:
            self.square_inclusions()
        # # self.clear_padding_and_axis()
        plt.matshow(self.image_lab2)
        # self.clear_padding_and_axis()
        # plt.show()
        return self.image_lab2


    def change_to_rgb(self):
        """return self.copy_of_image"""
        # self.validate_vals() 
        self.copy_of_image = np.zeros((self.width, self.height, 3), dtype=float)
        # print(self.copy_of_image)
        self.image = self.update_status_of_grain()
        # print(self.image)
        for k in range(1, self.number_of_grains+1):
            # print('k', k)
            r = random.uniform(0.01, 0.99)
            g = random.uniform(0.01, 0.99)
            b = random.uniform(0.01, 0.99)
            for i in range(0, self.width):
                for j in range(0, self.height):
                    if self.image[i, j] == k:
                        # print(self.image[i, j], k)
                        self.copy_of_image[i, j] = [r, g ,b]
                        # print('changed color')
                        # print(self.copy_of_image[i, j])

        return self.copy_of_image


    def odleglosc_2pkt(self, x :float, y :float, k :float, j :float):
        return math.sqrt(pow(x - (x+k), 2) + pow(y - (y+j), 2))


    def circular_inclusions(self):
        self.random_neighbors = self.random_adjacent_cells()
        black = [0, 0, 0]
        for i in range(self.number_of_inclusions):
            random_from_list = random.choice(self.random_neighbors)
            x = random_from_list[0]
            y = random_from_list[1]
            self.copy_of_image[x, y] = black
            R = self.size_of_inclusions
            for k in range(-R, R+1, 1):
                for j in range(-R, R+1, 1):
                    R_r = self.odleglosc_2pkt(x, y, k, j)
                    # print(x, y, k, j, R_r)
                    if R_r < R:
                        try:
                            self.copy_of_image[x+k , y+j] = black
                        except:
                            pass
        
        return self.copy_of_image


    def square_inclusions(self):
        self.random_neighbors = self.random_adjacent_cells()
        black = [0, 0, 0]
        for i in range(self.number_of_inclusions):
            random_from_list = random.choice(self.random_neighbors)
            x = random_from_list[0]
            y = random_from_list[1]
            self.copy_of_image[x, y] = black
            R = self.size_of_inclusions//2
            for k in range(-R, R+1, 1):
                for j in range(-R, R+1, 1):
                    try:
                        self.copy_of_image[x+k , y+j] = black
                    except:
                        pass

        return self.copy_of_image


    def circular_inclusions_before(self):
        black = [0, 0, 0]
        for i in range(self.number_of_inclusions):
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            self.copy_of_image[x, y] = black
            R = self.size_of_inclusions
            for k in range(-R, R+1, 1):
                for j in range(-R, R+1, 1):
                    R_r = self.odleglosc_2pkt(x, y, k, j)
                    # print(x, y, k, j, R_r)
                    if R_r < R:
                        try:
                            self.copy_of_image[x+k , y+j] = black
                        except:
                            pass
        
        return self.copy_of_image


    def square_inclusions_before(self):
        black = [0, 0, 0]
        for i in range(self.number_of_inclusions):
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            self.copy_of_image[x, y] = black
            R = self.size_of_inclusions//2
            for k in range(-R, R+1, 1):
                for j in range(-R, R+1, 1):
                    try:
                        self.copy_of_image[x+k , y+j] = black
                    except:
                        pass

        return self.copy_of_image


    def seed_random_grains(self):
        """This fucntion takes matrix of height x width and 
        changes values of random values from 0 to natural number.""" 

        for i in range(self.number_of_grains):
            self.image[random.randint(0, self.width-1), random.randint(0, self.height-1)] = i
        return self.image


    def update_status_of_grain(self):
        """This function iterates over every value in matrix and
        if value in 'cell' is equal 0, runs von_neumann_fx()
        to count most occuring value around that cell using Von Neumann method
        then signs that value to the cell. 
        PS. Returns self.image"""

        self.copy_image()
        
        for row, row_tab in enumerate(self.image_old):
            for col in range(len(row_tab)):
                if self.image_old[row, col] == 0:
                    if self.von_neumann:
                        self.image[row, col] = self.von_neumann_fx(row, col)
                    else:
                        self.image[row, col] = self.moore_fx(row, col)

        # print('moore:', self.moore)
        # print('von_neuman:', self.von_neumann)
        return self.image 


    def copy_image(self):
        """Create copy of newest image""" 

        for i in range(0, self.width):
            for j in range(0, self.height): 
                self.image_old[i, j] = self.image[i, j]
      
        return self.image_old


    def reset_image(self):
        """Reset matrix to zeros at every position."""
        row, col = 0, 0
        for i in range(0, self.width): 
            for j in range(0, self.height): 
                self.image[i, j] = self.image[row, col]

        return self.image


    def import_image(self):
        """Import image by name, only name of an image can change, location is fixed.""" 
        
        self.img = mpimg.imread('C:/Users/adeq/Desktop/{}.png'.format(import_name))
        self.image = self.imp
        return self.image


    def clear_padding_and_axis(self):
        plt.gca().set_axis_off()
        plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
                    hspace = 0, wspace = 0)
        plt.margins(0,0)
        plt.gca().xaxis.set_major_locator(plt.NullLocator())
        plt.gca().yaxis.set_major_locator(plt.NullLocator())


    def von_neumann_fx(self, row, col):

        self.values_of_neighbors = []

        if (row-1) < 0: #top
            pass
        else: 
            self.values_of_neighbors.append(self.image_old[row-1, col])

        if (row+1) > self.width-1: #bottom
            pass
        else: 
            self.values_of_neighbors.append(self.image_old[row+1, col])

        if (col-1) < 0: #left
            pass
        else: 
            self.values_of_neighbors.append(self.image_old[row, col-1])

        if (col+1) > self.height-1: #GeT_RiGhT
            pass
        else: 
            self.values_of_neighbors.append(self.image_old[row, col+1])

        try:
            value = int(mode(self.values_of_neighbors))
            if value == 0:
                value = max(self.values_of_neighbors)
        
        except StatisticsError:
            value = int(max(self.values_of_neighbors)) 

        return value


    def moore_fx(self, row, col):

        self.values_of_neighbors_moore = []

        # coords_moore = [[row-1, col-1], [row-1, col],   [row-1, col+1], #123
        #                 [row,   col-1], [row,   col],   [row,   col+1], #456
        #                 [row+1, col-1], [row+1, col],   [row+1, col+1]] #789

        try:
            self.values_of_neighbors_moore.append(self.image_old[row-1, col-1]) #1
        except:
            pass
        try:
            self.values_of_neighbors_moore.append(self.image_old[row-1, col]) #2 
        except:
            pass
        try:
            self.values_of_neighbors_moore.append(self.image_old[row-1, col+1])# 3
        except:
            pass
        try:
            self.values_of_neighbors_moore.append(self.image_old[row,   col-1]) #4
        except:
            pass
        try:
            self.values_of_neighbors_moore.append(self.image_old[row,   col]) #5
        except:
            pass
        try:
            self.values_of_neighbors_moore.append(self.image_old[row,   col+1]) # 6
        except:
            pass
        try:
            self.values_of_neighbors_moore.append(self.image_old[row+1, col-1]) # 7
        except:
            pass
        try:
            self.values_of_neighbors_moore.append(self.image_old[row+1, col]) # 8
        except:
            pass
        try:
            self.values_of_neighbors_moore.append(self.image_old[row+1, col+1]) #9
        except:
            pass


        try:
            value = int(mode(self.values_of_neighbors_moore))
            if value == 0:
                value = max(self.values_of_neighbors_moore)
        
        except StatisticsError:
            value = int(max(self.values_of_neighbors_moore)) 

        return value


if __name__ == "__main__":
    gr = Grain_grow()
