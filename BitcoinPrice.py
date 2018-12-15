import urllib2
import json
import pprint
import sched, time
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import os
import shutil


# Variables

percentDifference = 1
hasStarted = 0
value = str(0)
valueFloat = float(value)
updatedValue = str(value)
updatedValueFloat = float(updatedValue)
mydir = os.path.dirname(os.path.abspath(__file__))
dataFolder = 'Coin Data'
x = []
y = []

#Clear Data

contChoice = raw_input('Would you like to clear the files? (Y/N) ')
if(contChoice.upper() == 'Y') :
	print('Clearing Data')
	
	# Delete Folder
	
	if os.path.isdir(dataFolder) :
		shutil.rmtree(dataFolder)
		
	
	# Remake Folder
	if not os.path.exists(dataFolder) :
		os.makedirs(dataFolder)

	
# Get Coin
	
coin = raw_input('Enter the coin ticker: ')
	
# Make Capital
	
coinT = coin.upper() 

# Tell user what they chose

print('You chose: ' + coinT) 

def valueFunc() :
			
			#Make Data Folder
				
			global hasStarted
			global value
			global valueFloat
			global updatedValue
			global updatedValueFloat
			if(hasStarted == 0) :
				
				if not os.path.exists(dataFolder) :
					os.makedirs(dataFolder)
				
				base = urllib2.urlopen('https://min-api.cryptocompare.com/data/price?fsym=' + coinT + '&tsyms=USD')
				data = json.load(base)

				value = str(data["USD"])
				valueFloat = float(value)
				#time.sleep(5)
				
				print(coinT + ' Starting Value: $' + value)
				
				os.chdir(dataFolder)
				
				hasStarted = hasStarted + 1
				
				
		
			base = urllib2.urlopen('https://min-api.cryptocompare.com/data/price?fsym=' + coinT + '&tsyms=USD')
			data = json.load(base)
			global updatedValue
			global updatedValueFloat
			updatedValue = str(data["USD"])   
			updatedValueFloat = float(updatedValue)
				
			percentDifference = round(abs(float((((valueFloat - updatedValueFloat) / valueFloat) * 100))), 2)
			
			# if(percentDifference < 0.05) :
				
				
				
			# print(str(percentDifference))
			# percentNumber = percentDifference * 10
			print(coinT + ' Value: $' + updatedValue)
			#print('Value Changed: ' + str((percentDifference)) + '%')
			logPricef = open(coinT + "_price_change.txt","a")
			logPricef.write(updatedValue + "\n")
			timeLoggedf = open(coinT + "_time_change.txt","a")
			timeLoggedf.write(str(datetime.now()) + "\n")
			value = updatedValue
			valueFloat = updatedValueFloat
			# time.sleep(10)
			plot()
				



def plot() :
	global hasStarted
	global value
	global valueFloat
	global updatedValue
	global updatedValueFloat
	global coinT
	global x
	global y
	
	timeNow = np.loadtxt(coinT + '_time_change.txt')
	timeString = timeNow.strftime('%Y-%m-%d')
	
	x = np.loadtxt(timeString, delimiter='\n', unpack = True)
	y = np.loadtxt(coinT + '_price_change.txt', delimiter='\n', unpack = True)

	
	plt.plot(x,y, label='test')
	
	plt.xlabel('x')
	plt.ylabel('y')
	plt.legend()
	plt.show()
	
	
	
	


while (abs(percentDifference) >= 0) :
	valueFunc()





