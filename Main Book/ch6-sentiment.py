from utils import load_sanders_data
import numpy as np

X_orig, Y_orig = load_sanders_data()
classes = np.unique(Y_orig)

print X_orig