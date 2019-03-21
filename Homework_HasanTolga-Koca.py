import math

count = int(input('give number of coordinates: '))

listX = []
listY = []
result = zip()

resultList = list(result)
#question1
for x in range(count):
	listX.append(float(input('Input x coordinate: ')))
	listY.append(float(input('Input y coordinate: ')))
result = zip(listX, listY)

print ('your set is: ')
for value in result:
  print (value)

#question2
sumX = 0
sumY = 0
x = 0
for x in range(count):
	sumX += listX[x]
	sumY += listY[x]
comX = sumX/count
comY = sumY/count
print ('center of mass is (', comX, ',' , comY, ')')

#question3
listD = []
for x in range(count):
	listD.append(math.sqrt(math.pow(comX-listX[x],2)+math.pow(comY-listY[x],2)))
print ('distance list is ' , listD)

#question4
closest = 0
farthest = 0
for x in range(1,count):
	if listD[x] > listD[farthest]:
		farthest = x
	if listD[x] < listD[closest]:
		closest = x

print ('closest is ', listX[closest],',',listY[closest], ' and the distance is ',listD[closest]) 
print ('farthest is ', listX[farthest],',',listY[farthest], ' and the distance is ',listD[farthest]) 
