#! /usr/bin/env python3
import random
import statistics as st
import matplotlib.pyplot as plotlib

temp_ranges_max = 36 # max allowed random temperature
temp_ranges_min = 10 # min allowed temperature
# months and days
months = [
	{
		"month": "jan", "days": 31
	},
	{
		"month": "feb", "days": 28
	},
	{
		"month": "march", "days": 31
	},
	{
		"month": "april", "days": 30
	},
	{
		"month": "may", "days": 31
	},
	{
		"month": "june", "days": 30
	},
	{
		"month": "july", "days": 31
	},
	{
		"month": "august", "days": 31
	},
	{
		"month": "sept", "days": 30
	},
	{
		"month": "oct", "days": 31
	},
	{
		"month": "nov", "days": 30
	},
	{
		"month": "dec", "days": 31
	},
]

t_overall = [];
month_values = [];
sd_values = [];
for x in months:
	m = x.get('month')
	month_values.append(m)
	d = x.get('days')
	t_days = []
	for num in range(1, d + 1): # 1 and last value inclusive
		temp = random.randrange(temp_ranges_min, temp_ranges_max)
		t_days.append(temp)
	sd = st.stdev(t_days) # just use stdev, because its there
	t_overall.append({"month": m, "temps": t_days, "s_dev": sd})
	sd_values.append(sd)
	t_days = []; # reset days to empty list
print(t_overall)
print(month_values)
print(sd_values)

# error when using string values, so resort to some numeric value temporarily
plotlib.scatter(range(1, 13), sd_values)
plotlib.show()

# end