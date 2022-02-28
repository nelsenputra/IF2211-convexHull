# myConvexHull.py
# Source code program yang berisi implementasi fungsi utama myConvexHull

# IMPORT LIBRARY AND FUNCTION
import numpy as np
from function import *


'''
/* *** myConvexHull *** */
** Mengembalikan semua titik-titik yang merupakan titik terluar dari convex hull
** param: bucket (array of titik convex hull yang diuji)
** return: kumpulan titik terluar dar convex hull
'''
def myConvexHull(bucket):
    # Membagi kumpulan titik menjadi 2 bagian, yakni titik bagian kiri dan titik bagian kanan
    leftBucket = []
    rightBucket = []

    # Mendaftarkan titik-titik pada array bucket
    bucketTrue = np.array(bucket).astype(float)

    # Mencari titik p1 dan pn yang merupakan titik terluar pada bucket
    p1, pn = extremeIndex(bucketTrue)

    # Pengecekan posisi seluruh titik
    for i in range(len(bucketTrue)):
        if ((pointPosition(p1, pn, i, bucketTrue) > 0) and (i != p1) and (i != pn)):
            leftBucket.append(i)
        elif ((pointPosition(p1, pn, i, bucketTrue) < 0) and (i != p1) and (i != pn)):
            rightBucket.append(i)

    # Memanggil fungsi rekursif untuk mendapatkan titik-titik yang sesuai
    left = recursiveFunction(p1, pn, bucketTrue, leftBucket)
    right = recursiveFunction(pn, p1, bucketTrue, rightBucket)

    # Mengembalikan hasil kombinasi dari partisi yang sudah dilakukan sebelumnya berupa array dari bucket yang bernilai true
    return left + right