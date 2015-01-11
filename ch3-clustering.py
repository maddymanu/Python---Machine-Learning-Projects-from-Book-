from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(min_df=1)

content = ["How to format my hard disk" , "Hard disk format problems"]
X = vectorizer.fit_transform(content)
print vectorizer.get_feature_names()

import os
import sys

from utils import DATA_DIR

TOY_DIR = os.path.join(DATA_DIR, "toy")

posts = [open(os.path.join(TOY_DIR , f)).read() for f in os.listdir(TOY_DIR)]
print posts