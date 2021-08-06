import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

##	'longitude', 'latitude', 'housing_median_age', 'total_rooms',
##	'total_bedrooms', 'population', 'households', 'median_income',
##	'median_house_value'

df = pd.read_csv('../california_housing_train.csv')
print(df.mean())

def sea():
	# seaborn
	for s in df.columns:
		sns.distplot(s)
		plt.show()

def lalo():
	# 緯度経度
	plt.xlabel('latitude')
	plt.ylabel('longitude')
	plt.grid()
	plt.scatter(df['longitude'],df['latitude'],s=5,alpha=0.1,c=red)
	plt.show()

def pota():
	# 人数と部屋の数
	plt.xlabel('population')
	plt.ylabel('total_rooms')
	plt.scatter(df['total_rooms'],df['population'],s=5,alpha=0.1)
	plt.show()

	plt.xlabel('population')
	plt.ylabel('total_rooms')
	plt.xlim(0,10000)
	plt.ylim(0,5000)
	plt.scatter(df['total_rooms'],df['population'],s=5,alpha=0.05)
	plt.show()

def func():
	#試し
	lis = [i/j for (i,j) in zip(df['population'],df['households'])];
	lis = pd.DataFrame({'pop/hou':lis})
	sns.distplot(lis)
	plt.show()

def main():
	#sna()
	#lalo()
	#pota()
	func()



if __name__ == '__main__':
	main()