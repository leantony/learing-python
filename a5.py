#! /usr/bin/env python3
import csv
from collections import defaultdict
import numbers
import math

def extract_data(csv_file="train.csv"):
	columns = defaultdict(list)
	with open('train.csv', 'r') as f:
	    reader = csv.DictReader(f)
	    for row in reader:
	        for (k,v) in row.items():
	            columns[k].append(v)
	return columns


def process_data(data):
	lot_area = data['LotArea']
	sale_price = data['SalePrice']
	return (sale_price, lot_area)

def ignore_invalid(data):
	for x in data:
		try:
			yield int(x)
		except ValueError as e:
			continue

def mins(y):
	# y= y-min/y-Max - Miny
	values = sorted(y)
	biggest = values[len(values) - 1]
	smallest = values[0]
	for x in y:
		yield (x - smallest) / (biggest - smallest)


def gradient_descent(data):
	lot_area = [l for l in ignore_invalid(data[0])]
	sale_price = [s for s in ignore_invalid(data[1])]
	if(len(lot_area) != len(sale_price)):
		raise ValueError('Both lot area and sales price need to be of same lengths')
	a = 1
	b = 1
	
	# minimmum values
	ymin = [v for v in mins(lot_area)]

	# ypred
	ypred = [x for x in ab(ymin)]

	# sse
	sse_value = [y for y in sse(ypred, ymin)]

	diff = [j for j in diff_min_pred(ymin, ypred)]
	
	dmp = [k for k in diff_min_pred_st(diff, ymin)]

	print(a - (0.1 * sum(diff)))


def ab(data, a=1, b=1):
	for x in data:
		yield a + b * x

def sse(yp, y):
	# SSE=(½ (Y-YP)2) (0.5 * (x - i) * 2)
	for x in range(0, len(yp)):
		v = math.pow(0.5 * (y[x] - yp[x]), 2)
		yield v

def diff_min_pred(y, yp):
	# -y -ypred
	for x in range(0, len(y)):
		yield -(y[x] - yp[x])

def diff_min_pred_st(mp, ymin):
	for x in range(0, len(mp)):
		yield mp[x] * ymin[x]

data = extract_data()
processed_data = process_data(data)

gradient_descent(processed_data)