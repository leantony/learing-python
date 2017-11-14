#! /usr/bin/env python3
import re
import operator
import matplotlib.pyplot as plt

data = []
with open('alice.txt', 'r') as handler:
  data = handler.read()

s = data.split(' ')
words = {}
for x in s:
  if x is '\n' or len(x) < 2:
    continue
  else:
    if re.compile(r'[a-zA-Z0-9]').match(x): # take only alpha nums
      # add to words
      if x in words:
        count = words[x]
        words[x] = count + 1
      else:
        words[x] = 1
# print(words)

sorted_values = sorted(words.items(), key=operator.itemgetter(1), reverse=False)
k = [x[0] for x in sorted_values[-5:]]
v = [x[1] for x in sorted_values[-5:]]

print(k)
print(v)
plt.title('Graph of top 5 words')
plt.xlabel('word')
plt.ylabel('appearances')
plt.grid(True)
plt.plot(sorted(k), v)
plt.ylim(ymin=0)
plt.show()