import numpy as np
import matplotlib.pyplot as plot

data1_file_name = '../donnes_problematique/S2GE_APP3_Problematique_Detecteur_Primaire.csv'
data2_file_name = '../donnes_problematique/S2GE_APP3_Problematique_Detecteur_Secondaire.csv'

data1 = np.loadtxt(data1_file_name, delimiter=',', skiprows=1)
data2 = np.loadtxt(data2_file_name, delimiter=',', skiprows=1)

