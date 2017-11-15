#! /usr/bin/env python3
import csv
from collections import defaultdict

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


def gradient_descent(data):
	lot_area = data[0]
	sale_price = data[1]
	if(len(lot_area) != len(sale_price)):
		raise ValueError('Both lot area and sales price need to be of same lengths')
	a = 1
	b = 1
	# Ypred = a + b X,
	ypred = [a + (lot_area[s] * b) for s in lot_area if type(s) == int]
	print(ypred)
		


data = extract_data()
processed_data = process_data(data)

gradient_descent(processed_data)