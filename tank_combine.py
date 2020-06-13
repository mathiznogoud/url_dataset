import os
import glob
import pandas as pd

os.chdir("phishtank_features/")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

for i in all_filenames:
    data = []
    with open(i,'r') as f:
        data = f.readlines()
    with open('../tank_dataset.arff','a') as f:
        for j in data:
            f.write(j)
