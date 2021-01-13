#The area of Cylider
def calculateCylinder(H,R):
	volume = 22/7 * R ** 2 * H
	print(volume)
#The vulme of Surface
def calculateSurface(H,R):
	area =  2 * 22/7 * R * H + 2 * 22/7 * R ** 2
	print(area)

#Calling the functions
calculateCylinder(4,6)
calculateSurface(4,6)