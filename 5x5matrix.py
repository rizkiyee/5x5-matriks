import threading
import time

#array matriks dideklarasikan dan digambarkan sebagai berikut

                            
matrix_a = [[1, 2, 3, 2, 1],       
            [4, 5, 6, 5, 4],       
            [7, 8, 9, 8, 9],      
            [6, 5, 4, 5, 6],      
            [3, 2, 1, 2, 3]]       

matrix_b = [[9, 8, 7, 8, 9], 
            [6, 5, 4, 5, 6], 
            [3, 2, 1, 5, 4], 
            [4, 5, 6, 5, 4], 
            [7, 8, 9, 2, 1]]

#ini adalah hasil perkalian a * b
matrix_w = [[0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0]]


matrix_c = [[1, 2, 3, 4, 6],
            [2, 3, 5, 6, 4],
            [4, 1, 3, 5, 2],
            [2, 1 ,3, 4, 6],
            [2, 2, 4, 5, 2]]

matrix_d = [[9, 5, 4, 2, 5],
            [7, 6, 2, 3, 2], 
            [1, 6, 7, 8, 6],
            [2, 3, 5, 6, 2],
            [1, 2, 6, 9, 8]]

#ini adalah hasil perkalian matrix c*d
matrix_x = [[0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0]]

matrix_e = [[1, 2, 3, 2, 1],       
            [4, 5, 6, 5, 4],       
            [7, 8, 9, 8, 9],      
            [6, 5, 4, 5, 6],      
            [3, 2, 1, 2, 3]]

matrix_f = [[9, 8, 7, 8, 9], 
            [6, 5, 4, 5, 6], 
            [3, 2, 1, 5, 4], 
            [4, 5, 6, 5, 4], 
            [7, 8, 9, 2, 1]]

#ini adalah hasil perkalian matrix e*f
matrix_y = [[0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0]]

matrix_g = [[1, 2, 3, 4, 6],
            [2, 3, 5, 6, 4],
            [4, 1, 3, 5, 2],
            [2, 1 ,3, 4, 6],
            [2, 2, 4, 5, 2]]
            
matrix_h = [[9, 5, 4, 2, 5],
            [7, 6, 2, 3, 2], 
            [1, 6, 7, 8, 6],
            [2, 3, 5, 6, 2],
            [1, 2, 6, 9, 8]]

#ini adalah hasil perkalian matrix g*h
matrix_z = [[0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0]]

#ini adalah hasil perkalian matrix axb * cxd 
matrix_wx = [[0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0]]
#ini adalah hasil perkalian matrix y*z
matrix_yz = [[0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0]]

#ini adalah hasil perkalian semua matrix 
matrix_semua = [[0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0]]



#dekomposisi dan operasi untuk mendapatkan hasil dari matriks,
#menggunakan 1 thread per baris.

class Thread1(threading.Thread):        #0|0, 0, 0, 0, 0| 
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        print ("Starting " + self.name + "\n")

        matrix_w[0][0] = matrix_a[0][0] * matrix_b[0][0] + matrix_a[0][1] * matrix_b[1][0] + matrix_a[0][2] * matrix_b[2][0] + matrix_a[0][3] * matrix_b[3][0] + matrix_a[0][4] * matrix_b[4][0]
        matrix_w[0][1] = matrix_a[0][0] * matrix_b[0][1] + matrix_a[0][1] * matrix_b[1][1] + matrix_a[0][2] * matrix_b[2][1] + matrix_a[0][3] * matrix_b[3][1] + matrix_a[0][4] * matrix_b[4][1]
        matrix_w[0][2] = matrix_a[0][0] * matrix_b[0][2] + matrix_a[0][1] * matrix_b[1][2] + matrix_a[0][2] * matrix_b[2][2] + matrix_a[0][3] * matrix_b[3][2] + matrix_a[0][4] * matrix_b[4][2]
        matrix_w[0][3] = matrix_a[0][0] * matrix_b[0][3] + matrix_a[0][1] * matrix_b[1][3] + matrix_a[0][2] * matrix_b[2][3] + matrix_a[0][3] * matrix_b[3][3] + matrix_a[0][4] * matrix_b[4][3]
        matrix_w[0][4] = matrix_a[0][0] * matrix_b[0][4] + matrix_a[0][1] * matrix_b[1][4] + matrix_a[0][2] * matrix_b[2][4] + matrix_a[0][3] * matrix_b[3][4] + matrix_a[0][4] * matrix_b[4][4]
        
        matrix_x[0][0] = matrix_c[0][0] * matrix_d[0][0] + matrix_c[0][1] * matrix_d[1][0] + matrix_c[0][2] * matrix_d[2][0] + matrix_c[0][3] * matrix_d[3][0] + matrix_c[0][4] * matrix_d[4][0]
        matrix_x[0][1] = matrix_c[0][0] * matrix_d[0][1] + matrix_c[0][1] * matrix_d[1][1] + matrix_c[0][2] * matrix_d[2][1] + matrix_c[0][3] * matrix_d[3][1] + matrix_c[0][4] * matrix_d[4][1]
        matrix_x[0][2] = matrix_c[0][0] * matrix_d[0][2] + matrix_c[0][1] * matrix_d[1][2] + matrix_c[0][2] * matrix_d[2][2] + matrix_c[0][3] * matrix_d[3][2] + matrix_c[0][4] * matrix_d[4][2]
        matrix_x[0][3] = matrix_c[0][0] * matrix_d[0][3] + matrix_c[0][1] * matrix_d[1][3] + matrix_c[0][2] * matrix_d[2][3] + matrix_c[0][3] * matrix_d[3][3] + matrix_c[0][4] * matrix_d[4][3]
        matrix_x[0][4] = matrix_c[0][0] * matrix_d[0][4] + matrix_c[0][1] * matrix_d[1][4] + matrix_c[0][2] * matrix_d[2][4] + matrix_c[0][3] * matrix_d[3][4] + matrix_c[0][4] * matrix_d[4][4]

        matrix_wx[0][0] = matrix_w[0][0] * matrix_x[0][0] + matrix_w[0][1] * matrix_x[1][0] + matrix_w[0][2] * matrix_x[2][0] + matrix_w[0][3] * matrix_x[3][0] + matrix_w[0][4] * matrix_x[4][0]
        matrix_wx[0][1] = matrix_w[0][0] * matrix_x[0][1] + matrix_w[0][1] * matrix_x[1][1] + matrix_w[0][2] * matrix_x[2][1] + matrix_w[0][3] * matrix_x[3][1] + matrix_w[0][4] * matrix_x[4][1]
        matrix_wx[0][2] = matrix_w[0][0] * matrix_x[0][2] + matrix_w[0][1] * matrix_x[1][2] + matrix_w[0][2] * matrix_x[2][2] + matrix_w[0][3] * matrix_x[3][2] + matrix_w[0][4] * matrix_x[4][2]
        matrix_wx[0][3] = matrix_w[0][0] * matrix_x[0][3] + matrix_w[0][1] * matrix_x[1][3] + matrix_w[0][2] * matrix_x[2][3] + matrix_w[0][3] * matrix_x[3][3] + matrix_w[0][4] * matrix_x[4][3]
        matrix_wx[0][4] = matrix_w[0][0] * matrix_x[0][4] + matrix_w[0][1] * matrix_x[1][4] + matrix_w[0][2] * matrix_x[2][4] + matrix_w[0][3] * matrix_x[3][4] + matrix_w[0][4] * matrix_x[4][4]

        matrix_y[0][0] = matrix_e[0][0] * matrix_f[0][0] + matrix_e[0][1] * matrix_f[1][0] + matrix_e[0][2] * matrix_f[2][0] + matrix_e[0][3] * matrix_f[3][0] + matrix_e[0][4] * matrix_f[4][0]
        matrix_y[0][1] = matrix_e[0][0] * matrix_f[0][1] + matrix_e[0][1] * matrix_f[1][1] + matrix_e[0][2] * matrix_f[2][1] + matrix_e[0][3] * matrix_f[3][1] + matrix_e[0][4] * matrix_f[4][1]
        matrix_y[0][2] = matrix_e[0][0] * matrix_f[0][2] + matrix_e[0][1] * matrix_f[1][2] + matrix_e[0][2] * matrix_f[2][2] + matrix_e[0][3] * matrix_f[3][2] + matrix_e[0][4] * matrix_f[4][2]
        matrix_y[0][3] = matrix_e[0][0] * matrix_f[0][3] + matrix_e[0][1] * matrix_f[1][3] + matrix_e[0][2] * matrix_f[2][3] + matrix_e[0][3] * matrix_f[3][3] + matrix_e[0][4] * matrix_f[4][3]
        matrix_y[0][4] = matrix_e[0][0] * matrix_f[0][4] + matrix_e[0][1] * matrix_f[1][4] + matrix_e[0][2] * matrix_f[2][4] + matrix_e[0][3] * matrix_f[3][4] + matrix_e[0][4] * matrix_f[4][4]

        matrix_z[0][0] = matrix_g[0][0] * matrix_h[0][0] + matrix_h[0][1] * matrix_h[1][0] + matrix_g[0][2] * matrix_h[2][0] + matrix_g[0][3] * matrix_h[3][0] + matrix_h[0][4] * matrix_h[4][0]
        matrix_z[0][1] = matrix_g[0][0] * matrix_h[0][1] + matrix_h[0][1] * matrix_h[1][1] + matrix_g[0][2] * matrix_h[2][1] + matrix_g[0][3] * matrix_h[3][1] + matrix_h[0][4] * matrix_h[4][1]
        matrix_z[0][2] = matrix_g[0][0] * matrix_h[0][2] + matrix_h[0][1] * matrix_h[1][2] + matrix_g[0][2] * matrix_h[2][2] + matrix_g[0][3] * matrix_h[3][2] + matrix_h[0][4] * matrix_h[4][2]
        matrix_z[0][3] = matrix_g[0][0] * matrix_h[0][3] + matrix_h[0][1] * matrix_h[1][3] + matrix_g[0][2] * matrix_h[2][3] + matrix_g[0][3] * matrix_h[3][3] + matrix_h[0][4] * matrix_h[4][3]
        matrix_z[0][4] = matrix_g[0][0] * matrix_h[0][4] + matrix_h[0][1] * matrix_h[1][4] + matrix_g[0][2] * matrix_h[2][4] + matrix_g[0][3] * matrix_h[3][4] + matrix_h[0][4] * matrix_h[4][4]

        matrix_yz[0][0] = matrix_y[0][0] * matrix_z[0][0] + matrix_y[0][1] * matrix_z[1][0] + matrix_y[0][2] * matrix_z[2][0] + matrix_y[0][3] * matrix_z[3][0] + matrix_y[0][4] * matrix_z[4][0]
        matrix_yz[0][1] = matrix_y[0][0] * matrix_z[0][1] + matrix_y[0][1] * matrix_z[1][1] + matrix_y[0][2] * matrix_z[2][1] + matrix_y[0][3] * matrix_z[3][1] + matrix_y[0][4] * matrix_z[4][1]
        matrix_yz[0][2] = matrix_y[0][0] * matrix_z[0][2] + matrix_y[0][1] * matrix_z[1][2] + matrix_y[0][2] * matrix_z[2][2] + matrix_y[0][3] * matrix_z[3][2] + matrix_y[0][4] * matrix_z[4][2]
        matrix_yz[0][3] = matrix_y[0][0] * matrix_z[0][3] + matrix_y[0][1] * matrix_z[1][3] + matrix_y[0][2] * matrix_z[2][3] + matrix_y[0][3] * matrix_z[3][3] + matrix_y[0][4] * matrix_z[4][3]
        matrix_yz[0][4] = matrix_y[0][0] * matrix_z[0][4] + matrix_y[0][1] * matrix_z[1][4] + matrix_y[0][2] * matrix_z[2][4] + matrix_y[0][3] * matrix_z[3][4] + matrix_y[0][4] * matrix_z[4][4]

        matrix_semua[0][0] = matrix_wx[0][0] * matrix_yz[0][0] + matrix_wx[0][1] * matrix_yz[1][0] + matrix_wx[0][2] * matrix_yz[2][0] + matrix_wx[0][3] * matrix_yz[3][0] + matrix_wx[0][4] * matrix_yz[4][0]
        matrix_semua[0][1] = matrix_wx[0][0] * matrix_yz[0][1] + matrix_wx[0][1] * matrix_yz[1][1] + matrix_wx[0][2] * matrix_yz[2][1] + matrix_wx[0][3] * matrix_yz[3][1] + matrix_wx[0][4] * matrix_yz[4][1]
        matrix_semua[0][2] = matrix_wx[0][0] * matrix_yz[0][2] + matrix_wx[0][1] * matrix_yz[1][2] + matrix_wx[0][2] * matrix_yz[2][2] + matrix_wx[0][3] * matrix_yz[3][2] + matrix_wx[0][4] * matrix_yz[4][2]
        matrix_semua[0][3] = matrix_wx[0][0] * matrix_yz[0][3] + matrix_wx[0][1] * matrix_yz[1][3] + matrix_wx[0][2] * matrix_yz[2][3] + matrix_wx[0][3] * matrix_yz[3][3] + matrix_wx[0][4] * matrix_yz[4][3]
        matrix_semua[0][4] = matrix_wx[0][0] * matrix_yz[0][4] + matrix_wx[0][1] * matrix_yz[1][4] + matrix_wx[0][2] * matrix_yz[2][4] + matrix_wx[0][3] * matrix_yz[3][4] + matrix_wx[0][4] * matrix_yz[4][4]

        

        print ("End " + self.name + "\n")


class Thread2(threading.Thread):        #1|0, 0, 0, 0, 0|
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        print ("Starting " + self.name + "\n")

        matrix_w[1][0] = matrix_a[1][0] * matrix_b[0][0] + matrix_a[1][1] * matrix_b[1][0] + matrix_a[1][2] * matrix_b[2][0] + matrix_a[1][3] * matrix_b[3][0] + matrix_a[1][4] * matrix_b[4][0]
        matrix_w[1][1] = matrix_a[1][0] * matrix_b[0][1] + matrix_a[1][1] * matrix_b[1][1] + matrix_a[1][2] * matrix_b[2][1] + matrix_a[1][3] * matrix_b[3][1] + matrix_a[1][4] * matrix_b[4][1]
        matrix_w[1][2] = matrix_a[1][0] * matrix_b[0][2] + matrix_a[1][1] * matrix_b[1][2] + matrix_a[1][2] * matrix_b[2][2] + matrix_a[1][3] * matrix_b[3][2] + matrix_a[1][4] * matrix_b[4][2]
        matrix_w[1][3] = matrix_a[1][0] * matrix_b[0][3] + matrix_a[1][1] * matrix_b[1][3] + matrix_a[1][2] * matrix_b[2][3] + matrix_a[1][3] * matrix_b[3][3] + matrix_a[1][4] * matrix_b[4][3]
        matrix_w[1][4] = matrix_a[1][0] * matrix_b[0][4] + matrix_a[1][1] * matrix_b[1][4] + matrix_a[1][2] * matrix_b[2][4] + matrix_a[1][3] * matrix_b[3][4] + matrix_a[1][4] * matrix_b[4][4]

        matrix_x[1][0] = matrix_c[1][0] * matrix_d[0][0] + matrix_c[1][1] * matrix_d[1][0] + matrix_c[1][2] * matrix_d[2][0] + matrix_c[1][3] * matrix_d[3][0] + matrix_c[1][4] * matrix_d[4][0]
        matrix_x[1][1] = matrix_c[1][0] * matrix_d[0][1] + matrix_c[1][1] * matrix_d[1][1] + matrix_c[1][2] * matrix_d[2][1] + matrix_c[1][3] * matrix_d[3][1] + matrix_c[1][4] * matrix_d[4][1]
        matrix_x[1][2] = matrix_c[1][0] * matrix_d[0][2] + matrix_c[1][1] * matrix_d[1][2] + matrix_c[1][2] * matrix_d[2][2] + matrix_c[1][3] * matrix_d[3][2] + matrix_c[1][4] * matrix_d[4][2]
        matrix_x[1][3] = matrix_c[1][0] * matrix_d[0][3] + matrix_c[1][1] * matrix_d[1][3] + matrix_c[1][2] * matrix_d[2][3] + matrix_c[1][3] * matrix_d[3][3] + matrix_c[1][4] * matrix_d[4][3]
        matrix_x[1][4] = matrix_c[1][0] * matrix_d[0][4] + matrix_c[1][1] * matrix_d[1][4] + matrix_c[1][2] * matrix_d[2][4] + matrix_c[1][3] * matrix_d[3][4] + matrix_c[1][4] * matrix_d[4][4]

        matrix_wx[1][0] = matrix_w[1][0] * matrix_x[0][0] + matrix_w[1][1] * matrix_x[1][0] + matrix_w[1][2] * matrix_x[2][0] + matrix_w[1][3] * matrix_x[3][0] + matrix_w[1][4] * matrix_x[4][0]
        matrix_wx[1][1] = matrix_w[1][0] * matrix_x[0][1] + matrix_w[1][1] * matrix_x[1][1] + matrix_w[1][2] * matrix_x[2][1] + matrix_w[1][3] * matrix_x[3][1] + matrix_w[1][4] * matrix_x[4][1]
        matrix_wx[1][2] = matrix_w[1][0] * matrix_x[0][2] + matrix_w[1][1] * matrix_x[1][2] + matrix_w[1][2] * matrix_x[2][2] + matrix_w[1][3] * matrix_x[3][2] + matrix_w[1][4] * matrix_x[4][2]
        matrix_wx[1][3] = matrix_w[1][0] * matrix_x[0][3] + matrix_w[1][1] * matrix_x[1][3] + matrix_w[1][2] * matrix_x[2][3] + matrix_w[1][3] * matrix_x[3][3] + matrix_w[1][4] * matrix_x[4][3]
        matrix_wx[1][4] = matrix_w[1][0] * matrix_x[0][4] + matrix_w[1][1] * matrix_x[1][4] + matrix_w[1][2] * matrix_x[2][4] + matrix_w[1][3] * matrix_x[3][4] + matrix_w[1][4] * matrix_x[4][4]

        matrix_y[1][0] = matrix_e[1][0] * matrix_f[0][0] + matrix_e[1][1] * matrix_f[1][0] + matrix_e[1][2] * matrix_f[2][0] + matrix_e[1][3] * matrix_f[3][0] + matrix_e[1][4] * matrix_f[4][0]
        matrix_y[1][1] = matrix_e[1][0] * matrix_f[0][1] + matrix_e[1][1] * matrix_f[1][1] + matrix_e[1][2] * matrix_f[2][1] + matrix_e[1][3] * matrix_f[3][1] + matrix_e[1][4] * matrix_f[4][1]
        matrix_y[1][2] = matrix_e[1][0] * matrix_f[0][2] + matrix_e[1][1] * matrix_f[1][2] + matrix_e[1][2] * matrix_f[2][2] + matrix_e[1][3] * matrix_f[3][2] + matrix_e[1][4] * matrix_f[4][2]
        matrix_y[1][3] = matrix_e[1][0] * matrix_f[0][3] + matrix_e[1][1] * matrix_f[1][3] + matrix_e[1][2] * matrix_f[2][3] + matrix_e[1][3] * matrix_f[3][3] + matrix_e[1][4] * matrix_f[4][3]
        matrix_y[1][4] = matrix_e[1][0] * matrix_f[0][4] + matrix_e[1][1] * matrix_f[1][4] + matrix_e[1][2] * matrix_f[2][4] + matrix_e[1][3] * matrix_f[3][4] + matrix_e[1][4] * matrix_f[4][4]

        matrix_z[1][0] = matrix_g[1][0] * matrix_h[0][0] + matrix_h[1][1] * matrix_h[1][0] + matrix_g[1][2] * matrix_h[2][0] + matrix_g[1][3] * matrix_h[3][0] + matrix_h[1][4] * matrix_h[4][0]
        matrix_z[1][1] = matrix_g[1][0] * matrix_h[0][1] + matrix_h[1][1] * matrix_h[1][1] + matrix_g[1][2] * matrix_h[2][1] + matrix_g[1][3] * matrix_h[3][1] + matrix_h[1][4] * matrix_h[4][1]
        matrix_z[1][2] = matrix_g[1][0] * matrix_h[0][2] + matrix_h[1][1] * matrix_h[1][2] + matrix_g[1][2] * matrix_h[2][2] + matrix_g[1][3] * matrix_h[3][2] + matrix_h[1][4] * matrix_h[4][2]
        matrix_z[1][3] = matrix_g[1][0] * matrix_h[0][3] + matrix_h[1][1] * matrix_h[1][3] + matrix_g[1][2] * matrix_h[2][3] + matrix_g[1][3] * matrix_h[3][3] + matrix_h[1][4] * matrix_h[4][3]
        matrix_z[1][4] = matrix_g[1][0] * matrix_h[0][4] + matrix_h[1][1] * matrix_h[1][4] + matrix_g[1][2] * matrix_h[2][4] + matrix_g[1][3] * matrix_h[3][4] + matrix_h[1][4] * matrix_h[4][4]

        matrix_yz[1][0] = matrix_y[1][0] * matrix_z[0][0] + matrix_y[1][1] * matrix_z[1][0] + matrix_y[1][2] * matrix_z[2][0] + matrix_y[1][3] * matrix_z[3][0] + matrix_y[1][4] * matrix_z[4][0]
        matrix_yz[1][1] = matrix_y[1][0] * matrix_z[0][1] + matrix_y[1][1] * matrix_z[1][1] + matrix_y[1][2] * matrix_z[2][1] + matrix_y[1][3] * matrix_z[3][1] + matrix_y[1][4] * matrix_z[4][1]
        matrix_yz[1][2] = matrix_y[1][0] * matrix_z[0][2] + matrix_y[1][1] * matrix_z[1][2] + matrix_y[1][2] * matrix_z[2][2] + matrix_y[1][3] * matrix_z[3][2] + matrix_y[1][4] * matrix_z[4][2]
        matrix_yz[1][3] = matrix_y[1][0] * matrix_z[0][3] + matrix_y[1][1] * matrix_z[1][3] + matrix_y[1][2] * matrix_z[2][3] + matrix_y[1][3] * matrix_z[3][3] + matrix_y[1][4] * matrix_z[4][3]
        matrix_yz[1][4] = matrix_y[1][0] * matrix_z[0][4] + matrix_y[1][1] * matrix_z[1][4] + matrix_y[1][2] * matrix_z[2][4] + matrix_y[1][3] * matrix_z[3][4] + matrix_y[1][4] * matrix_z[4][4]


    #hasil matrix seumanya
        matrix_semua[1][0] = matrix_wx[1][0] * matrix_yz[0][0] + matrix_wx[1][1] * matrix_yz[1][0] + matrix_wx[1][2] * matrix_yz[2][0] + matrix_wx[1][3] * matrix_yz[3][0] + matrix_wx[1][4] * matrix_yz[4][0]
        matrix_semua[1][1] = matrix_wx[1][0] * matrix_yz[0][1] + matrix_wx[1][1] * matrix_yz[1][1] + matrix_wx[1][2] * matrix_yz[2][1] + matrix_wx[1][3] * matrix_yz[3][1] + matrix_wx[1][4] * matrix_yz[4][1]
        matrix_semua[1][2] = matrix_wx[1][0] * matrix_yz[0][2] + matrix_wx[1][1] * matrix_yz[1][2] + matrix_wx[1][2] * matrix_yz[2][2] + matrix_wx[1][3] * matrix_yz[3][2] + matrix_wx[1][4] * matrix_yz[4][2]
        matrix_semua[1][3] = matrix_wx[1][0] * matrix_yz[0][3] + matrix_wx[1][1] * matrix_yz[1][3] + matrix_wx[1][2] * matrix_yz[2][3] + matrix_wx[1][3] * matrix_yz[3][3] + matrix_wx[1][4] * matrix_yz[4][3]
        matrix_semua[1][4] = matrix_wx[1][0] * matrix_yz[0][4] + matrix_wx[1][1] * matrix_yz[1][4] + matrix_wx[1][2] * matrix_yz[2][4] + matrix_wx[1][3] * matrix_yz[3][4] + matrix_wx[1][4] * matrix_yz[4][4]

        print ("End " + self.name + "\n")


class Thread3(threading.Thread):        #2|0, 0, 0, 0, 0|
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        print ("Starting " + self.name + "\n")

        matrix_w[2][0] = matrix_a[2][0] * matrix_b[0][0] + matrix_a[2][1] * matrix_b[1][0] + matrix_a[2][2] * matrix_b[2][0] + matrix_a[2][3] * matrix_b[3][0] + matrix_a[2][4] * matrix_b[4][0]
        matrix_w[2][1] = matrix_a[2][0] * matrix_b[0][1] + matrix_a[2][1] * matrix_b[1][1] + matrix_a[2][2] * matrix_b[2][1] + matrix_a[2][3] * matrix_b[3][1] + matrix_a[2][4] * matrix_b[4][1]
        matrix_w[2][2] = matrix_a[2][0] * matrix_b[0][2] + matrix_a[2][1] * matrix_b[1][2] + matrix_a[2][2] * matrix_b[2][2] + matrix_a[2][3] * matrix_b[3][2] + matrix_a[2][4] * matrix_b[4][2]
        matrix_w[2][3] = matrix_a[2][0] * matrix_b[0][3] + matrix_a[2][1] * matrix_b[1][3] + matrix_a[2][2] * matrix_b[2][3] + matrix_a[2][3] * matrix_b[3][3] + matrix_a[2][4] * matrix_b[4][3]
        matrix_w[2][4] = matrix_a[2][0] * matrix_b[0][4] + matrix_a[2][1] * matrix_b[1][4] + matrix_a[2][2] * matrix_b[2][4] + matrix_a[2][3] * matrix_b[3][4] + matrix_a[2][4] * matrix_b[4][4]

        matrix_x[2][0] = matrix_c[2][0] * matrix_d[0][0] + matrix_c[2][1] * matrix_d[1][0] + matrix_c[2][2] * matrix_d[2][0] + matrix_c[2][3] * matrix_d[3][0] + matrix_c[2][4] * matrix_d[4][0]
        matrix_x[2][1] = matrix_c[2][0] * matrix_d[0][1] + matrix_c[2][1] * matrix_d[1][1] + matrix_c[2][2] * matrix_d[2][1] + matrix_c[2][3] * matrix_d[3][1] + matrix_c[2][4] * matrix_d[4][1]
        matrix_x[2][2] = matrix_c[2][0] * matrix_d[0][2] + matrix_c[2][1] * matrix_d[1][2] + matrix_c[2][2] * matrix_d[2][2] + matrix_c[2][3] * matrix_d[3][2] + matrix_c[2][4] * matrix_d[4][2]
        matrix_x[2][3] = matrix_c[2][0] * matrix_d[0][3] + matrix_c[2][1] * matrix_d[1][3] + matrix_c[2][2] * matrix_d[2][3] + matrix_c[2][3] * matrix_d[3][3] + matrix_c[2][4] * matrix_d[4][3]
        matrix_x[2][4] = matrix_c[2][0] * matrix_d[0][4] + matrix_c[2][1] * matrix_d[1][4] + matrix_c[2][2] * matrix_d[2][4] + matrix_c[2][3] * matrix_d[3][4] + matrix_c[2][4] * matrix_d[4][4]

        matrix_wx[2][0] = matrix_w[2][0] * matrix_x[0][0] + matrix_w[2][1] * matrix_x[1][0] + matrix_w[2][2] * matrix_x[2][0] + matrix_w[2][3] * matrix_x[3][0] + matrix_w[2][4] * matrix_x[4][0]
        matrix_wx[2][1] = matrix_w[2][0] * matrix_x[0][1] + matrix_w[2][1] * matrix_x[1][1] + matrix_w[2][2] * matrix_x[2][1] + matrix_w[2][3] * matrix_x[3][1] + matrix_w[2][4] * matrix_x[4][1]
        matrix_wx[2][2] = matrix_w[2][0] * matrix_x[0][2] + matrix_w[2][1] * matrix_x[1][2] + matrix_w[2][2] * matrix_x[2][2] + matrix_w[2][3] * matrix_x[3][2] + matrix_w[2][4] * matrix_x[4][2]
        matrix_wx[2][3] = matrix_w[2][0] * matrix_x[0][3] + matrix_w[2][1] * matrix_x[1][3] + matrix_w[2][2] * matrix_x[2][3] + matrix_w[2][3] * matrix_x[3][3] + matrix_w[2][4] * matrix_x[4][3]
        matrix_wx[2][4] = matrix_w[2][0] * matrix_x[0][4] + matrix_w[2][1] * matrix_x[1][4] + matrix_w[2][2] * matrix_x[2][4] + matrix_w[2][3] * matrix_x[3][4] + matrix_w[2][4] * matrix_x[4][4]

        matrix_y[2][0] = matrix_e[2][0] * matrix_f[0][0] + matrix_e[2][1] * matrix_f[1][0] + matrix_e[2][2] * matrix_f[2][0] + matrix_e[2][3] * matrix_f[3][0] + matrix_e[2][4] * matrix_f[4][0]
        matrix_y[2][1] = matrix_e[2][0] * matrix_f[0][1] + matrix_e[2][1] * matrix_f[1][1] + matrix_e[2][2] * matrix_f[2][1] + matrix_e[2][3] * matrix_f[3][1] + matrix_e[2][4] * matrix_f[4][1]
        matrix_y[2][2] = matrix_e[2][0] * matrix_f[0][2] + matrix_e[2][1] * matrix_f[1][2] + matrix_e[2][2] * matrix_f[2][2] + matrix_e[2][3] * matrix_f[3][2] + matrix_e[2][4] * matrix_f[4][2]
        matrix_y[2][3] = matrix_e[2][0] * matrix_f[0][3] + matrix_e[2][1] * matrix_f[1][3] + matrix_e[2][2] * matrix_f[2][3] + matrix_e[2][3] * matrix_f[3][3] + matrix_e[2][4] * matrix_f[4][3]
        matrix_y[2][4] = matrix_e[2][0] * matrix_f[0][4] + matrix_e[2][1] * matrix_f[1][4] + matrix_e[2][2] * matrix_f[2][4] + matrix_e[2][3] * matrix_f[3][4] + matrix_e[2][4] * matrix_f[4][4]

        matrix_z[2][0] = matrix_g[2][0] * matrix_h[0][0] + matrix_h[2][1] * matrix_h[1][0] + matrix_g[2][2] * matrix_h[2][0] + matrix_g[2][3] * matrix_h[3][0] + matrix_h[2][4] * matrix_h[4][0]
        matrix_z[2][1] = matrix_g[2][0] * matrix_h[0][1] + matrix_h[2][1] * matrix_h[1][1] + matrix_g[2][2] * matrix_h[2][1] + matrix_g[2][3] * matrix_h[3][1] + matrix_h[2][4] * matrix_h[4][1]
        matrix_z[2][2] = matrix_g[2][0] * matrix_h[0][2] + matrix_h[2][1] * matrix_h[1][2] + matrix_g[2][2] * matrix_h[2][2] + matrix_g[2][3] * matrix_h[3][2] + matrix_h[2][4] * matrix_h[4][2]
        matrix_z[2][3] = matrix_g[2][0] * matrix_h[0][3] + matrix_h[2][1] * matrix_h[1][3] + matrix_g[2][2] * matrix_h[2][3] + matrix_g[2][3] * matrix_h[3][3] + matrix_h[2][4] * matrix_h[4][3]
        matrix_z[2][4] = matrix_g[2][0] * matrix_h[0][4] + matrix_h[2][1] * matrix_h[1][4] + matrix_g[2][2] * matrix_h[2][4] + matrix_g[2][3] * matrix_h[3][4] + matrix_h[2][4] * matrix_h[4][4]

        matrix_yz[2][0] = matrix_y[2][0] * matrix_z[0][0] + matrix_y[2][1] * matrix_z[1][0] + matrix_y[2][2] * matrix_z[2][0] + matrix_y[2][3] * matrix_z[3][0] + matrix_y[2][4] * matrix_z[4][0]
        matrix_yz[2][1] = matrix_y[2][0] * matrix_z[0][1] + matrix_y[2][1] * matrix_z[1][1] + matrix_y[2][2] * matrix_z[2][1] + matrix_y[2][3] * matrix_z[3][1] + matrix_y[2][4] * matrix_z[4][1]
        matrix_yz[2][2] = matrix_y[2][0] * matrix_z[0][2] + matrix_y[2][1] * matrix_z[1][2] + matrix_y[2][2] * matrix_z[2][2] + matrix_y[2][3] * matrix_z[3][2] + matrix_y[2][4] * matrix_z[4][2]
        matrix_yz[2][3] = matrix_y[2][0] * matrix_z[0][3] + matrix_y[2][1] * matrix_z[1][3] + matrix_y[2][2] * matrix_z[2][3] + matrix_y[2][3] * matrix_z[3][3] + matrix_y[2][4] * matrix_z[4][3]
        matrix_yz[2][4] = matrix_y[2][0] * matrix_z[0][4] + matrix_y[2][1] * matrix_z[1][4] + matrix_y[2][2] * matrix_z[2][4] + matrix_y[2][3] * matrix_z[3][4] + matrix_y[2][4] * matrix_z[4][4]

        matrix_semua[2][0] = matrix_wx[2][0] * matrix_yz[0][0] + matrix_wx[2][1] * matrix_yz[1][0] + matrix_wx[2][2] * matrix_yz[2][0] + matrix_wx[2][3] * matrix_yz[3][0] + matrix_wx[2][4] * matrix_yz[4][0]
        matrix_semua[2][1] = matrix_wx[2][0] * matrix_yz[0][1] + matrix_wx[2][1] * matrix_yz[1][1] + matrix_wx[2][2] * matrix_yz[2][1] + matrix_wx[2][3] * matrix_yz[3][1] + matrix_wx[2][4] * matrix_yz[4][1]
        matrix_semua[2][2] = matrix_wx[2][0] * matrix_yz[0][2] + matrix_wx[2][1] * matrix_yz[1][2] + matrix_wx[2][2] * matrix_yz[2][2] + matrix_wx[2][3] * matrix_yz[3][2] + matrix_wx[2][4] * matrix_yz[4][2]
        matrix_semua[2][3] = matrix_wx[2][0] * matrix_yz[0][3] + matrix_wx[2][1] * matrix_yz[1][3] + matrix_wx[2][2] * matrix_yz[2][3] + matrix_wx[2][3] * matrix_yz[3][3] + matrix_wx[2][4] * matrix_yz[4][3]
        matrix_semua[2][4] = matrix_wx[2][0] * matrix_yz[0][4] + matrix_wx[2][1] * matrix_yz[1][4] + matrix_wx[2][2] * matrix_yz[2][4] + matrix_wx[2][3] * matrix_yz[3][4] + matrix_wx[2][4] * matrix_yz[4][4]

        print ("End " + self.name + "\n")

class Thread4(threading.Thread):        #3|0, 0, 0, 0, 0|
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        print ("Starting " + self.name + "\n")

        matrix_w[3][0] = matrix_a[3][0] * matrix_b[0][0] + matrix_a[3][1] * matrix_b[1][0] + matrix_a[3][2] * matrix_b[2][0] + matrix_a[3][3] * matrix_b[3][0] + matrix_a[3][4] * matrix_b[4][0]
        matrix_w[3][1] = matrix_a[3][0] * matrix_b[0][1] + matrix_a[3][1] * matrix_b[1][1] + matrix_a[3][2] * matrix_b[2][1] + matrix_a[3][3] * matrix_b[3][1] + matrix_a[3][4] * matrix_b[4][1]
        matrix_w[3][2] = matrix_a[3][0] * matrix_b[0][2] + matrix_a[3][1] * matrix_b[1][2] + matrix_a[3][2] * matrix_b[2][2] + matrix_a[3][3] * matrix_b[3][2] + matrix_a[3][4] * matrix_b[4][2]
        matrix_w[3][3] = matrix_a[3][0] * matrix_b[0][3] + matrix_a[3][1] * matrix_b[1][3] + matrix_a[3][2] * matrix_b[2][3] + matrix_a[3][3] * matrix_b[3][3] + matrix_a[3][4] * matrix_b[4][3]
        matrix_w[3][4] = matrix_a[3][0] * matrix_b[0][4] + matrix_a[3][1] * matrix_b[1][4] + matrix_a[3][2] * matrix_b[2][4] + matrix_a[3][3] * matrix_b[3][4] + matrix_a[3][4] * matrix_b[4][4]

        matrix_x[3][0] = matrix_c[3][0] * matrix_d[0][0] + matrix_c[3][1] * matrix_d[1][0] + matrix_c[3][2] * matrix_d[2][0] + matrix_c[3][3] * matrix_d[3][0] + matrix_c[3][4] * matrix_d[4][0]
        matrix_x[3][1] = matrix_c[3][0] * matrix_d[0][1] + matrix_c[3][1] * matrix_d[1][1] + matrix_c[3][2] * matrix_d[2][1] + matrix_c[3][3] * matrix_d[3][1] + matrix_c[3][4] * matrix_d[4][1]
        matrix_x[3][2] = matrix_c[3][0] * matrix_d[0][2] + matrix_c[3][1] * matrix_d[1][2] + matrix_c[3][2] * matrix_d[2][2] + matrix_c[3][3] * matrix_d[3][2] + matrix_c[3][4] * matrix_d[4][2]
        matrix_x[3][3] = matrix_c[3][0] * matrix_d[0][3] + matrix_c[3][1] * matrix_d[1][3] + matrix_c[3][2] * matrix_d[2][3] + matrix_c[3][3] * matrix_d[3][3] + matrix_c[3][4] * matrix_d[4][3]
        matrix_x[3][4] = matrix_c[3][0] * matrix_d[0][4] + matrix_c[3][1] * matrix_d[1][4] + matrix_c[3][2] * matrix_d[2][4] + matrix_c[3][3] * matrix_d[3][4] + matrix_c[3][4] * matrix_d[4][4]

        
        matrix_wx[3][0] = matrix_w[3][0] * matrix_x[0][0] + matrix_w[3][1] * matrix_x[1][0] + matrix_w[3][2] * matrix_x[2][0] + matrix_w[3][3] * matrix_x[3][0] + matrix_w[3][4] * matrix_x[4][0]
        matrix_wx[3][1] = matrix_w[3][0] * matrix_x[0][1] + matrix_w[3][1] * matrix_x[1][1] + matrix_w[3][2] * matrix_x[2][1] + matrix_w[3][3] * matrix_x[3][1] + matrix_w[3][4] * matrix_x[4][1]
        matrix_wx[3][2] = matrix_w[3][0] * matrix_x[0][2] + matrix_w[3][1] * matrix_x[1][2] + matrix_w[3][2] * matrix_x[2][2] + matrix_w[3][3] * matrix_x[3][2] + matrix_w[3][4] * matrix_x[4][2]
        matrix_wx[3][3] = matrix_w[3][0] * matrix_x[0][3] + matrix_w[3][1] * matrix_x[1][3] + matrix_w[3][2] * matrix_x[2][3] + matrix_w[3][3] * matrix_x[3][3] + matrix_w[3][4] * matrix_x[4][3]
        matrix_wx[3][4] = matrix_w[3][0] * matrix_x[0][4] + matrix_w[3][1] * matrix_x[1][4] + matrix_w[3][2] * matrix_x[2][4] + matrix_w[3][3] * matrix_x[3][4] + matrix_w[3][4] * matrix_x[4][4]

        matrix_y[3][0] = matrix_e[3][0] * matrix_f[0][0] + matrix_e[3][1] * matrix_f[1][0] + matrix_e[3][2] * matrix_f[2][0] + matrix_e[3][3] * matrix_f[3][0] + matrix_e[3][4] * matrix_f[4][0]
        matrix_y[3][1] = matrix_e[3][0] * matrix_f[0][1] + matrix_e[3][1] * matrix_f[1][1] + matrix_e[3][2] * matrix_f[2][1] + matrix_e[3][3] * matrix_f[3][1] + matrix_e[3][4] * matrix_f[4][1]
        matrix_y[3][2] = matrix_e[3][0] * matrix_f[0][2] + matrix_e[3][1] * matrix_f[1][2] + matrix_e[3][2] * matrix_f[2][2] + matrix_e[3][3] * matrix_f[3][2] + matrix_e[3][4] * matrix_f[4][2]
        matrix_y[3][3] = matrix_e[3][0] * matrix_f[0][3] + matrix_e[3][1] * matrix_f[1][3] + matrix_e[3][2] * matrix_f[2][3] + matrix_e[3][3] * matrix_f[3][3] + matrix_e[3][4] * matrix_f[4][3]
        matrix_y[3][4] = matrix_e[3][0] * matrix_f[0][4] + matrix_e[3][1] * matrix_f[1][4] + matrix_e[3][2] * matrix_f[2][4] + matrix_e[3][3] * matrix_f[3][4] + matrix_e[3][4] * matrix_f[4][4]

        matrix_z[3][0] = matrix_g[3][0] * matrix_h[0][0] + matrix_h[3][1] * matrix_h[1][0] + matrix_g[3][2] * matrix_h[2][0] + matrix_g[3][3] * matrix_h[3][0] + matrix_h[3][4] * matrix_h[4][0]
        matrix_z[3][1] = matrix_g[3][0] * matrix_h[0][1] + matrix_h[3][1] * matrix_h[1][1] + matrix_g[3][2] * matrix_h[2][1] + matrix_g[3][3] * matrix_h[3][1] + matrix_h[3][4] * matrix_h[4][1]
        matrix_z[3][2] = matrix_g[3][0] * matrix_h[0][2] + matrix_h[3][1] * matrix_h[1][2] + matrix_g[3][2] * matrix_h[2][2] + matrix_g[3][3] * matrix_h[3][2] + matrix_h[3][4] * matrix_h[4][2]
        matrix_z[3][3] = matrix_g[3][0] * matrix_h[0][3] + matrix_h[3][1] * matrix_h[1][3] + matrix_g[3][2] * matrix_h[2][3] + matrix_g[3][3] * matrix_h[3][3] + matrix_h[3][4] * matrix_h[4][3]
        matrix_z[3][4] = matrix_g[3][0] * matrix_h[0][4] + matrix_h[3][1] * matrix_h[1][4] + matrix_g[3][2] * matrix_h[2][4] + matrix_g[3][3] * matrix_h[3][4] + matrix_h[3][4] * matrix_h[4][4]

        matrix_yz[3][0] = matrix_y[3][0] * matrix_z[0][0] + matrix_y[3][1] * matrix_z[1][0] + matrix_y[3][2] * matrix_z[2][0] + matrix_y[3][3] * matrix_z[3][0] + matrix_y[3][4] * matrix_z[4][0]
        matrix_yz[3][1] = matrix_y[3][0] * matrix_z[0][1] + matrix_y[3][1] * matrix_z[1][1] + matrix_y[3][2] * matrix_z[2][1] + matrix_y[3][3] * matrix_z[3][1] + matrix_y[3][4] * matrix_z[4][1]
        matrix_yz[3][2] = matrix_y[3][0] * matrix_z[0][2] + matrix_y[3][1] * matrix_z[1][2] + matrix_y[3][2] * matrix_z[2][2] + matrix_y[3][3] * matrix_z[3][2] + matrix_y[3][4] * matrix_z[4][2]
        matrix_yz[3][3] = matrix_y[3][0] * matrix_z[0][3] + matrix_y[3][1] * matrix_z[1][3] + matrix_y[3][2] * matrix_z[2][3] + matrix_y[3][3] * matrix_z[3][3] + matrix_y[3][4] * matrix_z[4][3]
        matrix_yz[3][4] = matrix_y[3][0] * matrix_z[0][4] + matrix_y[3][1] * matrix_z[1][4] + matrix_y[3][2] * matrix_z[2][4] + matrix_y[3][3] * matrix_z[3][4] + matrix_y[3][4] * matrix_z[4][4]

        matrix_semua[3][0] = matrix_wx[3][0] * matrix_yz[0][0] + matrix_wx[3][1] * matrix_yz[1][0] + matrix_wx[3][2] * matrix_yz[2][0] + matrix_wx[3][3] * matrix_yz[3][0] + matrix_wx[3][4] * matrix_yz[4][0]
        matrix_semua[3][1] = matrix_wx[3][0] * matrix_yz[0][1] + matrix_wx[3][1] * matrix_yz[1][1] + matrix_wx[3][2] * matrix_yz[2][1] + matrix_wx[3][3] * matrix_yz[3][1] + matrix_wx[3][4] * matrix_yz[4][1]
        matrix_semua[3][2] = matrix_wx[3][0] * matrix_yz[0][2] + matrix_wx[3][1] * matrix_yz[1][2] + matrix_wx[3][2] * matrix_yz[2][2] + matrix_wx[3][3] * matrix_yz[3][2] + matrix_wx[3][4] * matrix_yz[4][2]
        matrix_semua[3][3] = matrix_wx[3][0] * matrix_yz[0][3] + matrix_wx[3][1] * matrix_yz[1][3] + matrix_wx[3][2] * matrix_yz[2][3] + matrix_wx[3][3] * matrix_yz[3][3] + matrix_wx[3][4] * matrix_yz[4][3]
        matrix_semua[3][4] = matrix_wx[3][0] * matrix_yz[0][4] + matrix_wx[3][1] * matrix_yz[1][4] + matrix_wx[3][2] * matrix_yz[2][4] + matrix_wx[3][3] * matrix_yz[3][4] + matrix_wx[3][4] * matrix_z[4][4]



        print ("End " + self.name + "\n")

class Thread5(threading.Thread):        #4|0, 0, 0, 0, 0|
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        print ("Starting " + self.name + "\n")

        matrix_w[4][0] = matrix_a[4][0] * matrix_b[0][0] + matrix_a[4][1] * matrix_b[1][0] + matrix_a[4][2] * matrix_b[2][0] + matrix_a[4][3] * matrix_b[3][0] + matrix_a[4][4] * matrix_b[4][0]
        matrix_w[4][1] = matrix_a[4][0] * matrix_b[0][1] + matrix_a[4][1] * matrix_b[1][1] + matrix_a[4][2] * matrix_b[2][1] + matrix_a[4][3] * matrix_b[3][1] + matrix_a[4][4] * matrix_b[4][1]
        matrix_w[4][2] = matrix_a[4][0] * matrix_b[0][2] + matrix_a[4][1] * matrix_b[1][2] + matrix_a[4][2] * matrix_b[2][2] + matrix_a[4][3] * matrix_b[3][2] + matrix_a[4][4] * matrix_b[4][2]
        matrix_w[4][3] = matrix_a[4][0] * matrix_b[0][3] + matrix_a[4][1] * matrix_b[1][3] + matrix_a[4][2] * matrix_b[2][3] + matrix_a[4][3] * matrix_b[3][3] + matrix_a[4][4] * matrix_b[4][3]
        matrix_w[4][4] = matrix_a[4][0] * matrix_b[0][4] + matrix_a[4][1] * matrix_b[1][4] + matrix_a[4][2] * matrix_b[2][4] + matrix_a[4][3] * matrix_b[3][4] + matrix_a[4][4] * matrix_b[4][4]

        matrix_x[4][0] = matrix_c[4][0] * matrix_d[0][0] + matrix_c[4][1] * matrix_d[1][0] + matrix_c[4][2] * matrix_d[2][0] + matrix_c[4][3] * matrix_d[3][0] + matrix_c[4][4] * matrix_d[4][0]
        matrix_x[4][1] = matrix_c[4][0] * matrix_d[0][1] + matrix_c[4][1] * matrix_d[1][1] + matrix_c[4][2] * matrix_d[2][1] + matrix_c[4][3] * matrix_d[3][1] + matrix_c[4][4] * matrix_d[4][1]
        matrix_x[4][2] = matrix_c[4][0] * matrix_d[0][2] + matrix_c[4][1] * matrix_d[1][2] + matrix_c[4][2] * matrix_d[2][2] + matrix_c[4][3] * matrix_d[3][2] + matrix_c[4][4] * matrix_d[4][2]
        matrix_x[4][3] = matrix_c[4][0] * matrix_d[0][3] + matrix_c[4][1] * matrix_d[1][3] + matrix_c[4][2] * matrix_d[2][3] + matrix_c[4][3] * matrix_d[3][3] + matrix_c[4][4] * matrix_d[4][3]
        matrix_x[4][4] = matrix_c[4][0] * matrix_d[0][4] + matrix_c[4][1] * matrix_d[1][4] + matrix_c[4][2] * matrix_d[2][4] + matrix_c[4][3] * matrix_d[3][4] + matrix_c[4][4] * matrix_d[4][4]

        matrix_wx[4][0] = matrix_w[4][0] * matrix_x[0][0] + matrix_w[4][1] * matrix_x[1][0] + matrix_w[4][2] * matrix_x[2][0] + matrix_w[4][3] * matrix_x[3][0] + matrix_w[4][4] * matrix_x[4][0]
        matrix_wx[4][1] = matrix_w[4][0] * matrix_x[0][1] + matrix_w[4][1] * matrix_x[1][1] + matrix_w[4][2] * matrix_x[2][1] + matrix_w[4][3] * matrix_x[3][1] + matrix_w[4][4] * matrix_x[4][1]
        matrix_wx[4][2] = matrix_w[4][0] * matrix_x[0][2] + matrix_w[4][1] * matrix_x[1][2] + matrix_w[4][2] * matrix_x[2][2] + matrix_w[4][3] * matrix_x[3][2] + matrix_w[4][4] * matrix_x[4][2]
        matrix_wx[4][3] = matrix_w[4][0] * matrix_x[0][3] + matrix_w[4][1] * matrix_x[1][3] + matrix_w[4][2] * matrix_x[2][3] + matrix_w[4][3] * matrix_x[3][3] + matrix_w[4][4] * matrix_x[4][3]
        matrix_wx[4][4] = matrix_w[4][0] * matrix_x[0][4] + matrix_w[4][1] * matrix_x[1][4] + matrix_w[4][2] * matrix_x[2][4] + matrix_w[4][3] * matrix_x[3][4] + matrix_w[4][4] * matrix_x[4][4]

        matrix_y[4][0] = matrix_e[4][0] * matrix_f[0][0] + matrix_e[4][1] * matrix_f[1][0] + matrix_e[4][2] * matrix_f[2][0] + matrix_e[4][3] * matrix_f[3][0] + matrix_e[4][4] * matrix_f[4][0]
        matrix_y[4][1] = matrix_e[4][0] * matrix_f[0][1] + matrix_e[4][1] * matrix_f[1][1] + matrix_e[4][2] * matrix_f[2][1] + matrix_e[4][3] * matrix_f[3][1] + matrix_e[4][4] * matrix_f[4][1]
        matrix_y[4][2] = matrix_e[4][0] * matrix_f[0][2] + matrix_e[4][1] * matrix_f[1][2] + matrix_e[4][2] * matrix_f[2][2] + matrix_e[4][3] * matrix_f[3][2] + matrix_e[4][4] * matrix_f[4][2]
        matrix_y[4][3] = matrix_e[4][0] * matrix_f[0][3] + matrix_e[4][1] * matrix_f[1][3] + matrix_e[4][2] * matrix_f[2][3] + matrix_e[4][3] * matrix_f[3][3] + matrix_e[4][4] * matrix_f[4][3]
        matrix_y[4][4] = matrix_e[4][0] * matrix_f[0][4] + matrix_e[4][1] * matrix_f[1][4] + matrix_e[4][2] * matrix_f[2][4] + matrix_e[4][3] * matrix_f[3][4] + matrix_e[4][4] * matrix_f[4][4]

        matrix_z[4][0] = matrix_g[4][0] * matrix_h[0][0] + matrix_h[4][1] * matrix_h[1][0] + matrix_g[4][2] * matrix_h[2][0] + matrix_g[4][3] * matrix_h[3][0] + matrix_h[4][4] * matrix_h[4][0]
        matrix_z[4][1] = matrix_g[4][0] * matrix_h[0][1] + matrix_h[4][1] * matrix_h[1][1] + matrix_g[4][2] * matrix_h[2][1] + matrix_g[4][3] * matrix_h[3][1] + matrix_h[4][4] * matrix_h[4][1]
        matrix_z[4][2] = matrix_g[4][0] * matrix_h[0][2] + matrix_h[4][1] * matrix_h[1][2] + matrix_g[4][2] * matrix_h[2][2] + matrix_g[4][3] * matrix_h[3][2] + matrix_h[4][4] * matrix_h[4][2]
        matrix_z[4][3] = matrix_g[4][0] * matrix_h[0][3] + matrix_h[4][1] * matrix_h[1][3] + matrix_g[4][2] * matrix_h[2][3] + matrix_g[4][3] * matrix_h[3][3] + matrix_h[4][4] * matrix_h[4][3]
        matrix_z[4][4] = matrix_g[4][0] * matrix_h[0][4] + matrix_h[4][1] * matrix_h[1][4] + matrix_g[4][2] * matrix_h[2][4] + matrix_g[4][3] * matrix_h[3][4] + matrix_h[4][4] * matrix_h[4][4]

        matrix_yz[4][0] = matrix_y[4][0] * matrix_z[0][0] + matrix_y[4][1] * matrix_z[1][0] + matrix_y[4][2] * matrix_z[2][0] + matrix_y[4][3] * matrix_z[3][0] + matrix_y[4][4] * matrix_z[4][0]
        matrix_yz[4][1] = matrix_y[4][0] * matrix_z[0][1] + matrix_y[4][1] * matrix_z[1][1] + matrix_y[4][2] * matrix_z[2][1] + matrix_y[4][3] * matrix_z[3][1] + matrix_y[4][4] * matrix_z[4][1]
        matrix_yz[4][2] = matrix_y[4][0] * matrix_z[0][2] + matrix_y[4][1] * matrix_z[1][2] + matrix_y[4][2] * matrix_z[2][2] + matrix_y[4][3] * matrix_z[3][2] + matrix_y[4][4] * matrix_z[4][2]
        matrix_yz[4][3] = matrix_y[4][0] * matrix_z[0][3] + matrix_y[4][1] * matrix_z[1][3] + matrix_y[4][2] * matrix_z[2][3] + matrix_y[4][3] * matrix_z[3][3] + matrix_y[4][4] * matrix_z[4][3]
        matrix_yz[4][4] = matrix_y[4][0] * matrix_z[0][4] + matrix_y[4][1] * matrix_z[1][4] + matrix_y[4][2] * matrix_z[2][4] + matrix_y[4][3] * matrix_z[3][4] + matrix_y[4][4] * matrix_z[4][4]

        
        matrix_semua[4][0] = matrix_wx[4][0] * matrix_yz[0][0] + matrix_wx[4][1] * matrix_yz[1][0] + matrix_wx[4][2] * matrix_yz[2][0] + matrix_wx[4][3] * matrix_yz[3][0] + matrix_wx[4][4] * matrix_yz[4][0]
        matrix_semua[4][1] = matrix_wx[4][0] * matrix_yz[0][1] + matrix_wx[4][1] * matrix_yz[1][1] + matrix_wx[4][2] * matrix_yz[2][1] + matrix_wx[4][3] * matrix_yz[3][1] + matrix_wx[4][4] * matrix_yz[4][1]
        matrix_semua[4][2] = matrix_wx[4][0] * matrix_yz[0][2] + matrix_wx[4][1] * matrix_yz[1][2] + matrix_wx[4][2] * matrix_yz[2][2] + matrix_wx[4][3] * matrix_yz[3][2] + matrix_wx[4][4] * matrix_yz[4][2]
        matrix_semua[4][3] = matrix_wx[4][0] * matrix_yz[0][3] + matrix_wx[4][1] * matrix_yz[1][3] + matrix_wx[4][2] * matrix_yz[2][3] + matrix_wx[4][3] * matrix_yz[3][3] + matrix_wx[4][4] * matrix_yz[4][3]
        matrix_semua[4][4] = matrix_wx[4][0] * matrix_yz[0][4] + matrix_wx[4][1] * matrix_yz[1][4] + matrix_wx[4][2] * matrix_yz[2][4] + matrix_wx[4][3] * matrix_yz[3][4] + matrix_wx[4][4] * matrix_yz[4][4]



        print ("End " + self.name + "\n")

start = int(round(time.time_ns())) #start perhitungan waktu eksekusi program hingga selesai

thread1 = Thread1(1, "Thread 1")
thread2 = Thread2(2, "Thread 2")
thread3 = Thread3(3, "Thread 3")
thread4 = Thread4(4, "Thread 4")
thread5 = Thread5(5, "Thread 5")


#untuk hasil serial parallel silahkan comment atau uncomment salah satu dari dibawah ini

'''#serial exec
thread1.start()
thread1.join()
thread2.start()
thread2.join()
thread3.start()
thread3.join()
thread4.start()
thread4.join()
thread5.start()
thread5.join()'''

#parallel exec
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()

print("Waktu Eksekusi: ", (int(round(time.time_ns())) - start)," nanosecond") #print hasil waktu eksekusi saat selesai

print(*matrix_semua, sep='\n') #separator print hasil array