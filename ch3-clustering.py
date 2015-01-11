from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(min_df=1)

content = ["How to format my hard disk" , "Hard disk format problems"]
X = vectorizer.fit_transform(content)
print vectorizer.get_feature_names()

import os
import sys

# from utils import DATA_DIR

TOY_DIR = os.path.join(os.path.dirname(__file__), "toy")

posts = [open(os.path.join(TOY_DIR , f)).read() for f in os.listdir(TOY_DIR)]
posts.pop(0)
print posts

X_train = vectorizer.fit_transform(posts)
num_samples , num_features = X_train.shape

print num_samples

new_post = "imaging databases"
new_post_vec = vectorizer.transform([new_post])

print new_post_vec