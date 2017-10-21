#! /usr/bin/env python3
a = set([1, 2, 2, 3])
b = set([3, 7, 9, 5])
print(a & b)


def my_function(*args):
	return sum(args)
print(my_function(10, 50, 90, 5, 20, 20))
print(lambda *args: (sum(args)) / 2)(3, 4, 4, 5, 4)