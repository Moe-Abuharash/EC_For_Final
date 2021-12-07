from operator import itemgetter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from textblob import TextBlob
import nltk
from pathlib import Path
import pandas as pd

import textblob
# nltk.download("stopwords")

stops = stopwords.words("english")

#blob = TextBlob("Today is a beautiful day.")

# print(blob.words)

text = TextBlob(Path("comments.txt").read_text())

# print(cleanlist)

blob1 = []
blob1 += text.noun_phrases
items = text.word_counts.items()
# print(items)


cleanitems = [i for i in items if i[0] in blob1 and i[0] not in stops]
sorted_list = sorted(cleanitems, key=itemgetter(1), reverse=True)

top = sorted_list[1:21]

all_of_them = " "
for i in all_of_them:
    all_of_them += i[0]
    all_of_them += " "


df = pd.DataFrame(top, columns=["word", "count"])

print(df)


axes = df.plot.bar(x="word", y="count", legend=False,
                   color=["y", "c", "m", "b", "g", "r"])

plt.gcf().tight_layout

plt.show()
