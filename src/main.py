# main.py
# Source code program utama 

# IMPORT LIBRARY DAN MYCONVEXHULL
import pandas as pd
import matplotlib.pyplot as plt
import random
from scipy.spatial import ConvexHull
from myConvexHull import myConvexHull

def header():
    print("[]=========================================================================================[]")
    print("||    _ _              _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _       _ _ _ _ _ _ _ _ _   ||")
    print("||   /   |            |   \     __ _|   |    _ _ _ _|     \     \     /     |     __ _ _|  ||")
    print("||  /   /     _ __     \   \   /_ __    |   |  /   _ _ _   \     \_ _/      |    /_ _ __   ||")
    print("||  \   \    /    \    /   /        |   |   | /   /     \   \               |           |  ||")
    print("||   \   \  /  /\  \  /   /   _ _ __|   |   | \   \_ _ _/   / |\       /|   |    _ _ _ _|  ||")
    print("||    \   \/  /__\  \/   /    \_ _ _    |_ _|_ \_ __       /  | \_ _ _/ |   |    \_ _ __   ||")
    print("||     \_ _ _ _ _ _ _ __/_ _ _ _ _ _|_ _ _ _ _|_ _ _|_ _ _/_ _|         |_ _|__ _ _ _ _ |  ||")
    print("||                                 _ _ _ _ _ ___ _ _ _ _                                   ||")
    print("||                                |_ __    _ __|        \                                  ||")
    print("||                                     |  |  /    _ _    \                                 ||")
    print("||                                     |  | /    /   \    \                                ||")
    print("||                                     |  | \    \_ _/    /                                ||")
    print("||                                     |  |  \           /                                 ||")
    print("||                                     |__|   \ _ _ _ __/                                  ||")
    print("||   _ _ _ _ _ _ _ _ _ _ _      _ _ _           _ _ _ _ _ _ _        _ _ _                 ||")
    print("||  |    _ _ _|      \    \    |   |  \        /    /  _ _ _ |\     /    /                 ||")
    print("||  |   |   /   _ _   \    \   |   |   \      /    /  /_ _\__  \_ _/    /                  ||")
    print("||  |   |  /   /   \   \    \  |   |    \    /    /          |  _ _    /                   ||")
    print("||  |   |  \   \_ _/   /     \ |   |\    \_ /    /     _ _ __| /   \   \                   ||")
    print("||  |   |_ _\_        /       \|   | \          /     \_ _/__ /     \   \                  ||")
    print("||  |_ _ _ _ _|_ _ _ /|_ _|\_ _ _ _|  \_ _ _ __/_ _ _ _ _ _ _|_ _    \_ _\_ _ _ _ _        ||")
    print("||                                              _ __      _ _ _ _       _ _ _ _ _ _        ||")
    print("||                                             |    |    |   |   |     |   |   |   |       ||")
    print("||                                             |    |    |   |   |     |   |   |   |       ||")
    print("||                                             |    |_ __|   |   |     |   |   |   |       ||")
    print("||                                             |     _ __    |   |     |   |   |   |       ||")
    print("||                                             |    |    |   |   |_ _ _|   |   |   |       ||")
    print("||                                             |    |    |   |             |   |_ _|_ _ _  ||")
    print("||                                             |_ __|    |_ _|_ _ _ _ _ _ _|_ _ _ _ _|_ _| ||")
    print("||                _ _ __ __ _ _ _ _ _ __ _ _         _ _ _ _ _ __ _ _ _ _ _                ||")
    print("||               /    _ _ _|       \    |   \       /    /  _ _ _|   _ _   |               ||")
    print("||              /    /   /    _ _   \   |    \     /    /  /_ _ _   |_ _|  |               ||")
    print("||              \    \  /    /   \   \  |\    \   /    /         |        /                ||")
    print("||               \    \ \    \_ _/   /  | \    \_/    /    _ _ __|   |\   \                ||")
    print("||            __ _\    \ \          /   |_ \_ __     /     \_ _ _    | \   \               ||")
    print("||           |_ _ _ _ _/  \_ _ _ _ /_ _ _ _ _ _|_ _ /_ _ _ _ _ _ |_ _|  \_ _\              ||")
    print("||                                                                                         ||")
    print("[]=========================================================================================[]")
    print("[]=============================Created by Nelsen Putra 13520130============================[]")

def logo():
    print("""\033[36m\n\n
                          (####)
                        (#######)
                      (#########)
                     (#########)
                    (#########)
                   (#########)
   __&__          (#########)
  /     \        (#########)   |\/\/\/|     /\ /\  /\               /\
 |       |      (#########)    |      |     | V  \/  \---.    .----/  \----.
 |  (o)(o)       (o)(o)(##)    |      |      \_        /       \          /
 C   .---_)    ,_C     (##)    | (o)(o)       (o)(o)  <__.   .--\ (o)(o) /__.
  | |.___|    /___,   (##)     C      _)     _C         /     \     ()     /
  |  \__/       \     (#)       | ,___|     /____,   )  \      >   (C_)   <
  /_____\        |    |         |   /         \     /----'    /___\____/___\
 /_____/ \       OOOOOO        /____\          ooooo             /|    |\
/         \     /      \      /      \        /     \           /        \
    \n\n\033[0m""")

def welcome():
    print("""\033[31m \nOnce again, welcome to CONVEX HULL SOLVER by Nelsen \033[0m""")
    print("""\033[32m This program was created by Nelsen Putra 13520130 to fulfill the second small project of IF2211 Algorithm Strategies. \033[0m""")

def menu():
    print("""\033[33m Main Menu: \n\033[0m""")
    print("""\033[37m
    1. Start CONVEX HULL!
    2. Exit Program\n\033[0m""")
    choice1 = int(input("""\033[36m Enter menu: \033[0m """))
    if (choice1 == 1):
        print("These is the list of datasets that exist in this program:")
        print("""\033[37m
        1. Dataset iris
        2. Dataset digits
        3. Dataset wine
        4. Dataset breast_cancer\n\033[0m""")
        choice2 = int(input("""\033[36m Enter dataset: \033[0m """))
        if (choice2 == 1):
            iris()
        elif (choice2 == 2):
            digits()
        elif (choice2 == 3):
            wine()
        elif (choice2 == 4):
            breast_cancer()
    elif (choice1 == 2):
        exit()

def thankYou():
    print("""\033[36m

████████╗██╗░░██╗░█████╗░███╗░░██╗██╗░░██╗  ██╗░░░██╗░█████╗░██╗░░░██╗██╗
╚══██╔══╝██║░░██║██╔══██╗████╗░██║██║░██╔╝  ╚██╗░██╔╝██╔══██╗██║░░░██║██║
░░░██║░░░███████║███████║██╔██╗██║█████═╝░  ░╚████╔╝░██║░░██║██║░░░██║██║
░░░██║░░░██╔══██║██╔══██║██║╚████║██╔═██╗░  ░░╚██╔╝░░██║░░██║██║░░░██║╚═╝
░░░██║░░░██║░░██║██║░░██║██║░╚███║██║░╚██╗  ░░░██║░░░╚█████╔╝╚██████╔╝██╗
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚═════╝░╚═╝
    \033[0m""")

def iris():
        from sklearn import datasets
        data = datasets.load_iris()
        df = pd.DataFrame(data.data, columns = data.feature_names)
        df['label'] = pd.DataFrame(data.target)
        print(df.shape)
        print(df.head)
        col1 = int(input("Enter the first column pair: "))
        col2 = int(input("Enter the second column pair: "))
        fileName = input("Enter file name: ")
        madeByPython(df, "Library Python Spicy",data.feature_names[col1],data.feature_names[col2],col1,col2,data.target_names,fileName+"python")
        madeByMe(df, "Library myConvexHull",data.feature_names[col1],data.feature_names[col2],col1,col2,data.target_names,fileName)

def digits():
        from sklearn import datasets
        data = datasets.load_digits()
        df = pd.DataFrame(data.data, columns = data.feature_names)
        df['label'] = pd.DataFrame(data.target)
        print(df.shape)
        print(df.head)
        col1 = int(input("Enter the first column pair: "))
        col2 = int(input("Enter the second column pair: "))
        fileName = input("Enter file name: ")
        madeByPython(df, "Library Python Spicy",data.feature_names[col1],data.feature_names[col2],col1,col2,data.target_names,fileName+"python")
        madeByMe(df, "Library myConvexHull",data.feature_names[col1],data.feature_names[col2],col1,col2,data.target_names,fileName)

def wine():
        from sklearn import datasets
        data = datasets.load_wine()
        df = pd.DataFrame(data.data, columns = data.feature_names)
        df['label'] = pd.DataFrame(data.target)
        print(df.shape)
        print(df.head)
        col1 = int(input("Enter the first column pair: "))
        col2 = int(input("Enter the second column pair: "))
        fileName = input("Enter file name: ")
        madeByPython(df, "Library Python Spicy",data.feature_names[col1],data.feature_names[col2],col1,col2,data.target_names,fileName+"python")
        madeByMe(df, "Library myConvexHull",data.feature_names[col1],data.feature_names[col2],col1,col2,data.target_names,fileName)

def breast_cancer():
        from sklearn import datasets
        data = datasets.load_breast_cancer()
        df = pd.DataFrame(data.data, columns = data.feature_names)
        df['label'] = pd.DataFrame(data.target)
        print(df.shape)
        print(df.head)
        col1 = int(input("Enter the first column pair: "))
        col2 = int(input("Enter the second column pair: "))
        fileName = input("Enter file name: ")
        madeByPython(df, "Library Python Spicy",data.feature_names[col1],data.feature_names[col2],col1,col2,data.target_names,fileName+"python")
        madeByMe(df, "Library myConvexHull",data.feature_names[col1],data.feature_names[col2],col1,col2,data.target_names,fileName)

def madeByMe(df, title, xLabel, yLabel, xCol, yCol, labelName, fileName):
    plt.figure(figsize = (10, 6))
    labelSize = len(df['label'].unique())
    color = color2(labelSize)

    plt.title(title)
    plt.xLabel(xLabel)
    plt.yLabel(yLabel)
    
    print("Such points that are located in convex hull are in the list below:")
    for i in range(labelSize):
        bucket = df[df['label'] == i]
        bucket = bucket.iloc[:, [xCol, yCol]].values
        hull = myConvexHull(bucket)
        plt.scatter(bucket[:, 0], bucket[:, 1], label = labelName[i], color = color[i])
        print(hull)
        for simplex in hull:
            plt.plot(bucket[simplex, 0], bucket[simplex, 1], color = color[i])
    plt.legend()
    plt.savefig('output/' + fileName)
    plt.show()

def madeByPython(df, title, xLabel, yLabel,xCol, yCol, labelName, fileName):
    plt.figure(figsize = (10, 6))
    labelSize = len(df['label'].unique())
    color = color1(labelSize)

    plt.title(title)
    plt.xLabel(xLabel)
    plt.yLabel(yLabel)

    for i in range(labelSize):
        bucket = df[df['label'] == i]
        bucket = bucket.iloc[:, [xCol, yCol]].values
        hull = ConvexHull(bucket)
        plt.scatter(bucket[:, 0], bucket[:, 1], label = labelName[i], color = color[i])
        for simplex in hull.simplices:
            plt.plot(bucket[simplex, 0], bucket[simplex, 1], color = color[i])
    plt.legend()
    plt.savefig('output/' + fileName)

def color1(n):
    color = ['b','r','g','c','m','y','k','w']
    if n > len(color):
        for i in (range(n - len(color))):
            r = random.random()
            g = random.random()
            b = random.random()
            color.append((r, g, b))
    return color

def color2(n):
    color = ['y','b','m','c','g','y','k','w']
    if n > len(color):
        for i in (range(n - len(color))):
            r = random.random()
            g = random.random()
            b = random.random()
            color.append((r, g, b))
    return color

if __name__ == "__main__":
    header()
    logo()
    welcome()
    menu()
    thankYou()