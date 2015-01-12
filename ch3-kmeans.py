import sklearn.datasets

MLCOMP_DIR = r"/Users/adityabansal/Documents"
data = sklearn.datasets.load_mlcomp("20news-18828", mlcomp_root=MLCOMP_DIR)
print(data.filenames)