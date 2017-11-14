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

print("===============================================================")
print("scanning {0} for links. This might take a while....".format(url))

scanned = []
url_regexp = '"((http|ftp)s?://.*?)"'
p_tags_regexp = '<p (class|id)=(.*?)>(.*?)<\/p>'
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
              if re.compile(r'[<>/{}[\]~`|class=(.*?)]').match(w): # skip invalid chars
                continue
              else:
                apps = words_scanned[w] # how many times it intially appeared
                words_scanned[w] = apps + 1
                statistics[url] = words_scanned
            else:
              words_scanned[w] = 1 # intial appearances
      
        links = re.findall(url_regexp, str(words)) # find the links in the paragraphs identified above
        for link in links:
            # the link is a tuple, so we access the first item, which is the link
            items.add(link[0])
        print("successfully printed {0} links from {1}".format(len(links), url))
        for x in items.copy():
          if depth == depth_max:
            print("depth reached.")
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
              scan(x, items, depth=depth+1)
  except urllib.error.URLError as e:
      print(e.reason) # error

# draw a graph
def draw_graph(sorted_values, top = 50):
	k = [x[0] for x in sorted_values[-top:]]
	v = [x[1] for x in sorted_values[-top:]]
	print(k)
	print(v)
	plt.title('Graph of top 50 words found')
	plt.xlabel('word')
	plt.ylabel('appearances')
	plt.grid(True)
	plt.plot(sorted(k), v)
	plt.ylim(ymin=0)
	plt.show()

# call the dfs scanner
def perform_work():
  time_start = time.time()
  scan(url);
  time_end = time.time()
  print("==========================================================")
  print('task finished in {} ms'.format(int(time_end - time_start * 1000)))

# start everything
perform_work()