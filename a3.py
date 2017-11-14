#! /usr/bin/env python3
import re
import operator
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import statistics as st

def scan_file(file='alice.txt'):
  data = []
  with open(file, 'r') as handler:
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
  return words

def draw_histogram(x_values, y_values):
  mean = sum(y_values)/len(y_values)
  sdev = st.stdev(y_values)
  plt.title('Histogram of top 5 words')
  plt.xlabel('word')
  plt.ylabel('appearances')
  plt.grid(True)
  n, bins, patches = plt.hist(y_values, 10, normed=1, facecolor='blue', alpha=0.5)
  y = mlab.normpdf(bins, mean, sdev)
  plt.plot(bins, y, 'r--')
  plt.show()
  # plt.plot(sorted(k), v)
  # plt.ylim(ymin=0)
  # plt.show()

def draw_line_graph(x_values, y_values):
  plt.title('Graph of top 5 words')
  plt.xlabel('word')
  plt.ylabel('appearances')
  plt.grid(True)
  plt.plot(sorted(x_values), y_values)
  plt.ylim(ymin=0)
  plt.show()


words = scan_file()
sorted_values = sorted(words.items(), key=operator.itemgetter(1), reverse=False)
k = [x[0] for x in sorted_values[-20:]]
v = [x[1] for x in sorted_values[-20:]]

print(k)
print(v)
draw_line_graph(k, v)