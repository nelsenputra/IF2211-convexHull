# function.py
# Source code program yang berisi fungsi-fungsi dasar pembentuk fungsi myConvexHull

# IMPORT LIBRARY
import numpy as np


'''
/* *** DETERMINAN *** */
** Mengembalikan determinan dari kumpulan tiga titik yang berada dalam array bucket
** param: p1, pn, check (titik-titik yang akan dicari determinannya)
** param: bucket (array tempat titik berada)
** return: det (determinan dari ketiga titik)
'''
def determinan(p1, pn, check, bucket):
    # Inisialisasi semua elemen dari titik-titiknya
    x1 = bucket[p1][0]
    y1 = bucket[p1][1]
    x2 = bucket[pn][0]
    y2 = bucket[pn][1]
    x3 = bucket[check][0]
    y3 = bucket[check][1]

    # Menghitung determinan
    det = (x1 * y2) + (x3 * y1) + (x2 * y3) - (x3 * y2) - (x2 * y1) - (x1 * y3)
    return det


'''
/* *** POINT POSITION *** */
** Mengecek posisi titik, yakni berada di kiri/atas atau kanan/bawah dari garis yang merupakan perpanjangan dari titik p1 dan pn
** param: p1, pn (titik-titik terluar dari kumpulan titik yang kemudian membentuk garis)
** param: check (titik yang diperiksa)
** param: bucket (array tempat titik berada)
** return: determinan dari ketiga titik yang kemudian digunakan untuk menentukan posisi titik
'''
def pointPosition(p1, pn, check, bucket):
    # Jika determinan > 0 (positif), titik berada di sebelah kiri/atas garis
    # Jika determinan <= 0 (negatif), titik berada di sebelah kanan/bawah garis
    return determinan(p1, pn, check, bucket)


'''
/* *** EXTREME INDEX *** */
** Mengembalikan indeks dari titik koordinat pada bucket yang memiliki nilai x minimum atau maksimum
** param: bucket (array tempat titik berada)
** return: indeks minimum dan maksimum dari titik pada bucket
'''
def extremeIndex(bucket):
    # Inisialisasi nilai x
    valueOfX = []

    # Menambahkan semua elemen bucket ke dalam nilai x
    for i in range(len(bucket)):
        valueOfX.append(bucket[i][0])
    maxOfX = max(valueOfX)
    minOfX = min(valueOfX)

    # Pengecekan untuk indeks maksimum
    found = True
    indexMaxOfBucket = 0
    while ((indexMaxOfBucket < len(bucket)) and (found)):
        if (bucket[indexMaxOfBucket][0] == maxOfX):
            found = False
        else:
            indexMaxOfBucket += 1

    # Pengecekan untuk indeks minimum
    found = True
    indexMinOfBucket = 0 
    while ((indexMinOfBucket < len(bucket)) and (found)):
        if (bucket[indexMinOfBucket][0] == minOfX):
            found = False
        else:
             indexMinOfBucket += 1

    # Mengembalikan indeks minimum dan indeks maksimum dari titik pada bucket
    return (indexMinOfBucket, indexMaxOfBucket)


'''
/* *** TRIANGLE PARTITION *** */
** Mengembalikan besar sudur apit dari partisi segitiga
** param: p1, p3 (titik-titik terluar dari kumpulan titik yang kemudian membentuk garis))
** param: p2 (titik periksa)
** return: degree (sudut apit dari partisi segitiga)
'''
def trianglePartition(p1, p2, p3):
    # Menghitung jarak antara titik p1-p2 dan p3-p2
    distance12 = p1 - p2 
    distance32 = p3 - p2 
    # Menghitung dot product antara vektor distance12 dan distance32
    product1 = np.dot(distance12, distance32)
    # Menghitung vektor normal dari distance12 dan distance32
    product2 = np.linalg.norm(distance12) * np.linalg.norm(distance32)

    # Menghitung besar sudut p2 (sudut apit dari partisi segitiga)
    cosinusValue = product1 / product2
    degree = np.degrees(np.arccos(cosinusValue))
    return degree


'''
/* *** RECURSIVE FUNCTION *** */
** Fungsi yang akan digunakan secara rekursif pada fungsi myConvexHull
** param: p1, pn (titik-titik terluar dari kumpulan titik yang kemudian membentuk garis)
** param: bucketTrue (array yang berisi titik-titik pada convex hull)
** param: bucket (array yang berisi semua titik)
** return: array pada bucket yang bernilai true
'''
def recursiveFunction(p1, pn, bucketTrue, bucket):
    # Kondisi banyak titik pada bucket != 0
    if (len(bucket) != 0):
        # Inisialisasi array kosong
        temp = []

        # Pengecekan semua titik pada bucket
        for i in range(len(bucket)):
            if ((p1 != pn) and (p1 != bucket[i]) and (pn != bucket[i])):
                degreeOfTemp = trianglePartition(bucketTrue[pn], bucketTrue[p1], bucketTrue[bucket[i]])
            else:
                degreeOfTemp = 0
            # Menambahkan sudut temp ke array temp
            temp.append(degreeOfTemp)
        # Inisialisasi titik px dengan bucket pada index ke max dari array temp
        px = bucket[temp.index(max(temp))]

        # DIVIDE AND CONQUER SECARA REKURSIF
        # Inisialisasi array yang berisi titik pada garis Px-Pn
        pointOfPxPn = []
        # Pengecekan
        for i in range(len(bucket)):
            if ((pointPosition(px, pn, bucket[i],bucketTrue) > 0) and (bucket[i] != p1) and (bucket[i] != pn)):
                pointOfPxPn.append(bucket[i])

        # Inisialisasi array yang berisi titik pada garis P1-Px
        pointOfP1Px = []
        # Pengecekan
        for i in range(len(bucket)):
            if ((pointPosition(p1, px, bucket[i], bucketTrue) > 0) and (bucket[i] != p1) and (bucket[i] != pn)):
                pointOfP1Px.append(bucket[i])

        # Pemanggilan fungsi rekursif kembali
        left = recursiveFunction(p1, px, bucketTrue, pointOfP1Px)
        right = recursiveFunction(px, pn, bucketTrue, pointOfPxPn)

        # Mengembalikan hasil kombinasi dari partisi yang sudah dilakukan sebelumnya berupa array dari bucket yang bernilai true
        return left + right
    
    # Kondisi banyak titik pada bucket = 0
    else:
        # Pengecekan apakah p1 dan pn merupakan titik yang berbeda agar dapat membentuk garis
        if (p1 != pn):                        
            return [[p1, pn]]
        else:
            return []