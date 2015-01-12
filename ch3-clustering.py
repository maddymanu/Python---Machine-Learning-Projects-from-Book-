from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(min_df=1 , stop_words='english')

content = ["How to format my hard disk" , "Hard disk format problems"]
X = vectorizer.fit_transform(content)
print X
print vectorizer.get_feature_names()

import os
import sys
import scipy as sp

# from utils import DATA_DIR

TOY_DIR = os.path.join(os.path.dirname(__file__), "toy")

posts = [open(os.path.join(TOY_DIR , f)).read() for f in os.listdir(TOY_DIR)]
posts.pop(0)


new_post = "imaging databases"


import nltk.stem
english_stemmer = nltk.stem.SnowballStemmer('english')

class StemmedCountVectorizer(CountVectorizer):
	def build_analyzer(self):
		analyzer = super(StemmedCountVectorizer,self).build_analyzer()
		return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))

vectorizer = StemmedCountVectorizer(min_df=1, stop_words='english')

from sklearn.feature_extraction.text import TfidfVectorizer
class StemmedTfidfVectorizer(TfidfVectorizer):
	def build_analyzer(self):
		analyzer = super(TfidfVectorizer,self).build_analyzer()
		return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))


vectorizer = StemmedTfidfVectorizer(min_df=1, stop_words='english', charset_error='ignore')
X_train = vectorizer.fit_transform(posts)
num_samples , num_features = X_train.shape
print posts
new_post_vec = vectorizer.transform([new_post])

def dist_raw(v1, v2):
    delta = v1 - v2
    return sp.linalg.norm(delta.toarray())

def dist_norm(v1, v2):
    v1_normalized = v1 / sp.linalg.norm(v1.toarray())
    v2_normalized = v2 / sp.linalg.norm(v2.toarray())

    delta = v1_normalized - v2_normalized

    return sp.linalg.norm(delta.toarray())

best_doc = None
best_dist = sys.maxint
best_i = None
for i in range(0 , num_samples):
	post = posts[i]
	if post == new_post:
		continue
	post_vec = X_train.getrow(i)
	d = dist_norm(post_vec , new_post_vec)
	print ("===== Post %i with dist=%.2f: %s" %(i , d , post))
	if d < best_dist:
		best_dist = d
		best_i = i

print("Best post is %i with dist=%.2f" % (best_i, best_dist))




