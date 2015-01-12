import sklearn.datasets
import ch3-clustering

MLCOMP_DIR = r"/Users/adityabansal/Documents"
data = sklearn.datasets.load_mlcomp("20news-18828", mlcomp_root=MLCOMP_DIR)

groups = ['comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.ma c.hardware', 'comp.windows.x', 'sci.space']
train_data = sklearn.datasets.load_mlcomp("20news-18828", "train" , mlcomp_root=MLCOMP_DIR, categories=groups)

print(len(train_data.filenames))