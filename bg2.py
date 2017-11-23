#! /usr/bin/env python3
import csv
from collections import defaultdict
import codecs
from nltk import bigrams
from nltk import NaiveBayesClassifier
from nltk.metrics import BigramAssocMeasures
from nltk.collocations import BigramCollocationFinder

def extract_data(csv_file="spam.csv"):
	columns = defaultdict(list)
	with codecs.open(csv_file, "r", encoding='utf-8', errors='ignore') as f:
	    reader = csv.DictReader(f)
	    for row in reader:
	        for (k,v) in row.items():
	            columns[k].append(v)
	return columns

def build_corpus(data):
	spam = []
	legit = []
	size = len(data['v1'])
	for x in range(0, size):
		if data['v1'][x] == 'ham':
			# print("adding legit msgs")
			legit.append(data['v2'][x])
		else:
			# print("adding spammy msgs")
			spam.append(data['v2'][x])
	return legit, spam

def create_bigrams(data):
	return [b for l in data for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]

def get_counts(bi_grams):
	data_size = len(bi_grams)
	apps = {}
	for x in range(0, data_size):
		b = bi_grams[x]
		if b in apps:
			apps[b] = apps[b] + 1
		else:
		    apps[b] = 1
	return apps

def get_probabilities(apps, data):
	size = len(apps)
	keys = [list(x) for x in apps.keys()]
	# print(keys[1])
	items = [i[1] for i in apps.items()]
	s_items = sum(items)
	results = {}
	# print(apps)
	for x in range(0, len(items)):
		count = items[x]
		prob = count / s_items
		results[tuple(keys[x])] = prob
	print(results)


extracted = extract_data()
legit, spam = build_corpus(extracted)
legit_corpus = create_bigrams(legit)
spam_corpus = create_bigrams(spam)
c = get_counts(spam_corpus)
cd = get_counts(legit_corpus)
bg = bigrams(legit)
print(get_probabilities(c, legit))
