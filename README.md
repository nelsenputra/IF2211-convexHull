# Tucil Stima 2 by Nelsen Putra
> Convex hull solver written in Python. Based on the concept of Divide and Conquer algorithm.


## Table of Contents
* [Introduction](#introduction)
* [General Information](#general-information)
* [Technologies Used](#technologies-used)
* [Setup](#setup)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Library](#library)
* [Contact](#contact)


## Introduction
Hello, everyone! Welcome to my GitHub Repository!

This project was created by:
| Name | Student ID | Class |
| :---: | :---: | :---: |
| Nelsen Putra | 13520130 | IF2211-01


## General Information
In geometry, the convex hull or convex envelope or convex closure of a shape is the smallest convex set that contains it. The convex hull may be defined either as the intersection of all convex sets containing a given subset of a Euclidean space, or equivalently as the set of all convex combinations of points in the subset. For a bounded subset of the plane, the convex hull may be visualized as the shape enclosed by a rubber band stretched around the subset.

A myConvexHull library written in Python can return the convex hull of a 2-dimensional data set (it can be considered a collection of 2D point). The set of points in a planar plane is called a convex if for any two points on the plane (eg. p and q), all line segments ending in p and q is in the set.

This program allows you to visualize Linear Separability test from 2 selected columns from dataset and must have dataset classification model in order to work. It will show you all the point from selected columns, legends, and the convex hull using matplotlib. 


## Technologies Used
The whole program was written in Python.


## Setup
### Installation
- Download and install [Python](https://www.python.org/downloads/)
- Install the whole modules and [libraries](#library) used in the source code
- Download the whole folders and files in this repository or do clone the repository

### Execution
1. Clone this repository in your own local directory

    `git clone https://github.com/nelsenputra/IF2211-convexHull.git`

2. Open the command line and change the directory to 'bin' folder

    `cd IF2211-convexHull`
    
3. Run `python main.py` on the command line

### Usage
1. After you run the program, you can choose the dataset you want to visualize
2. Select either from the test folder or sklearn dataset
3. Your dataset must categorized as dataset classification and have Target column in order to work
4. Select two columns that you want to visualize
5. There you go! The matplotlib will show you the dataset visualization


## Project Status
Project is: _complete_

All the specifications were implemented, including bonus.


## Room for Improvement
- A faster or more efficient algorithm to make the program run quicker
- A better interface development to satisfy the users


## Acknowledgements
- This project was based on [Spesifikasi Tugas Kecil 2 Stima](https://informatika.stei.itb.ac.id/~rinaldi.munir/Stmik/2021-2022/Tugas-Kecil-2-(2022).pdf)
- Thanks to God
- Thanks to Mrs. Masayu Leylia Khodra, Mrs. Nur Ulfa Maulidevi, and Mr. Rinaldi as our lecturers
- Thanks to academic assistants
- This project was created to fulfill our Small Project for IF2211 Algorithm Strategies


## Library
- [numpy](https://numpy.org/install/)
- [pandas](https://pandas.pydata.org/docs/getting_started/install.html)
- [matplotlib](https://matplotlib.org/stable/users/installing/index.html)
- [sklearn](https://scikit-learn.org/stable/install.html)
- [random](https://docs.python.org/3/library/random.html)
- [scipy](https://scipy.org/install/)


## Contact
Created by Nelsen Putra. 2022 All Rights Reserved.
