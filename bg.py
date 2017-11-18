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

def calculate_probablities(apps, data):
	size = len(apps)
	keys = [list(x) for x in apps.keys()]
	# print(keys[1])
	items = [i[1] for i in apps.items()]
	results = {}
	for x in range(0, size):
		f1 = data.count(data[x])
		f2 = data.count(data[x + 1])
		# print("{0}, {1}".format(f1, f2))
		ngram_prob = math.log(f1/f2, 10)
		results[tuple(keys[x])] = ngram_prob
	print(results)
	# for x in range(0, size):
	# 	l = keys[x]
	# 	print(l)
	# for key, value in apps:
		# print(app)
		# print(value)
		# if(len(key) > 0):
		# 	l = str(key).split()
		# 	print(l)
		# 	f1 = data.count(l[0])
		# 	f2 = data.count(l[1])
		# 	ngram_prob = value/f1
		# 	print(ngram_prob)
		# else:
		# 	continue

data = get_file_data('alice.txt')
bg = get_bi_grams(data)
c = get_counts(bg)
# print(c)
ls = str(data).split(" ")
# print(ls.count(ls[1]))
calculate_probablities(c, ls)