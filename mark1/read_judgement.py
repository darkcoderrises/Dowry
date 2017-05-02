import sys
from collections import Counter
from textblob import TextBlob
import numpy as np
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import re

m = ["../"+i for i in filter(bool, open("in").read().split("\n"))]
t = []

for j,i in enumerate(m):
    try:
        f = open(unicode(i)).read().replace('\r', ' ').lower()
        regex = re.compile('[^a-zA-Z]')
        f = regex.sub(' ', f)
        f = filter(bool, f.split(' '))
        t.extend(f)
    except:
        pass

stop = set(stopwords.words('english'))
t = filter(lambda i: i not in stop, t)
t = filter(lambda i: wordnet.synsets(i), t)

c = Counter(t)
length = len(c.keys())
keys = []
values = []

val = float(sys.argv[1])

for index, i in enumerate(c.most_common(int(val*length))):
#    if index < int(float(sys.argv[2])*length):
#        continue

    keys.append(i[0])
    values.append(i[1])

y_pos = np.arange(len(values))
res = filter(lambda a: len(a)>2, keys)
print res
print len(res)

fi = open('in1', 'w+')
for i in res:
    fi.write(i)
    fi.write('\n')
fi.close()

#plt.bar(y_pos, values, align='center', alpha=0.5)
#plt.xticks(y_pos, keys)
#plt.show()
