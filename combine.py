import os
import glob
import pandas as pd

os.chdir("benign_features/")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

for i in all_filenames:
    data = []
    with open(i,'r') as f:
        data = f.readlines()
    with open('../benign_dataset.arff','a') as f:
        for j in data:
            f.write(j)
