from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(min_df=1 , stop_words='english')

content = ["How to format my hard disk" , "Hard disk format problems"]
X = vectorizer.fit_transform(content)
print X
print vectorizer.get_feature_names()

import os
import sys
import scipy as sp
import nltk

# from utils import DATA_DIR

TOY_DIR = os.path.join(os.path.dirname(__file__), "toy")

posts = [open(os.path.join(TOY_DIR , f)).read() for f in os.listdir(TOY_DIR)]
posts.pop(0)
print posts

X_train = vectorizer.fit_transform(posts)
print X_train
num_samples , num_features = X_train.shape

print num_samples

new_post = "imaging databases"
new_post_vec = vectorizer.transform([new_post])


def dist_raw(v1, v2):
    delta = v1 - v2
    return sp.linalg.norm(delta.toarray())


best_doc = None
best_dist = sys.maxint
best_i = None
for i in range(0 , num_samples):
	post = posts[i]
	if post == new_post:
		continue
	post_vec = X_train.getrow(i)
	d = dist_raw(post_vec , new_post_vec)
	print ("===== Post %i with dist=%.2f: %s" %(i , d , post))
	if d < best_dist:
		best_dist = d
		best_i = i

print("Best post is %i with dist=%.2f" % (best_i, best_dist))




