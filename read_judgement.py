import sys
from collections import Counter
from textblob import TextBlob
import numpy as np
import matplotlib.pyplot as plt

m = filter(bool, open("in").read().split("\n"))
t = []

for j,i in enumerate(m):
    try:
        f =  open(i).read().replace('\r', ' ').lower().replace('\n', ' ').replace('.',' ').replace('-', ' ').replace(',',' ').replace(":", " ").replace('`', ' ').replace('=',' ').replace('(', ' ').replace(')', ' ')
        for i in range(10):
            f = f.replace(str(i), '')
        f = f.split(" ")
        f = filter(bool, f)
        t.extend(f)
    except:
        pass

c = Counter(t)
length = len(c.keys())
keys = []
values = []

val = float(sys.argv[1])

for index, i in enumerate(c.most_common(int(val*length))):
    if index < int(float(sys.argv[2])*length):
        continue

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
