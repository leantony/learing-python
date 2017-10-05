#! /usr/bin/env python3

import urllib.request
import re

url = 'https://' + input("please enter a https url (without https://). E.g www.twitter.com\n")

print("===============================================================")
print("scanning {0} for links. This might take a while....".format(url))
try:
  with urllib.request.urlopen(url) as response:
      html = str (response.read())
      print("site content length is {0}".format(len(html)))
      links = re.findall('"((http|ftp)s?://.*?)"', html)
      print("=============================================================")
      for link in links:
          print(str(link[0]) + ',')
      print("=========================================================")
      print("successfully printed {0} links from {1}".format(len(links), url))
except urllib.error.URLError as e:
    print(e.reason)
