#! /usr/bin/env python3

import urllib.request
import operator
import re
import time
import matplotlib.pyplot as plt

url = input("please enter a https url (without https://). E.g www.twitter.com\n")
if url is "": # use a default url
  url = 'https://' + 'www.twitter.com'
else:
  url = 'https://' + url
time_start = time.time()
print("===============================================================")
print("scanning {0} for links. This might take a while....".format(url))

scanned = []
url_regexp = '"((http|ftp)s?://.*?)"'
p_tags_regexp = '<(b|p|li|div|span) (class|id)=(.*?)>(.*?)<\/(b|p|li|div|span)>' # scan a subset of html tags
words_to_ignore = [" ", "target=\"_blank\"", "[", "]", '\\\\n']
words_scanned = {}
statistics = {}

# dfs scanner to scan links in html <p> elements
def scan(url, items = set(), depth=0, depth_max=10):
  try:
    with urllib.request.urlopen(url) as response:
        html = str(response.read())
        print("site content length is {0}".format(len(html)))
        # words
        pattern = re.compile(p_tags_regexp, re.DOTALL) # use paragraphs as instructed
        words = pattern.findall(html)
        
        for w in str(words).split(' '):
          if w in words_to_ignore or len(w) < 2:
            # ignore set words
            continue
          else:
            if w in words_scanned:
              if re.compile(r'[\'\"<>/{}&@[\]()=~(-)`|{class|type|role|height|width|href|viewbox|data*|id=(.*?)}]').match(w): # skip invalid chars
                print("skipping {0} since its invalid...".format(w))
                continue
              else:
                apps = words_scanned[w] # how many times it intially appeared
                tn = apps + 1
                words_scanned[w] = tn
                statistics[url] = words_scanned
                print("adding occurrence {0} of {1}...".format(tn, w))
            else:
              words_scanned[w] = 1 # intial appearances
              print("adding first occurence of {0}".format(w))
      
        links = re.findall(url_regexp, str(words)) # find the links in the paragraphs identified above
        for link in links:
            # the link is a tuple, so we access the first item, which is the link
            items.add(link[0])
        print("{0} links found at {1}".format(len(links), url))
        for x in items.copy():
          if depth == depth_max:
            time_end = time.time()
            print("depth reached.")
            print("==========================================================")
            print('task finished in {}s'.format(int(time_end - time_start)))
            sorted_values = sorted(words_scanned.items(), key=operator.itemgetter(1), reverse=False)
            # print(sorted_values)
            draw_graph(sorted_values)
            exit(0)
          else:
            if x in scanned:
              print("ignoring link {0}".format(x))
              continue
            else:
              scanned.append(x)
              print("scanning {0}".format(x))
              scan(x, items, depth=depth+1)
  except urllib.error.URLError as e:
      print(e.reason) # error

# draw a graph
def draw_graph(sorted_values, top = 10):
	k = [x[0] for x in sorted_values[-top:]]
	v = [x[1] for x in sorted_values[-top:]]
	print(k)
	print(v)
	plt.title('Graph of top {0} words found'.format(top))
	plt.xlabel('word')
	plt.ylabel('appearances')
	plt.grid(True)
	plt.plot(sorted(k), v)
	plt.ylim(ymin=0)
	plt.show()

# call the dfs scanner
def perform_work():
  scan(url)

# start everything
perform_work()
