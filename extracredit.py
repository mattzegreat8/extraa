def OddOdd(values):
	Toggle= True
	SumToReturn= 0
	for value in values:
		if(Toggle == True):
			if(value%2 == 1):
				SumToReturn= SumToReturn + value
		Toggle= not Toggle 
	return SumToReturn


print(OddOdd([1,3,5,7,9]))
print(OddOdd([2,5,5,7,6,6,6]))
print(OddOdd([1,1,1,1,1,1,1,1]))
print(OddOdd([2,2,2,2,2,2,2,2,22,2]))