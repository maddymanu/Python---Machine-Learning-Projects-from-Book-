import sklearn.datasets

MLCOMP_DIR = r"/Users/adityabansal/Documents"
data = sklearn.datasets.load_mlcomp("20news-18828", mlcomp_root=MLCOMP_DIR)

groups = ['comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.ma c.hardware', 'comp.windows.x', 'sci.space']
train_data = sklearn.datasets.load_mlcomp("20news-18828", "train" , mlcomp_root=MLCOMP_DIR, categories=groups)

print(len(train_data.filenames))
# got the beginning data 

import nltk.stem
english_stemmer = nltk.stem.SnowballStemmer('english')

from sklearn.feature_extraction.text import TfidfVectorizer
class StemmedTfidfVectorizer(TfidfVectorizer):
	def build_analyzer(self):
		analyzer = super(TfidfVectorizer,self).build_analyzer()
		return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))


vectorizer = StemmedTfidfVectorizer(min_df=10, max_df=0.5, stop_words='english', charset_error='ignore')
vectorized = vectorizer.fit_transform(train_data.data)
num_samples, num_features = vectorized.shape
print("#samples: %d, #features: %d" % (num_samples, num_features))


num_clusters = 50
from sklearn.cluster import KMeans
km = KMeans(n_clusters=num_clusters, init='random', n_init=1,
   verbose=1)
km.fit(vectorized)

