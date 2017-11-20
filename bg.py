#! /usr/bin/env python3
import re
import math

def get_file_data(file):
    file_data =[]
    with open(file, 'r') as handle:
        for data in handle:
        	if re.compile("[\'\"`\|\/\+\#\,\)\(\?\!\B\-\:\=\;\.\«\»\—\@]").match(data):
        		continue
        	else:
        		file_data.append(data)
    return file_data


def get_bi_grams(data):
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

def train(bi_grams, data):
	apps = get_counts(bi_grams)
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

data = get_file_data('train.txt')
bg = get_bi_grams(data)
# print(c)
ls = str(data).split(" ")
# print(ls.count(ls[1]))
results = train(bg, ls)