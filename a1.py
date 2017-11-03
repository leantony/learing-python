#! /usr/bin/env python3

import urllib.request
from operator import itemgetter
from collections import OrderedDict
import re
import matplotlib.pyplot as plotlib

url = 'https://' + input("please enter a https url (without https://). E.g www.twitter.com\n")

print("===============================================================")
print("scanning {0} for links. This might take a while....".format(url))

items = set()
scanned = []
words_to_ignore = ["the", "at", "&nbsp", "n", ".js"]
words_scanned = []
scanned_appearances = {}
statistics = {}
def scan(url, depth=0, depth_max=10):
  try:
    with urllib.request.urlopen(url) as response:
        html = str(response.read())
        print("site content length is {0}".format(len(html)))
        marked = 0
        # words
        words = re.compile(r'<[^>]+>').sub('', html) # ignore html tags
        stripped_words = re.findall(r'\w+', words) # fetch words only
        for w in stripped_words:
          if w in words_to_ignore:
            # ignore set words
            continue
          else:
            if w in words_scanned:
              scanned_appearances[w] = c = marked = marked + 1 # how namy times the word appears
              statistics[url] = scanned_appearances
            else:
              words_scanned.append(w)
        links = re.findall('"((http|ftp)s?://.*?)"', html)
        for link in links:
            items.add(link[0]) # add the link to the list
        print("successfully printed {0} links from {1}".format(len(links), url))
        for x in items:
          if depth == depth_max:
            print("depth reached.")
            # print(scanned)
            # print(words_scanned)
            plotlib.scatter(range(1, len(statistics)), statistics.items())
            plotlib.show()

            exit(0)
          else:
            if x in scanned:
              print("ignoring link {0}".format(x))
              continue
            else:
              scanned.append(x)
              scan(x, depth=depth+1)
  except urllib.error.URLError as e:
      print(e.reason)


scan(url);

graph = {url: set(items)};

# print(graph);
# def dfs(graph, start, visited=None, d_max=10):
#     depth=0
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     for next in graph[start] - visited:
#         if depth >= d_max:
#           print("exhausted depths...");
#           break;
#         else:
#           depth+=1;
#           dfs(graph, next, visited)
#     return visited


# result = dfs(graph, 'A');
# print(result);